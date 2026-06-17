import sys
import os
import random
import time
from collections import Counter

from cg.api import (
    Observation,
    to_observation_class,
    OptionType,
    SelectContext,
    SelectType,
    all_card_data,
    all_attack,
    search_begin,
    search_step,
    search_end,
    search_release,
    EnergyType
)
from cg.game import battle_start, battle_select, battle_finish

# Global Card names cache for printing logs
CARDS_CACHE = {}

def initialize_caches():
    global CARDS_CACHE
    if not CARDS_CACHE:
        try:
            CARDS_CACHE = {c.cardId: c.name for c in all_card_data()}
        except Exception:
            pass

def read_deck(file_path="deck.csv") -> list[int]:
    if not os.path.exists(file_path):
        file_path = "/kaggle_simulations/agent/" + file_path
    with open(file_path, "r") as file:
        csv = file.read().split("\n")
    deck = []
    for i in range(60):
        deck.append(int(csv[i]))
    return deck

# ==========================================
# 1. FEATURIZER MINIMAL
# ==========================================
def minimal_featurize(obs: Observation) -> dict:
    """Extract a minimal set of board features from the Observation dataclass."""
    state = obs.current
    if not state:
        return {}
        
    your_idx = state.yourIndex
    opp_idx = 1 - your_idx
    
    me = state.players[your_idx]
    opp = state.players[opp_idx]
    
    features = {
        "turn": state.turn,
        "energy_attached": int(state.energyAttached),
        "supporter_played": int(state.stadiumPlayed),
        "my_hand_count": me.handCount,
        "opp_hand_count": opp.handCount,
        "my_deck_count": me.deckCount,
        "opp_deck_count": opp.deckCount,
        "my_prizes_count": len(me.prize),
        "opp_prizes_count": len(opp.prize),
        "my_bench_count": len(me.bench),
        "opp_bench_count": len(opp.bench),
    }
    
    # Active HP
    features["my_active_hp"] = me.active[0].hp if (me.active and me.active[0]) else 0
    features["opp_active_hp"] = opp.active[0].hp if (opp.active and opp.active[0]) else 0
    
    # Hand card list IDs
    features["hand_ids"] = [c.id for c in me.hand] if me.hand else []
    
    return features

# ==========================================
# 2. DÉTERMINISATION PRÉCISE
# ==========================================
def get_visible_card_ids(state, target_player_idx):
    """Gathers all visible card IDs owned by target_player_idx."""
    visible = []
    
    def add_card(c):
        if c and c.playerIndex == target_player_idx:
            visible.append(c.id)
            
    for p_idx in [0, 1]:
        p_state = state.players[p_idx]
        # Active
        if p_state.active and p_state.active[0]:
            act = p_state.active[0]
            if p_idx == target_player_idx:
                visible.append(act.id)
            for c in act.preEvolution: add_card(c)
            for c in act.energyCards: add_card(c)
            for c in act.tools: add_card(c)
            
        # Bench
        for b in p_state.bench:
            if p_idx == target_player_idx:
                visible.append(b.id)
            for c in b.preEvolution: add_card(c)
            for c in b.energyCards: add_card(c)
            for c in b.tools: add_card(c)
            
        # Discard
        for c in p_state.discard:
            add_card(c)
            
        # Hand (only visible for me, i.e., target_player_idx == yourIndex)
        if p_state.hand:
            for c in p_state.hand:
                add_card(c)
                
    if state.stadium:
        add_card(state.stadium[0])
        
    if state.looking:
        for c in state.looking:
            add_card(c)
            
    return visible

