import os
import sys
import random
import time
import torch
import multiprocessing
from collections import Counter

project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

from cg.api import to_observation_class, search_begin, search_step, search_end, search_release
from cg.game import battle_start, battle_select, battle_finish
from featurizer import featurize_state

GLOBAL_MODEL = None
GLOBAL_DEVICE = torch.device("cpu")

def read_deck(file_path="deck.csv") -> list[int]:
    if not os.path.exists(file_path):
        file_path = os.path.join(project_dir, file_path)
    if not os.path.exists(file_path):
        file_path = "/kaggle_simulations/agent/deck.csv"
    with open(file_path, "r") as file:
        csv = file.read().split("\n")
    deck = []
    for i in range(60):
        deck.append(int(csv[i]))
    return deck

def get_value_model():
    global GLOBAL_MODEL
    if GLOBAL_MODEL is None:
        from model import ValueNetwork
        GLOBAL_MODEL = ValueNetwork().to(GLOBAL_DEVICE)
        model_path = os.path.join(project_dir, "value_network_lopunny_weighted_best.pth")
        if not os.path.exists(model_path):
            model_path = "/kaggle_simulations/agent/value_network_lopunny_weighted_best.pth"
        GLOBAL_MODEL.load_state_dict(torch.load(model_path, map_location="cpu"))
        GLOBAL_MODEL.eval()
        torch.set_num_threads(1) # Crucial for parallel subprocesses
    return GLOBAL_MODEL

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
        
    opp_visible = get_visible_card_ids(state, opp_idx)
    opp_visible_counts = Counter(opp_visible)
    opp_unseen = []
    for cid, count in starting_counts.items():
        unseen_count = max(0, count - opp_visible_counts.get(cid, 0))
        opp_unseen.extend([cid] * unseen_count)
    random.shuffle(opp_unseen)
    
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

def evaluate_states_neural_batch(states, root_player_idx, model, device) -> list[float]:
    if not states:
        return []
        
    scores = [0.0] * len(states)
    non_terminal_indices = []
    feats = []
    
    for idx, s in enumerate(states):
        if s is None:
            scores[idx] = -2.0
        elif s.result != -1:
            if s.result == root_player_idx:
                scores[idx] = 2.0
            elif s.result == 2:
                scores[idx] = 0.0
            else:
                scores[idx] = -2.0
        else:
            non_terminal_indices.append(idx)
            feats.append(featurize_state(s))
            
    if not feats:
        return scores
        
    max_L = max(f["tokens_card_id"].shape[0] for f in feats)
    
    gf_list = []
    t_cid_list = []
    t_role_list = []
    t_feat_list = []
    mask_list = []
    
    for f in feats:
        L = f["tokens_card_id"].shape[0]
        padding_needed = max_L - L
        
        gf_list.append(f["global_features"])
        
        if padding_needed > 0:
            t_cid_list.append(torch.cat([f["tokens_card_id"], torch.zeros(padding_needed, dtype=torch.long)]))
            t_role_list.append(torch.cat([f["tokens_role"], torch.zeros(padding_needed, dtype=torch.long)]))
            t_feat_list.append(torch.cat([f["tokens_features"], torch.zeros(padding_needed, 18, dtype=torch.float32)], dim=0))
            mask_list.append(torch.cat([f["attention_mask"], torch.zeros(padding_needed, dtype=torch.float32)]))
        else:
            t_cid_list.append(f["tokens_card_id"])
            t_role_list.append(f["tokens_role"])
            t_feat_list.append(f["tokens_features"])
            mask_list.append(f["attention_mask"])
            
    gf = torch.stack(gf_list).to(device)
    t_cid = torch.stack(t_cid_list).to(device)
    t_role = torch.stack(t_role_list).to(device)
    t_feat = torch.stack(t_feat_list).to(device)
    mask = torch.stack(mask_list).to(device)
    
    with torch.no_grad():
        v_batch = model(gf, t_cid, t_role, t_feat, mask)
        v_list = v_batch.squeeze(-1).tolist() if v_batch.dim() > 1 else v_batch.tolist()
        if not isinstance(v_list, list):
            v_list = [v_list]
            
    for list_idx, original_idx in enumerate(non_terminal_indices):
        s = states[original_idx]
        v = v_list[list_idx]
        if s.yourIndex != root_player_idx:
            v = -v
        scores[original_idx] = v
        
    return scores

