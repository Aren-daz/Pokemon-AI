import os
import sys
sys.path.append("sample_submission")
import torch
import numpy as np
import random
from model import ValueNetwork
from torch.utils.data import DataLoader
from evaluate_lopunny import collate_fn

def main():
    dataset_path = "selfplay_dataset_lopunny.pt"
    if not os.path.exists(dataset_path):
        dataset_path = os.path.join("sample_submission", dataset_path)
        
    dataset = torch.load(dataset_path)
    
    # Replicate validation split
    torch.manual_seed(42)
    random.seed(42)
    game_ids = list(set(int(item["game_id"]) for item in dataset))
    random.shuffle(game_ids)
    split_idx = int(0.8 * len(game_ids))
    val_game_ids = set(game_ids[split_idx:])
    val_data = [item for item in dataset if int(item["game_id"]) in val_game_ids]
    
    model_path = "sample_submission/value_network_lopunny_best.pth"
    model = ValueNetwork()
    model.load_state_dict(torch.load(model_path, map_location="cpu"))
    model.eval()
    
    val_loader = DataLoader(val_data, batch_size=512, shuffle=False, collate_fn=collate_fn)
    all_preds = []
    with torch.no_grad():
        for batch in val_loader:
            gf = batch["global_features"]
            t_cid = batch["tokens_card_id"]
            t_role = batch["tokens_role"]
            t_feat = batch["tokens_features"]
            mask = batch["attention_mask"]
            preds = model(gf, t_cid, t_role, t_feat, mask)
            all_preds.extend(preds.tolist())
            
    # Process properties
    processed = []
    for item, pred in zip(val_data, all_preds):
        gf = item["global_features"]
        tokens_cid = item["tokens_card_id"]
        tokens_role = item["tokens_role"]
        tokens_feat = item["tokens_features"]
        
        # Identify active roles
        me_active_idx = -1
        opp_active_idx = -1
        for idx, role in enumerate(tokens_role):
            if role == 1: me_active_idx = idx
            elif role == 2: opp_active_idx = idx
            
        if me_active_idx == -1 or opp_active_idx == -1:
            continue
            
        me_active_cid = tokens_cid[me_active_idx].item()
        opp_active_cid = tokens_cid[opp_active_idx].item()
        
        # Calculate active energy count
        me_active_energy = sum(tokens_feat[me_active_idx][2:14]).item()
        opp_active_energy = sum(tokens_feat[opp_active_idx][2:14]).item()
        
        # Get active HP
        me_active_hp = tokens_feat[me_active_idx][0].item() * tokens_feat[me_active_idx][1].item() * 350.0 if me_active_cid == 849 else 0.0
        opp_active_hp = tokens_feat[opp_active_idx][0].item() * tokens_feat[opp_active_idx][1].item() * 350.0 if opp_active_cid == 849 else 0.0
        
        # Total tokens count
        seq_len = len(tokens_role)
        
        processed.append({
            "seq_len": seq_len,
            "me_active_cid": me_active_cid,
            "opp_active_cid": opp_active_cid,
            "me_active_hp": me_active_hp,
            "opp_active_hp": opp_active_hp,
            "me_active_energy": me_active_energy,
            "opp_active_energy": opp_active_energy,
            "me_prize": round(gf[8].item() * 6.0),
            "opp_prize": round(gf[11].item() * 6.0),
            "pred": pred,
            "Z": item["Z"].item()
        })
        
    print(f"Total processed states: {len(processed)}")
    
    # ----------------------------------------------------
    # TEST 1 : Correlation active HP vs V(s) by sequence length
    # Filter: Player has Mega Lopunny active and is ahead in prizes (same as B3 case)
    # ----------------------------------------------------
    test1_data = [r for r in processed if r["me_active_cid"] == 849 and r["me_prize"] < r["opp_prize"]]
    print(f"\nSub-population for HP test (me_active=849, ahead in prizes): {len(test1_data)}")
    
    # Group by sequence length
    # Let's find cutoffs: <= 15 (short), 16 to 35 (medium), >= 36 (long)
    short_seq = [r for r in test1_data if r["seq_len"] <= 15]
    med_seq = [r for r in test1_data if 16 <= r["seq_len"] <= 35]
    long_seq = [r for r in test1_data if r["seq_len"] >= 36]
    
    print("\n--- TEST 1 : CORRELATION HP / V(s) SELON LA LONGUEUR DE SEQUENCE ---")
    for name, group in [("Séquence Courte (<= 15 tokens)", short_seq), 
                        ("Séquence Moyenne (16-35 tokens)", med_seq), 
                        ("Séquence Longue (>= 36 tokens)", long_seq)]:
        n_group = len(group)
        print(f"{name} : N = {n_group}")
        if n_group > 5:
            hps = [r["me_active_hp"] for r in group]
            preds = [r["pred"] for r in group]
            corr = np.corrcoef(hps, preds)[0, 1]
            print(f"  Corrél. HP / V(s) : {corr:+.4f}")
            print(f"  Z moyen           : {np.mean([r['Z'] for r in group]):+.4f}")
            print(f"  V(s) moyen prédit : {np.mean(preds):+.4f}")
        else:
            print("  Pas assez de données.")
            
    # ----------------------------------------------------
    # TEST 2 : Correlation other active features vs V(s) globally
    # Let's see if the network reads active energy!
    # ----------------------------------------------------
    print("\n--- TEST 2 : CORRELATION DE L'ENERGIE DE L'ACTIF AVEC V(s) ---")
    # Globally for states where player active is Lopunny
    lopunny_states = [r for r in processed if r["me_active_cid"] == 849]
    print(f"États avec Lopunny actif joueur : N = {len(lopunny_states)}")
    if len(lopunny_states) > 5:
        energies = [r["me_active_energy"] for r in lopunny_states]
        preds = [r["pred"] for r in lopunny_states]
        corr_energy = np.corrcoef(energies, preds)[0, 1]
        print(f"Corrélation Énergie de l'Actif / V(s) : {corr_energy:+.4f}")
        
        # Correlation of opponent's active energy
        opp_lopunny_states = [r for r in processed if r["opp_active_cid"] == 849]
        opp_energies = [r["opp_active_energy"] for r in opp_lopunny_states]
        opp_preds = [r["pred"] for r in opp_lopunny_states]
        corr_opp_energy = np.corrcoef(opp_energies, opp_preds)[0, 1]
        print(f"Corrélation Énergie de l'Actif adverse / V(s) : {corr_opp_energy:+.4f}")

if __name__ == "__main__":
    main()
