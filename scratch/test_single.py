import os
import sys
import random
import time
import torch

sys.path.append("sample_submission")
from cg.game import battle_start, battle_select, battle_finish
from cg.api import to_observation_class
import main
from main import (
    beam_search_agent,
    read_deck_csv,
    get_value_model,
    GLOBAL_DEVICE,
    evaluate_state_heuristic
)

# Patch with the hybrid evaluation model
def evaluate_state_neural_hybrid(state, root_player_idx, model, device) -> float:
    if state is None:
        return -2.0
    if state.result != -1:
        if state.result == root_player_idx:
            return 2.0
        elif state.result == 2:
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
        
    # Hybrid prize lead correction
    me = state.players[root_player_idx]
    opp = state.players[1 - root_player_idx]
    prize_diff = len(opp.prize) - len(me.prize)
    
    v = v + 0.15 * prize_diff
    v = max(-1.9, min(1.9, v))
    
    return v

main.evaluate_state_neural = evaluate_state_neural_hybrid

def run_single():
    main.ENABLE_LOGGING = True
    deck0 = read_deck_csv()
    deck1 = read_deck_csv()
    
    print("Starting single test game...")
    obs_dict, start_data = battle_start(deck0, deck1)
    if start_data.battlePtr is None or start_data.battlePtr == 0:
        print("Error starting battle.")
        return
        
    obs = to_observation_class(obs_dict)
    step = 0
    
    while obs.current.result == -1:
        step += 1
        print(f"\n--- STEP {step} ---")
        your_idx = obs.current.yourIndex
        
        # Neural vs Heuristic
        if your_idx == 0:
            action = main.agent(obs_dict)
        else:
            action = beam_search_agent(
                obs_dict, 
                starting_deck=deck1, 
                N_determinizations=4, 
                depth_turns=2, 
                width=3, 
                evaluation_mode="heuristic"
            )
            
        obs_dict = battle_select(action)
        obs = to_observation_class(obs_dict)
        
    print(f"Game finished in {step} steps. Winner: {obs.current.result}")
    battle_finish()

if __name__ == "__main__":
    run_single()