def beam_search_agent_batch(obs, starting_deck, N_determinizations=4, depth_turns=2, width=3) -> list[int]:
    select_info = obs.select
    if select_info is None:
        return starting_deck
    options = select_info.option
    
    if len(options) <= 1:
        return list(range(len(options)))
    if select_info.maxCount > 1:
        return list(range(min(select_info.maxCount, len(options))))
        
    root_player_idx = obs.current.yourIndex
    accumulated_scores = [0.0] * len(options)
    
    model = get_value_model()
    device = GLOBAL_DEVICE
    
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
            
        beam = [([], root_state, 0, root_player_idx, 0.0)]
        max_plies = 25
        
        for ply_idx in range(max_plies):
            all_done = True
            for path, s_state, transitions, prev_player, _ in beam:
                sel = s_state.observation.select
                if sel is not None and transitions < 2 and s_state.observation.current.result == -1:
                    all_done = False
                    break
            if all_done:
                break
                
            to_evaluate_states = []
            to_evaluate_metadata = []
            candidates = []
            
            for path_idx, (path, s_state, transitions, prev_player, current_score) in enumerate(beam):
                sel = s_state.observation.select
                if sel is None or transitions >= 2 or s_state.observation.current.result != -1:
                    candidates.append((path, s_state, transitions, prev_player, current_score))
                    continue
                    
                current_player = s_state.observation.current.yourIndex
                next_transitions = transitions
                if current_player != prev_player:
                    next_transitions += 1
                    
                if next_transitions >= 2:
                    to_evaluate_states.append(s_state.observation.current)
                    to_evaluate_metadata.append((path, s_state, next_transitions, current_player, path_idx, -1))
                    continue
                    
                if current_player == root_player_idx:
                    # MAX Node
                    if sel.maxCount > 1 or sel.minCount > 1:
                        num_to_select = sel.maxCount if sel.maxCount > 0 else sel.minCount
                        num_to_select = min(num_to_select, len(sel.option))
                        selection = list(range(num_to_select))
                        try:
                            next_state = search_step(s_state.searchId, selection)
                            if next_state is not None:
                                to_evaluate_states.append(next_state.observation.current)
                                to_evaluate_metadata.append((path + [0], next_state, next_transitions, current_player, path_idx, -1))
                        except Exception:
                            pass
                    else:
                        for opt_idx in range(len(sel.option)):
                            try:
                                next_state = search_step(s_state.searchId, [opt_idx])
                                if next_state is not None:
                                    to_evaluate_states.append(next_state.observation.current)
                                    to_evaluate_metadata.append((path + [opt_idx], next_state, next_transitions, current_player, path_idx, opt_idx))
                            except Exception:
                                pass
                else:
                    # MIN Node
                    if sel.maxCount > 1 or sel.minCount > 1:
                        num_to_select = sel.maxCount if sel.maxCount > 0 else sel.minCount
                        num_to_select = min(num_to_select, len(sel.option))
                        selection = list(range(num_to_select))
                        try:
                            next_state = search_step(s_state.searchId, selection)
                            if next_state is not None:
                                to_evaluate_states.append(next_state.observation.current)
                                to_evaluate_metadata.append((path + [0], next_state, next_transitions, current_player, path_idx, -1))
                        except Exception:
                            pass
                    else:
                        for opt_idx in range(len(sel.option)):
                            try:
                                next_state = search_step(s_state.searchId, [opt_idx])
                                if next_state is not None:
                                    to_evaluate_states.append(next_state.observation.current)
                                    to_evaluate_metadata.append((path + [opt_idx], next_state, next_transitions, current_player, path_idx, opt_idx))
                            except Exception:
                                pass
                                
            scores = evaluate_states_neural_batch(to_evaluate_states, root_player_idx, model, device)
            
            opp_groups = {}
            for idx, score in enumerate(scores):
                path, next_state, next_transitions, current_player, path_idx, opt_idx = to_evaluate_metadata[idx]
                is_opp_single = (current_player != root_player_idx) and (opt_idx != -1)
                
                if is_opp_single:
                    if path_idx not in opp_groups:
                        opp_groups[path_idx] = []
                    opp_groups[path_idx].append((score, next_state, path, next_transitions, current_player))
                else:
                    candidates.append((path, next_state, next_transitions, current_player, score))
                    
            for path_idx, choices in opp_groups.items():
                choices.sort(key=lambda x: x[0])
                best_choice = choices[0]
                candidates.append((best_choice[2], best_choice[1], best_choice[3], best_choice[4], best_choice[0]))
                for choice in choices[1:]:
                    try: search_release(choice[1].searchId)
                    except Exception: pass
                        
            candidates.sort(key=lambda x: x[4], reverse=True)
            old_beam = beam
            beam = candidates[:width]
            
            active_ids = {b[1].searchId for b in beam}
            for pb in old_beam:
                if pb[1].searchId not in active_ids and pb[1].searchId != root_state.searchId:
                    try: search_release(pb[1].searchId)
                    except Exception: pass
            for cand in candidates[width:]:
                if cand[1].searchId not in active_ids:
                    try: search_release(cand[1].searchId)
                    except Exception: pass
                    
        for path, _, _, _, score in beam:
            if path:
                root_action = path[0]
                accumulated_scores[root_action] += score
                
        search_end()
        
    best_option = accumulated_scores.index(max(accumulated_scores))
    return [best_option]