def determinize(obs: Observation, starting_deck: list[int]) -> tuple:
    """Generate determinization predictions for search_begin.
    
    Returns:
        tuple: (your_deck, your_prize, opponent_deck, opponent_prize, opponent_hand, opponent_active)
    """
    state = obs.current
    your_idx = state.yourIndex
    opp_idx = 1 - your_idx
    
    me = state.players[your_idx]
    opp = state.players[opp_idx]
    
    # Count of each card ID in the starting deck
    starting_counts = Counter(starting_deck)
    
    # 1. Determinize our own deck & prizes
    my_visible = get_visible_card_ids(state, your_idx)
    my_visible_counts = Counter(my_visible)
    
    my_unseen = []
    for cid, count in starting_counts.items():
        unseen_count = max(0, count - my_visible_counts.get(cid, 0))
        my_unseen.extend([cid] * unseen_count)
        
    random.shuffle(my_unseen)
    
    # Split my_unseen into deck and prize matching the game counts
    your_deck = my_unseen[:me.deckCount]
    your_prize = my_unseen[me.deckCount:me.deckCount + len(me.prize)]
    
    # Fill up with default water energy (ID 3) if there's any count mismatch
    if len(your_deck) < me.deckCount:
        your_deck += [3] * (me.deckCount - len(your_deck))
    if len(your_prize) < len(me.prize):
        your_prize += [3] * (len(me.prize) - len(your_prize))
        
    # 2. Determinize opponent's deck, prize, hand
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
            
    # Opponent distribution counts
    hand_cnt = opp.handCount
    prize_cnt = len(opp.prize)
    deck_cnt = opp.deckCount
    
    # Slice cards matching exact counts
    opponent_hand = opp_unseen[:hand_cnt]
    opponent_prize = opp_unseen[hand_cnt:hand_cnt + prize_cnt]
    opponent_deck = opp_unseen[hand_cnt + prize_cnt:hand_cnt + prize_cnt + deck_cnt]
    
    if opp.active and opp.active[0] is None:
        opponent_active = [opp_unseen[-1]]
        
    # Fallback padding to guarantee exact size
    if len(opponent_hand) < hand_cnt:
        opponent_hand += [3] * (hand_cnt - len(opponent_hand))
    if len(opponent_prize) < prize_cnt:
        opponent_prize += [3] * (prize_cnt - len(opponent_prize))
    if len(opponent_deck) < deck_cnt:
        opponent_deck += [3] * (deck_cnt - len(opponent_deck))
        
    return (your_deck, your_prize, opponent_deck, opponent_prize, opponent_hand, opponent_active)

# ==========================================
# 3. VALUATION / HEURISTIQUE BIDON
# ==========================================
def evaluate_state(state, player_idx) -> float:
    """Calculates a heuristic score from the perspective of player_idx."""
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
    
    # Prizes taken
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
        
    # Hand cards
    score += me.handCount * 10.0
    score -= opp.handCount * 10.0
    
    return score

# ==========================================
# 4. PIMC BEAM SEARCH AGENT
# ==========================================
def beam_search_agent(obs_dict: dict, starting_deck: list[int], N_determinizations: int, depth=2, width=3) -> list[int]:
    obs = to_observation_class(obs_dict)
    if obs.select is None:
        return starting_deck
        
    select_info = obs.select
    options = select_info.option
    max_c = select_info.maxCount
    
    # If only one choice is possible, return it immediately
    if len(options) <= 1:
        return list(range(len(options)))
        
    # If we need to select multiple items, do a greedy fallback
    if max_c > 1:
        return list(range(min(max_c, len(options))))
        
    root_player_idx = obs.current.yourIndex
    accumulated_scores = [0.0] * len(options)
    
    for _ in range(N_determinizations):
        # 1. Determinize
        y_deck, y_prize, o_deck, o_prize, o_hand, o_active = determinize(obs, starting_deck)
        
        # 2. Begin Search Session
        root_state = search_begin(
            obs,
            y_deck, y_prize,
            o_deck, o_prize, o_hand, o_active,
            manual_coin=False
        )
        
        if root_state is None:
            continue
            
        # Beam entry structure: (path: list, current_search_state: SearchState, score: float)
        beam = [([], root_state, 0.0)]
        
        for d in range(depth):
            candidates = []
            
            for path, s_state, _ in beam:
                sel = s_state.observation.select
                # If turn has ended or game is finished, we don't expand further
                if sel is None or s_state.observation.current.yourIndex != root_player_idx or s_state.observation.current.result != -1:
                    candidates.append((path, s_state, evaluate_state(s_state.observation.current, root_player_idx)))
                    continue
                
                # Expand options
                for opt_idx in range(len(sel.option)):
                    # Sim step
                    try:
                        next_state = search_step(s_state.searchId, [opt_idx])
                        if next_state is not None:
                            new_path = path + [opt_idx]
                            score = evaluate_state(next_state.observation.current, root_player_idx)
                            candidates.append((new_path, next_state, score))
                    except Exception:
                        pass
            
            # Sort candidates by score descending
            candidates.sort(key=lambda x: x[2], reverse=True)
            
            # Keep top W paths
            old_beam = beam
            beam = candidates[:width]
            
            # Release state IDs that are NOT in the new beam to prevent memory leaks
            active_ids = {b[1].searchId for b in beam}
            for pb in old_beam:
                if pb[1].searchId not in active_ids and pb[1].searchId != root_state.searchId:
                    try:
                        search_release(pb[1].searchId)
                    except Exception:
                        pass
            for cand in candidates[width:]:
                if cand[1].searchId not in active_ids:
                    try:
                        search_release(cand[1].searchId)
                    except Exception:
                        pass
                        
        # After completing the search for this determinization, sum up scores for the root actions
        for path, _, score in beam:
            if path:
                root_action = path[0]
                accumulated_scores[root_action] += score
                
        # Clean up search session
        search_end()
        
    # Choose best root option
    best_option = accumulated_scores.index(max(accumulated_scores))
    return [best_option]

