import os
import sys
import random
import time
import torch
import multiprocessing
from collections import Counter

from cg.api import to_observation_class, search_begin, search_step, search_end, search_release
from cg.game import battle_start, battle_select, battle_finish
from featurizer import featurize_state

# We reuse the exact determinization and search logic from the spike,
# but cleaned up and optimized.

def read_deck(file_path="deck.csv") -> list[int]:
    if not os.path.exists(file_path):
        file_path = "/kaggle_simulations/agent/" + file_path
    with open(file_path, "r") as file:
        csv = file.read().split("\n")
    deck = []
    for i in range(60):
        deck.append(int(csv[i]))
    return deck

def get_visible_card_ids(state, target_player_idx):
    visible = []
    
    def add_card(c):
        if c and c.playerIndex == target_player_idx:
            visible.append(c.id)
            
    for p_idx in [0, 1]:
        p_state = state.players[p_idx]
        if p_state.active and p_state.active[0]:
            act = p_state.active[0]
            if p_idx == target_player_idx:
                visible.append(act.id)
            for c in act.preEvolution: add_card(c)
            for c in act.energyCards: add_card(c)
            for c in act.tools: add_card(c)
            
        for b in p_state.bench:
            if p_idx == target_player_idx:
                visible.append(b.id)
            for c in b.preEvolution: add_card(c)
            for c in b.energyCards: add_card(c)
            for c in b.tools: add_card(c)
            
        for c in p_state.discard:
            add_card(c)
            
        if p_state.hand:
            for c in p_state.hand:
                add_card(c)
                
    if state.stadium:
        add_card(state.stadium[0])
        
    if state.looking:
        for c in state.looking:
            add_card(c)
            
    return visible

def determinize(obs, starting_deck):
    state = obs.current
    your_idx = state.yourIndex
    opp_idx = 1 - your_idx
    
    me = state.players[your_idx]
    opp = state.players[opp_idx]
    
    starting_counts = Counter(starting_deck)
    
    # 1. Self
    my_visible = get_visible_card_ids(state, your_idx)
    my_visible_counts = Counter(my_visible)
    my_unseen = []
    for cid, count in starting_counts.items():
        unseen_count = max(0, count - my_visible_counts.get(cid, 0))
        my_unseen.extend([cid] * unseen_count)
    random.shuffle(my_unseen)
    
    your_deck = my_unseen[:me.deckCount]
    your_prize = my_unseen[me.deckCount:me.deckCount + len(me.prize)]
    if len(your_deck) < me.deckCount:
        your_deck += [3] * (me.deckCount - len(your_deck))
    if len(your_prize) < len(me.prize):
        your_prize += [3] * (len(me.prize) - len(your_prize))
        
    # 2. Opponent
    opp_visible = get_visible_card_ids(state, opp_idx)
    opp_visible_counts = Counter(opp_visible)
    opp_unseen = []
    for cid, count in starting_counts.items():
        unseen_count = max(0, count - opp_visible_counts.get(cid, 0))
        opp_unseen.extend([cid] * unseen_count)
    random.shuffle(opp_unseen)
    
    # Ensure a basic Pokémon is placed at the end of opp_unseen for opponent_active if face down
    opponent_active = []
    if opp.active and opp.active[0] is None:
        found_idx = -1
        for p_id in [722, 721]:
            if p_id in opp_unseen:
                found_idx = opp_unseen.index(p_id)
                break
        if found_idx != -1:
            val = opp_unseen.pop(found_idx)
            opp_unseen.append(val)
        else:
            opp_unseen.append(722)
            
    hand_cnt = opp.handCount
    prize_cnt = len(opp.prize)
    deck_cnt = opp.deckCount
    
    opponent_hand = opp_unseen[:hand_cnt]
    opponent_prize = opp_unseen[hand_cnt:hand_cnt + prize_cnt]
    opponent_deck = opp_unseen[hand_cnt + prize_cnt:hand_cnt + prize_cnt + deck_cnt]
    
    if opp.active and opp.active[0] is None:
        opponent_active = [opp_unseen[-1]]
        
    if len(opponent_hand) < hand_cnt:
        opponent_hand += [3] * (hand_cnt - len(opponent_hand))
    if len(opponent_prize) < prize_cnt:
        opponent_prize += [3] * (prize_cnt - len(opponent_prize))
    if len(opponent_deck) < deck_cnt:
        opponent_deck += [3] * (deck_cnt - len(opponent_deck))
        
    return (your_deck, your_prize, opponent_deck, opponent_prize, opponent_hand, opponent_active)

