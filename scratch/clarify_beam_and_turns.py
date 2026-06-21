import os
import sys
sys.path.append("sample_submission")
import torch
from torch.utils.data import DataLoader
import numpy as np
import random
import time
from model import ValueNetwork
from evaluate_lopunny import collate_fn

def benchmark_inference(model, device, num_passes=500):
    print("Benchmarking model inference on CPU (batch=1)...")
    # Average token length is around 35 based on featurizer statistics
    L = 35
    gf = torch.randn(1, 22).to(device)
    t_cid = torch.randint(1, 1300, (1, L)).to(device)
    t_role = torch.randint(1, 10, (1, L)).to(device)
    t_feat = torch.randn(1, L, 18).to(device)
    mask = torch.ones(1, L).to(device)
    
    # Warmup
    for _ in range(50):
        _ = model(gf, t_cid, t_role, t_feat, mask)
        
    start_time = time.perf_counter()
    for _ in range(num_passes):
        _ = model(gf, t_cid, t_role, t_feat, mask)
    end_time = time.perf_counter()
    
    avg_latency = (end_time - start_time) / num_passes
    print(f"  Avg inference latency: {avg_latency*1000:.3f} ms")
    return avg_latency

def main():
    torch.manual_seed(42)
    np.random.seed(42)
    random.seed(42)
    
    device = torch.device("cpu") # Benchmark strictly on CPU
    torch.set_num_threads(8)
    
    dataset_path = "selfplay_dataset_lopunny.pt"
    if not os.path.exists(dataset_path):
        dataset_path = os.path.join("sample_submission", dataset_path)
    
    print("Loading dataset...")
    dataset = torch.load(dataset_path)
    
    # Load Model B
    model_path = "sample_submission/value_network_lopunny_weighted_best.pth"
    model = ValueNetwork().to(device)
    model.load_state_dict(torch.load(model_path, map_location="cpu"))
    model.eval()
    
    # ----------------------------------------------------
    # CLARIFICATION 2 : PLIES PER TURN ANALYSIS
    # ----------------------------------------------------
    print("\n" + "="*50)
    print(" CLARIFICATION 2 : LONGUEUR REELLE DES TOURS EN PLIES ")
    print("="*50)
    
    # Group states by game_id and turn number
    game_turns = {}
    for item in dataset:
        gid = int(item["game_id"])
        gf = item["global_features"]
        turn = int(round(gf[0].item() * 50.0))
        action_cnt = int(round(gf[1].item() * 10.0))
        
        if gid not in game_turns:
            game_turns[gid] = {}
        if turn not in game_turns[gid]:
            game_turns[gid][turn] = []
        game_turns[gid][turn].append(action_cnt)
        
    # For each turn in each game, the length (number of plies) is the max action count reached
    turn_lengths = []
    for gid in game_turns:
        for turn in game_turns[gid]:
            max_actions = max(game_turns[gid][turn])
            # The number of states recorded in a turn represents the number of decision plies
            turn_lengths.append(max_actions)
            
    avg_plies = np.mean(turn_lengths)
    median_plies = np.median(turn_lengths)
    max_plies = np.max(turn_lengths)
    p95_plies = np.percentile(turn_lengths, 95)
    
    print(f"Statistiques sur les plies par tour (sur {len(turn_lengths)} tours) :")
    print(f"  - Moyenne : {avg_plies:.2f} plies par tour")
    print(f"  - Médiane : {median_plies:.1f} plies par tour")
    print(f"  - 95ème centile : {p95_plies:.1f} plies par tour")
    print(f"  - Maximum : {max_plies} plies par tour")
    
    # Benchmark CPU latency
    avg_inference_latency = benchmark_inference(model, device)
    
    # Recalculate time budget for "profondeur 2 tours complets"
    # A full turn average is around avg_plies.
    # Plies in 2 turns = 2 * avg_plies.
    # Total search steps = N_det * plies_2_turns * beam_width
    plies_2_turns_avg = 2 * avg_plies
    plies_2_turns_max = 2 * p95_plies
    
    steps_avg = 4 * plies_2_turns_avg * 3 # N_det=4, beam=3
    steps_max = 4 * plies_2_turns_max * 3
    
    time_avg = steps_avg * avg_inference_latency
    time_max = steps_max * avg_inference_latency
    
    print(f"\nRecalcul du budget temps pour Profondeur = 2 tours complets (N_det=4, Beam=3) :")
    print(f"  - Cas moyen  ({plies_2_turns_avg:.1f} plies) : {steps_avg:.0f} évaluations -> {time_avg:.3f} s CPU")
    print(f"  - Cas max 95% ({plies_2_turns_max:.1f} plies) : {steps_max:.0f} évaluations -> {time_max:.3f} s CPU")
    
    # ----------------------------------------------------
    # CLARIFICATION 1 : MYOPIE DU BEAM SUR LE SETUP
    # ----------------------------------------------------
    print("\n" + "="*50)
    print(" CLARIFICATION 1 : MYOPIE DU BEAM SUR LE SETUP ")
    print("="*50)
    
    # We want to check if the network values resource setup actions (more cards in hand, benched setup).
    # Let's inspect states before and after playing search/draw cards.
    # Let's reconstruct sequential games.
    game_histories = {}
    for item in dataset:
        gid = int(item["game_id"])
        if gid not in game_histories:
            game_histories[gid] = []
        game_histories[gid].append(item)
        
    # We sort each game history chronologically
    for gid in game_histories:
        game_histories[gid].sort(key=lambda s: (round(s["global_features"][0].item() * 50.0), round(s["global_features"][1].item() * 10.0)))
        
    # Search for setup transitions:
    # A step where me.handCount increases or a benched slot goes from empty (0) to a setup Pokemon (Dunsparce/Buneary)
    # and check how V(s) changes.
    
    setup_transitions = []
    
    # Let's run a batch inference to get V(s) for all states to make lookup fast
    val_loader = DataLoader(dataset[:10000], batch_size=512, shuffle=False, collate_fn=collate_fn)
    preds = []
    with torch.no_grad():
        for batch in val_loader:
            gf = batch["global_features"].to(device)
            t_cid = batch["tokens_card_id"].to(device)
            t_role = batch["tokens_role"].to(device)
            t_feat = batch["tokens_features"].to(device)
            mask = batch["attention_mask"].to(device)
            preds.extend(model(gf, t_cid, t_role, t_feat, mask).tolist())
            
    for idx in range(len(preds)):
        dataset[idx]["pred"] = preds[idx]
        
    # Find sequential transitions in the first 10,000 states (approx. 80 games)
    for gid in list(game_histories.keys())[:80]:
        states = game_histories[gid]
        for i in range(len(states) - 1):
            s_curr = states[i]
            s_next = states[i+1]
            
            # Check if predictions were computed
            if "pred" not in s_curr or "pred" not in s_next:
                continue
                
            gf_curr = s_curr["global_features"]
            gf_next = s_next["global_features"]
            
            turn_curr = round(gf_curr[0].item() * 50.0)
            turn_next = round(gf_next[0].item() * 50.0)
            
            # Stay within the same turn
            if turn_curr != turn_next:
                continue
                
            hand_curr = round(gf_curr[7].item() * 60.0)
            hand_next = round(gf_next[7].item() * 60.0)
            
            # If handCount increased significantly (e.g., Lillie's re-draw or search card played)
            if hand_next > hand_curr:
                # Setup cards played like Lillie's (1227) or Poffin (1086) or Ultra Ball (1121)
                # Let's verify if the V(s) increased or stayed stable
                delta_v = s_next["pred"] - s_curr["pred"]
                setup_transitions.append({
                    "type": "Pioche / Recherche (main +)",
                    "before_hand": hand_curr,
                    "after_hand": hand_next,
                    "before_pred": s_curr["pred"],
                    "after_pred": s_next["pred"],
                    "delta_v": delta_v
                })
                
            # Check bench count increases (e.g. Poffin played, bench Pokemon added)
            bench_curr = sum(1 for idx, role in enumerate(s_curr["tokens_role"]) if role == 3 and s_curr["tokens_card_id"][idx] != 0)
            bench_next = sum(1 for idx, role in enumerate(s_next["tokens_role"]) if role == 3 and s_next["tokens_card_id"][idx] != 0)
            if bench_next > bench_curr:
                delta_v = s_next["pred"] - s_curr["pred"]
                setup_transitions.append({
                    "type": "Bench setup (banc +)",
                    "before_bench": bench_curr,
                    "after_bench": bench_next,
                    "before_pred": s_curr["pred"],
                    "after_pred": s_next["pred"],
                    "delta_v": delta_v
                })
                
    print(f"Nombre de transitions de setup trouvées dans l'échantillon : {len(setup_transitions)}")
    if setup_transitions:
        deltas = [t["delta_v"] for t in setup_transitions]
        print(f"  - Delta V(s) moyen après setup : {np.mean(deltas):+.4f}")
        print(f"  - % de transitions où V(s) augmente ou reste stable (delta >= -0.05) : {sum(1 for d in deltas if d >= -0.05)/len(deltas)*100.0:.2f}%")
        
        # Check a few specific examples
        print("\nExemples détaillés de transitions de setup :")
        for i, t in enumerate(setup_transitions[:5], 1):
            if "before_hand" in t:
                desc = f"Main {t['before_hand']} -> {t['after_hand']}"
            else:
                desc = f"Banc {t['before_bench']} -> {t['after_bench']}"
            print(f"  [{i}] {t['type']} ({desc}) : V(s) {t['before_pred']:.4f} -> {t['after_pred']:.4f} (Delta: {t['delta_v']:+.4f})")

if __name__ == "__main__":
    main()