# ==========================================
# SIMULATION WORKER PROCESS
# ==========================================
def worker_simulate_game(game_id: int) -> list[dict] | None:
    random.seed(os.getpid() + int(time.time() * 1000) % 100000 + game_id)
    
    deck0 = read_deck()
    deck1 = read_deck()
    
    obs_dict, start_data = battle_start(deck0, deck1)
    if start_data.battlePtr is None or start_data.battlePtr == 0:
        return None
        
    obs = to_observation_class(obs_dict)
    game_history = []
    step = 0
    MAX_STEPS = 300
    
    try:
        while obs.current.result == -1:
            step += 1
            if step > MAX_STEPS:
                battle_finish()
                return None
                
            tensors = featurize_state(obs.current)
            game_history.append((tensors, obs.current.yourIndex))
            
            action = beam_search_agent_batch(obs, deck0, N_determinizations=4, depth_turns=2, width=3)
            obs_dict = battle_select(action)
            obs = to_observation_class(obs_dict)
            
        result = obs.current.result
        battle_finish()
        
        game_states = []
        for tensors, decider_idx in game_history:
            if result == decider_idx:
                z_val = 1.0
            elif result in (0, 1):
                z_val = -1.0
            else:
                z_val = 0.0
                
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
        
    except Exception:
        try: battle_finish()
        except Exception: pass
        return None

# ==========================================
# PARALLEL DATA COLLECTOR ENGINE
# ==========================================
def collect_selfplay_dataset(num_games=1000, num_workers=6, output_file="selfplay_dataset_lopunny_gen2.pt"):
    print("="*60)
    print(f" DEMARRAGE DU COLLECTEUR SELF-PLAY GEN 2 (Workers: {num_workers}) ")
    print(f" Volume cible : {num_games} parties en N_det=4 ")
    print("="*60)
    
    start_time = time.perf_counter()
    
    pool = multiprocessing.Pool(processes=num_workers, maxtasksperchild=10)
    results = pool.imap_unordered(worker_simulate_game, range(num_games))
    
    dataset = []
    completed_games = 0
    discarded_games = 0
    total_states = 0
    
    for res in results:
        if res is not None:
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
            
        elapsed = time.perf_counter() - start_time
        print(f"  Progres: {completed_games + discarded_games}/{num_games} | "
              f"Enregistrees: {completed_games} | Jetees: {discarded_games} | Tenseurs: {total_states} | "
              f"Temps: {elapsed:.1f}s", end="\r", flush=True)
              
    pool.close()
    pool.join()
    
    total_time = time.perf_counter() - start_time
    
    if dataset:
        torch.save(dataset, output_file)
        print(f"\n\nDataset Gen 2 sauvegarde avec succes dans: {output_file}")
        print(f"Temps total de calcul : {total_time/60.0:.2f} minutes")
    else:
        print("\n\nAucune donnee collectee.")
        
if __name__ == "__main__":
    multiprocessing.freeze_support()
    collect_selfplay_dataset(num_games=1000, num_workers=6, output_file="selfplay_dataset_lopunny_gen2.pt")