def evaluate_state(state, player_idx) -> float:
    if state is None:
        return -10000.0
    if state.result != -1:
        if state.result == player_idx:
            return 100000.0
        elif state.result == 2:  # Draw
            return 0.0
        else:
            return -100000.0
            
    me = state.players[player_idx]
    opp = state.players[1 - player_idx]
    
    score = 0.0
    
    # Prizes
    prizes_taken = 6 - len(me.prize)
    opp_prizes_taken = 6 - len(opp.prize)
    score += prizes_taken * 500.0
    score -= opp_prizes_taken * 500.0
    
    # Active
    if me.active and me.active[0]:
        act = me.active[0]
        score += act.hp
        score += len(act.energies) * 50.0
    else:
        score -= 2000.0
    if opp.active and opp.active[0]:
        act = opp.active[0]
        score -= act.hp
        score -= len(act.energies) * 50.0
    else:
        score += 2000.0
        
    # Bench
    for b in me.bench:
        score += b.hp * 0.5
        score += len(b.energies) * 25.0
    for b in opp.bench:
        score -= b.hp * 0.5
        score -= len(b.energies) * 25.0
        
    # Hand
    score += me.handCount * 10.0
    score -= opp.handCount * 10.0
    
    return score

def beam_search_agent(obs, starting_deck, N_determinizations=2, depth=2, width=3) -> list[int]:
    """Choose action index using PIMC Beam Search."""
    select_info = obs.select
    if select_info is None:
        return starting_deck
        
    options = select_info.option
    max_c = select_info.maxCount
    
    if len(options) <= 1:
        return list(range(len(options)))
    if max_c > 1:
        return list(range(min(max_c, len(options))))
        
    root_player_idx = obs.current.yourIndex
    accumulated_scores = [0.0] * len(options)
    
    for _ in range(N_determinizations):
        y_deck, y_prize, o_deck, o_prize, o_hand, o_active = determinize(obs, starting_deck)
        
        root_state = search_begin(
            obs,
            y_deck, y_prize,
            o_deck, o_prize, o_hand, o_active,
            manual_coin=False
        )
        if root_state is None:
            continue
            
        beam = [([], root_state, 0.0)]
        
        for d in range(depth):
            candidates = []
            for path, s_state, _ in beam:
                sel = s_state.observation.select
                if sel is None or s_state.observation.current.yourIndex != root_player_idx or s_state.observation.current.result != -1:
                    candidates.append((path, s_state, evaluate_state(s_state.observation.current, root_player_idx)))
                    continue
                
                for opt_idx in range(len(sel.option)):
                    try:
                        next_state = search_step(s_state.searchId, [opt_idx])
                        if next_state is not None:
                            new_path = path + [opt_idx]
                            score = evaluate_state(next_state.observation.current, root_player_idx)
                            candidates.append((new_path, next_state, score))
                    except Exception:
                        pass
            
            candidates.sort(key=lambda x: x[2], reverse=True)
            old_beam = beam
            beam = candidates[:width]
            
            # Release state IDs
            active_ids = {b[1].searchId for b in beam}
            for pb in old_beam:
                if pb[1].searchId not in active_ids and pb[1].searchId != root_state.searchId:
                    try: search_release(pb[1].searchId)
                    except Exception: pass
            for cand in candidates[width:]:
                if cand[1].searchId not in active_ids:
                    try: search_release(cand[1].searchId)
                    except Exception: pass
                    
        for path, _, score in beam:
            if path:
                accumulated_scores[path[0]] += score
                
        search_end()
        
    best_option = accumulated_scores.index(max(accumulated_scores))
    return [best_option]

# ==========================================
# SIMULATION WORKER PROCESS
# ==========================================
def worker_simulate_game(game_id: int) -> list[dict] | None:
    """Runs a single self-play simulation game.
    
    Returns:
        list[dict]: List of state dictionaries with their respective Z label,
                    or None if game failed or timed out.
    """
    # Initialize process-local seed
    random.seed(os.getpid() + int(time.time() * 1000) % 100000 + game_id)
    
    deck0 = read_deck()
    deck1 = read_deck()
    
    obs_dict, start_data = battle_start(deck0, deck1)
    if start_data.battlePtr is None or start_data.battlePtr == 0:
        return None
        
    obs = to_observation_class(obs_dict)
    
    game_history = [] # list of (featurized_state_dict, your_index)
    step = 0
    MAX_STEPS = 300 # Limit to discard looping/degenerate games
    
    try:
        while obs.current.result == -1:
            step += 1
            if step > MAX_STEPS:
                # Discard looping/degenerate games to preserve training quality
                battle_finish()
                return None
                
            # PIÈGE CRITIQUE 3 : Featuriser l'état RÉEL observé, pas l'état déterminisé
            tensors = featurize_state(obs.current)
            game_history.append((tensors, obs.current.yourIndex))
            
            # Beam search handles determinization internally
            action = beam_search_agent(obs, deck0, N_determinizations=2, depth=2, width=3)
            
            obs_dict = battle_select(action)
            obs = to_observation_class(obs_dict)
            
        result = obs.current.result # 0 or 1 (winner)
        battle_finish()
        
        # Game finished successfully! Reconstruct labels Z relative to the perspective of the decider
        # Z = +1 if the player at the trait at that step ends up winning, -1 otherwise.
        game_states = []
        for tensors, decider_idx in game_history:
            # PIÈGE CRITIQUE 1 : Calculer Z pour chaque état en fonction de decider_idx
            if result == decider_idx:
                z_val = 1.0
            elif result in (0, 1):
                z_val = -1.0
            else:
                z_val = 0.0 # Draw
                
            # Convert tensors to raw Python lists to bypass PyTorch Windows multiprocessing shared memory limit
            state_data = {
                "global_features": tensors["global_features"].tolist(),
                "tokens_card_id": tensors["tokens_card_id"].tolist(),
                "tokens_role": tensors["tokens_role"].tolist(),
                "tokens_features": tensors["tokens_features"].tolist(),
                "attention_mask": tensors["attention_mask"].tolist(),
                "Z": z_val,
                "game_id": game_id
            }
            game_states.append(state_data)
            
        return game_states
        
    except Exception as e:
        # Fallback cleanup in case of crash
        try:
            battle_finish()
        except Exception:
            pass
        return None

