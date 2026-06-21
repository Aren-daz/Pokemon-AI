import os
import sys
import random
import time
import torch
import multiprocessing

sys.path.append("sample_submission")
from cg.game import battle_start, battle_select, battle_finish
from cg.api import to_observation_class, SelectContext, OptionType
import main
from main import (
    beam_search_agent,
    read_deck_csv,
    get_b3_records,
    get_value_model,
    GLOBAL_DEVICE,
    evaluate_state_heuristic
)

# ----------------------------------------------------
# PATCH MAIN.PY TEMPORARILY IN MEMORY FOR THIS TEST
# ----------------------------------------------------
def evaluate_state_neural_fixed(state, root_player_idx, model, device) -> float:
    if state is None:
        return -2.0
    if state.result != -1:
        if state.result == root_player_idx:
            return 2.0
        elif state.result == 2:  # Draw
            return 0.0
        else:
            return -2.0
            
    from featurizer import featurize_state
    feat = featurize_state(state)
    
    gf = feat["global_features"].unsqueeze(0).to(device)
    t_cid = feat["tokens_card_id"].unsqueeze(0).to(device)
    t_role = feat["tokens_role"].unsqueeze(0).to(device)
    t_feat = feat["tokens_features"].unsqueeze(0).to(device)
    mask = feat["attention_mask"].unsqueeze(0).to(device)
    
    with torch.no_grad():
        v = model(gf, t_cid, t_role, t_feat, mask).item()
        
    if state.yourIndex != root_player_idx:
        v = -v
        
    # Hybrid prize correction (0.15 per prize lead)
    me = state.players[root_player_idx]
    opp = state.players[1 - root_player_idx]
    prize_diff = len(opp.prize) - len(me.prize)
    
    v = v + 0.15 * prize_diff
    v = max(-1.9, min(1.9, v))
    
    return v

def evaluate_state_generic_fixed(state, root_player_idx, evaluation_mode="neural") -> float:
    if evaluation_mode == "neural":
        model = get_value_model()
        return evaluate_state_neural_fixed(state, root_player_idx, model, GLOBAL_DEVICE)
    else:
        return evaluate_state_heuristic(state, root_player_idx)

# Apply patches to the imported main module
main.evaluate_state_neural = evaluate_state_neural_fixed
main.evaluate_state_generic = evaluate_state_generic_fixed

# ----------------------------------------------------
# RUNNER FOR TEST GAME
# ----------------------------------------------------
def run_test_game(args):
    torch.set_num_threads(1)
    game_id, p1_neural = args
    deck0 = read_deck_csv()
    deck1 = read_deck_csv()
    
    main.ENABLE_LOGGING = False
    _ = get_b3_records()
    
    try:
        obs_dict, start_data = battle_start(deck0, deck1)
        if start_data.battlePtr is None or start_data.battlePtr == 0:
            return {"winner": -1, "neural_won": False, "error": True, "b3_records": []}
            
        obs = to_observation_class(obs_dict)
        step = 0
        
        while obs.current.result == -1:
            step += 1
            your_idx = obs.current.yourIndex
            
            if your_idx == 0:
                mode = "neural" if p1_neural else "heuristic"
                active_deck = deck0
            else:
                mode = "heuristic" if p1_neural else "neural"
                active_deck = deck1
                
            action = beam_search_agent(
                obs_dict, 
                starting_deck=active_deck, 
                N_determinizations=4, 
                depth_turns=2, 
                width=3, 
                evaluation_mode=mode
            )
            obs_dict = battle_select(action)
            obs = to_observation_class(obs_dict)
            
        winner = obs.current.result
        battle_finish()
        
        neural_won = False
        if winner == 0:
            neural_won = p1_neural
        elif winner == 1:
            neural_won = not p1_neural
            
        b3_records = get_b3_records()
        
        return {
            "winner": winner,
            "neural_won": neural_won,
            "error": False,
            "b3_records": b3_records
        }
    except Exception as e:
        try:
            battle_finish()
        except Exception:
            pass
        return {"winner": -1, "neural_won": False, "error": True, "b3_records": [], "error_msg": str(e)}

def main_test():
    random.seed(1337)
    torch.manual_seed(1337)
    
    print("="*60)
    print(" DÉMARRAGE DU TEST DE FIX DE PERSPECTIVE (20 PARTIES) ")
    print("="*60)
    
    args_list = []
    for i in range(10):
        args_list.append((i, True))
    for i in range(10):
        args_list.append((10 + i, False))
        
    random.shuffle(args_list)
    
    num_workers = min(multiprocessing.cpu_count(), 6)
    print(f"Workers: {num_workers}")
    
    completed = 0
    neural_wins = 0
    heuristic_wins = 0
    errors = 0
    b3_all_records = []
    
    with multiprocessing.Pool(processes=num_workers) as pool:
        for res in pool.imap_unordered(run_test_game, args_list):
            completed += 1
            if res["error"]:
                errors += 1
            elif res["neural_won"]:
                neural_wins += 1
            else:
                heuristic_wins += 1
                
            b3_all_records.extend(res["b3_records"])
            print(f"  Parties : {completed}/20 completed | Wins Neural: {neural_wins} | Wins Heur: {heuristic_wins}")
            
    print("\n" + "="*50)
    print(" RÉSULTATS DU TEST DE FIX ")
    print("="*50)
    winrate = (neural_wins / completed * 100.0) if completed > 0 else 0.0
    print(f"Winrate Neural Agent : {winrate:.2f}% ({neural_wins}/{completed})")
    
    # B3 records
    danger_counts = {"high_danger": 0, "low_danger": 0, "medium_danger": 0}
    static_retreats = {"high_danger": 0, "low_danger": 0, "medium_danger": 0}
    search_retreats = {"high_danger": 0, "low_danger": 0, "medium_danger": 0}
    
    for r in b3_all_records:
        ctx = r["danger_context"]
        danger_counts[ctx] += 1
        if r["static_choice_is_retreat"]:
            static_retreats[ctx] += 1
        if r["search_choice_is_retreat"]:
            search_retreats[ctx] += 1
            
    print("\nCompensation contextuelle B3 :")
    for ctx in ["high_danger", "low_danger"]:
        n = danger_counts[ctx]
        s_pct = (static_retreats[ctx] / n * 100.0) if n > 0 else 0.0
        r_pct = (search_retreats[ctx] / n * 100.0) if n > 0 else 0.0
        print(f"  - {ctx.upper()} (N={n}) : Statique={s_pct:.2f}% | Recherche={r_pct:.2f}% (Diff: {r_pct - s_pct:+.2f}%)")
    print("="*50)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main_test()
