import os
import sys
sys.path.append("sample_submission")
import torch
import numpy as np
import random
from model import ValueNetwork

def main():
    dataset_path = "selfplay_dataset_lopunny.pt"
    if not os.path.exists(dataset_path):
        dataset_path = os.path.join("sample_submission", dataset_path)
        
    dataset = torch.load(dataset_path)
    
    # Validation split
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
    
    from evaluate_lopunny import collate_fn
    from torch.utils.data import DataLoader
    
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
            
    # Group states
    results = []
    for item, pred in zip(val_data, all_preds):
        gf = item["global_features"]
        tokens_cid = item["tokens_card_id"]
        tokens_role = item["tokens_role"]
        tokens_feat = item["tokens_features"]
        
        me_prize = round(gf[8].item() * 6.0)
        opp_prize = round(gf[11].item() * 6.0)
        
        me_active_idx = -1
        opp_active_idx = -1
        for idx, role in enumerate(tokens_role):
            if role == 1: me_active_idx = idx
            elif role == 2: opp_active_idx = idx
            
        if me_active_idx == -1 or opp_active_idx == -1:
            continue
            
        me_active_cid = tokens_cid[me_active_idx].item()
        opp_active_cid = tokens_cid[opp_active_idx].item()
        
        opp_has_lopunny = False
        for idx, role in enumerate(tokens_role):
            if role in [2, 4] and tokens_cid[idx].item() == 849:
                opp_has_lopunny = True
                break
                
        results.append({
            "me_prize": me_prize,
            "opp_prize": opp_prize,
            "me_active_cid": me_active_cid,
            "opp_active_cid": opp_active_cid,
            "me_active_hp": tokens_feat[me_active_idx][0].item() * tokens_feat[me_active_idx][1].item() * 350.0 if me_active_cid == 849 else 0.0,
            "opp_active_hp": tokens_feat[opp_active_idx][0].item() * tokens_feat[opp_active_idx][1].item() * 350.0 if opp_active_cid == 849 else 0.0,
            "opp_has_lopunny": opp_has_lopunny,
            "Z": item["Z"].item(),
            "pred": pred
        })
        
    # Analyze sensitivity to HP for player active Lopunny when ahead in prizes and opp has Lopunny
    group_high_hp = [r for r in results if r["me_active_cid"] == 849 and r["me_active_hp"] > 230.0 and r["me_prize"] < r["opp_prize"] and r["opp_has_lopunny"]]
    group_low_hp = [r for r in results if r["me_active_cid"] == 849 and r["me_active_hp"] <= 230.0 and r["me_prize"] < r["opp_prize"] and r["opp_has_lopunny"]]
    
    print("\n=== ANALYSE DE LA SENSIBILITE AUX PV (MEGAP LOPUNNY ACTIF JOUEUR, EN AVANCE) ===")
    print(f"Lopunny Actif en bonne santé (HP > 230) : N = {len(group_high_hp)}")
    if group_high_hp:
        print(f"  Z moyen : {np.mean([r['Z'] for r in group_high_hp]):+.4f} | V(s) moyen prédit : {np.mean([r['pred'] for r in group_high_hp]):+.4f}")
    print(f"Lopunny Actif en danger (HP <= 230) : N = {len(group_low_hp)}")
    if group_low_hp:
        print(f"  Z moyen : {np.mean([r['Z'] for r in group_low_hp]):+.4f} | V(s) moyen prédit : {np.mean([r['pred'] for r in group_low_hp]):+.4f}")
        
    # Let's also verify if there is an HP gradient (correlating HP directly with prediction within low HP range)
    if group_low_hp:
        hps = [r["me_active_hp"] for r in group_low_hp]
        preds = [r["pred"] for r in group_low_hp]
        corr = np.corrcoef(hps, preds)[0, 1]
        print(f"Corrélation HP / V(s) dans le cas exposé : {corr:+.4f}")

if __name__ == "__main__":
    main()