# ==========================================
# PARALLEL DATA COLLECTOR ENGINE
# ==========================================
def collect_selfplay_dataset(num_games=30, num_workers=4, output_file="selfplay_dataset.pt"):
    print("="*60)
    print(f" DÉMARRAGE DU COLLECTEUR SELF-PLAY (Workers: {num_workers}) ")
    print("="*60)
    
    start_time = time.perf_counter()
    
    # Run games in parallel, recycling workers to prevent memory/resource leaks
    pool = multiprocessing.Pool(processes=num_workers, maxtasksperchild=20)
    
    # We use map_async or imap_unordered to track progress
    results = pool.imap_unordered(worker_simulate_game, range(num_games))
    
    dataset = []
    completed_games = 0
    discarded_games = 0
    total_states = 0
    
    for res in results:
        if res is not None:
            # Convert the raw Python data back to PyTorch tensors in the main process
            for state_data in res:
                tensor_dict = {
                    "global_features": torch.tensor(state_data["global_features"], dtype=torch.float32),
                    "tokens_card_id": torch.tensor(state_data["tokens_card_id"], dtype=torch.long),
                    "tokens_role": torch.tensor(state_data["tokens_role"], dtype=torch.long),
                    "tokens_features": torch.tensor(state_data["tokens_features"], dtype=torch.float32),
                    "attention_mask": torch.tensor(state_data["attention_mask"], dtype=torch.float32),
                    "Z": torch.tensor([state_data["Z"]], dtype=torch.float32),
                    "game_id": torch.tensor([state_data["game_id"]], dtype=torch.long)
                }
                dataset.append(tensor_dict)
            completed_games += 1
            total_states += len(res)
        else:
            discarded_games += 1
            
        # Log progress periodically
        elapsed = time.perf_counter() - start_time
        print(f"  Progrès: {completed_games + discarded_games}/{num_games} parties traitées | "
              f"Enregistrées: {completed_games} | Jetées: {discarded_games} | Tenseurs: {total_states} | "
              f"Temps: {elapsed:.1f}s", end="\r", flush=True)
              
    pool.close()
    pool.join()
    
    total_time = time.perf_counter() - start_time
    
    # Save dataset to disk
    if dataset:
        torch.save(dataset, output_file)
        print(f"\n\nDataset sauvegardé avec succès dans: {output_file}")
    else:
        print("\n\nAucune donnée collectée.")
        return
        
    # Compile stats
    z_values = [t["Z"].item() for t in dataset]
    z_counts = Counter(z_values)
    
    games_per_hour = (completed_games / total_time) * 3600.0 if total_time > 0 else 0
    states_per_hour = (total_states / total_time) * 3600.0 if total_time > 0 else 0
    
    print("="*60)
    print(" STATISTIQUES DE COLLECTE SELF-PLAY ")
    print("="*60)
    print(f" Parties réussies : {completed_games} | Parties jetées : {discarded_games}")
    print(f" Nombre total d'états collectés : {total_states}")
    print(f" Distribution des labels Z (Perspective-relatifs) :")
    for z_val, cnt in sorted(z_counts.items()):
        percentage = (cnt / total_states) * 100.0
        print(f"   Z = {z_val:+.1f} : {cnt:5d} occurrences ({percentage:5.1f}%)")
    print(f" Débit mesuré :")
    print(f"   - {games_per_hour:.1f} parties / heure")
    print(f"   - {states_per_hour:.1f} états / heure")
    print(f" Temps total écoulé : {total_time:.1f} secondes")
    print("="*60)
    
    # Print sample to inspect
    print("\nÉchantillon de quelques états (Z et formes des tenseurs) :")
    sample_indices = random.sample(range(total_states), min(3, total_states))
    for idx in sample_indices:
        item = dataset[idx]
        print(f"  État #{idx:04d} :")
        print(f"    - Z : {item['Z'].item():+.1f}")
        print(f"    - global_features shape : {item['global_features'].shape}")
        print(f"    - tokens_card_id shape  : {item['tokens_card_id'].shape}")
        print(f"    - tokens_features shape : {item['tokens_features'].shape}")
    print("="*60)

if __name__ == "__main__":
    # Ensure Windows compatibility for multiprocessing
    multiprocessing.freeze_support()
    
    # Set default: generate 5000 games on 6 parallel workers for Lopunny deck
    collect_selfplay_dataset(num_games=5000, num_workers=6, output_file="selfplay_dataset_lopunny.pt")