# ==========================================
# 5. TEST DE SIMULATION ET MESURE (SPIKE)
# ==========================================
def run_spike_benchmark():
    initialize_caches()
    deck0 = read_deck()
    deck1 = read_deck()
    
    print("="*60)
    print(" DEMARRAGE DU SPIKE DE MESURE KAGGLE BUDGET ")
    print("="*60)
    
    # We will run a game, switching the N parameter every few turns
    # to measure the exact average decision times.
    obs_dict, start_data = battle_start(deck0, deck1)
    if start_data.battlePtr is None or start_data.battlePtr == 0:
        print("Erreur au démarrage du combat.")
        return
        
    obs = to_observation_class(obs_dict)
    step = 0
    
    # Trackers for times
    times_by_n = {1: [], 4: [], 8: []}
    
    while obs.current.result == -1:
        step += 1
        
        # Decide which N to test (alternate N=1, N=4, N=8)
        if step % 3 == 1:
            N = 1
        elif step % 3 == 2:
            N = 4
        else:
            N = 8
            
        # Time the decision
        start_time = time.perf_counter()
        action = beam_search_agent(obs_dict, deck0, N_determinizations=N, depth=2, width=3)
        end_time = time.perf_counter()
        
        elapsed_ms = (end_time - start_time) * 1000.0
        times_by_n[N].append(elapsed_ms)
        
        # Run Minimal Featurizer check
        feats = minimal_featurize(obs)
        
        # Log progress
        select_info = obs.select
        context_name = SelectContext(select_info.context).name if (select_info and select_info.context) else "Initial"
        print(f"Step {step:02d} | N={N} | Context: {context_name:<20} | Time: {elapsed_ms:6.2f} ms | Feats keys: {list(feats.keys())[:5]}")
        
        # Apply action
        obs_dict = battle_select(action)
        obs = to_observation_class(obs_dict)
        
    battle_finish()
    
    print("\n" + "="*60)
    print(" RESULTATS DE MESURE DU BUDGET DE DECISION ")
    print("="*60)
    for N, times in times_by_n.items():
        if times:
            avg_time = sum(times) / len(times)
            max_time = max(times)
            print(f" N = {N} déterminisations :")
            print(f"   - Temps moyen : {avg_time:.2f} ms")
            print(f"   - Temps max   : {max_time:.2f} ms")
            print(f"   - Nb mesures  : {len(times)}")
        else:
            print(f" N = {N} : pas de mesures.")
    print("="*60)

if __name__ == "__main__":
    run_spike_benchmark()
