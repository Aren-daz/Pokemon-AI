import os
import sys
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import numpy as np
import random
from collections import Counter
from model import ValueNetwork

def collate_fn(batch):
    max_L = max(item["tokens_card_id"].shape[0] for item in batch)
    global_features_list = []
    tokens_card_id_list = []
    tokens_role_list = []
    tokens_features_list = []
    attention_mask_list = []
    z_list = []
    
    for item in batch:
        L = item["tokens_card_id"].shape[0]
        padding_needed = max_L - L
        
        global_features_list.append(item["global_features"])
        z_list.append(item["Z"])
        
        if padding_needed > 0:
            tokens_card_id_list.append(torch.cat([item["tokens_card_id"], torch.zeros(padding_needed, dtype=torch.long)]))
            tokens_role_list.append(torch.cat([item["tokens_role"], torch.zeros(padding_needed, dtype=torch.long)]))
            tokens_features_list.append(torch.cat([item["tokens_features"], torch.zeros(padding_needed, 18, dtype=torch.float32)], dim=0))
            attention_mask_list.append(torch.cat([item["attention_mask"], torch.zeros(padding_needed, dtype=torch.float32)]))
        else:
            tokens_card_id_list.append(item["tokens_card_id"])
            tokens_role_list.append(item["tokens_role"])
            tokens_features_list.append(item["tokens_features"])
            attention_mask_list.append(item["attention_mask"])
            
    return {
        "global_features": torch.stack(global_features_list),
        "tokens_card_id": torch.stack(tokens_card_id_list),
        "tokens_role": torch.stack(tokens_role_list),
        "tokens_features": torch.stack(tokens_features_list),
        "attention_mask": torch.stack(attention_mask_list),
        "Z": torch.stack(z_list).squeeze(-1)
    }

def main():
    # Seeds
    torch.manual_seed(42)
    np.random.seed(42)
    random.seed(42)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Appareil d'évaluation : {device}")
    
    dataset_path = "selfplay_dataset_lopunny.pt"
    if not os.path.exists(dataset_path):
        if os.path.exists(os.path.join("sample_submission", dataset_path)):
            dataset_path = os.path.join("sample_submission", dataset_path)
        else:
            print("Dataset introuvable.")
            return
            
    print("Chargement du dataset...")
    dataset = torch.load(dataset_path)
    
    # Pré-conversion
    game_id_list = []
    for item in dataset:
        item["tokens_card_id"] = torch.as_tensor(item["tokens_card_id"], dtype=torch.long)
        item["tokens_role"] = torch.as_tensor(item["tokens_role"], dtype=torch.long)
        item["tokens_features"] = torch.as_tensor(item["tokens_features"], dtype=torch.float32)
        item["global_features"] = torch.as_tensor(item["global_features"], dtype=torch.float32)
        item["attention_mask"] = torch.as_tensor(item["attention_mask"], dtype=torch.float32)
        item["Z"] = torch.as_tensor(item["Z"], dtype=torch.float32)
        item["game_id"] = torch.as_tensor(item["game_id"], dtype=torch.long)
        game_id_list.append(int(item["game_id"].item()))
        
    # Validation split split (80/20 games)
    game_ids = list(set(game_id_list))
    shuffled_game_ids = list(game_ids)
    random.shuffle(shuffled_game_ids)
    split_idx = int(0.8 * len(shuffled_game_ids))
    val_game_ids = set(shuffled_game_ids[split_idx:])
    val_data = [item for item in dataset if int(item["game_id"].item()) in val_game_ids]
    
    print(f"Validation Split: {len(val_data)} états")
    
    # Load model weights
    model_path = "value_network_lopunny_best.pth"
    if not os.path.exists(model_path):
        if os.path.exists(os.path.join("sample_submission", model_path)):
            model_path = os.path.join("sample_submission", model_path)
        else:
            print("Poids du modèle introuvables.")
            return
            
    model = ValueNetwork().to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    print(f"Modèle chargé depuis {model_path}")
    
    # We will run predictions on all validation data
    val_loader = DataLoader(val_data, batch_size=512, shuffle=False, collate_fn=collate_fn)
    
    all_preds = []
    all_z = []
    
    with torch.no_grad():
        for batch in val_loader:
            gf = batch["global_features"].to(device)
            t_cid = batch["tokens_card_id"].to(device)
            t_role = batch["tokens_role"].to(device)
            t_feat = batch["tokens_features"].to(device)
            mask = batch["attention_mask"].to(device)
            
            preds = model(gf, t_cid, t_role, t_feat, mask)
            all_preds.extend(preds.cpu().tolist())
            all_z.extend(batch["Z"].tolist())
            
    # B1) Profil par phase
    phase_counts = {"debut": 0, "milieu": 0, "fin": 0}
    phase_correct = {"debut": 0, "milieu": 0, "fin": 0}
    
    for item, pred, z_val in zip(val_data, all_preds, all_z):
        gf = item["global_features"]
        turn = round(gf[0].item() * 50.0)
        me_prize = round(gf[8].item() * 6.0)
        opp_prize = round(gf[11].item() * 6.0)
        total_prizes = me_prize + opp_prize
        
        # Phase classification (Turn 0 is debut)
        if turn == 0 or total_prizes >= 11:
            phase = "debut"
        elif total_prizes >= 5:
            phase = "milieu"
        else:
            phase = "fin"
            
        phase_counts[phase] += 1
        is_correct = (pred >= 0.0) == (z_val >= 0.0)
        if is_correct:
            phase_correct[phase] += 1
            
    print("\n" + "="*60)
    print(" MESURE B1 — PROFIL PAR PHASE DE JEU ")
    print("="*60)
    print(f"| {'Phase':<8} | {'Accuracy':<10} | {'nb états (N)':<12} | {'Profil Abomasnow':<18} |")
    print(f"|{'-'*10}|{'-'*12}|{'-'*14}|{'-'*20}|")
    for phase in ["debut", "milieu", "fin"]:
        cnt = phase_counts[phase]
        acc = (phase_correct[phase] / cnt * 100.0) if cnt > 0 else 0.0
        aboma = "76.0% (début)" if phase == "debut" else ("69.0% (milieu)" if phase == "milieu" else "69.0% (fin)")
        print(f"| {phase:<8} | {acc:8.2f}%  | {cnt:<12d} | {aboma:<18} |")
    print("="*60)
    
    # B2) Calibration globale par bins de 0.2
    bins = [[] for _ in range(10)]
    for pred, z_val in zip(all_preds, all_z):
        # Map pred [-1.0, 1.0] to bin index [0, 9]
        # pred = -1.0 -> idx = 0, pred = 1.0 -> idx = 9
        bin_idx = int((pred + 1.0) / 2.0 * 10.0)
        bin_idx = min(9, max(0, bin_idx))
        bins[bin_idx].append(z_val)
        
    print("\n" + "="*60)
    print(" MESURE B2 — CALIBRATION GLOBALE DU RESEAU ")
    print("="*60)
    print(f"| {'Bin de prédiction':<22} | {'nb états (N)':<12} | {'Z moyen réel':<14} |")
    print(f"|{'-'*24}|{'-'*14}|{'-'*16}|")
    for i in range(10):
        low = -1.0 + i * 0.2
        high = low + 0.2
        bin_z = bins[i]
        n_bin = len(bin_z)
        mean_z = np.mean(bin_z) if n_bin > 0 else 0.0
        print(f"| [{low:+.1f}, {high:+.1f}]             | {n_bin:<12d} | {mean_z:+.4f}       |")
    print("="*60)
    
    # B3) Test de Santé "Menace de KO à 3 prizes"
    case1_states = [] # Player exposed, ahead in prizes
    case2_states = [] # Opponent exposed, behind in prizes
    
    for item, pred, z_val in zip(val_data, all_preds, all_z):
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
                
        self_has_lopunny = False
        for idx, role in enumerate(tokens_role):
            if role in [1, 3] and tokens_cid[idx].item() == 849:
                self_has_lopunny = True
                break
                
        # Case 1
        if me_active_cid == 849:
            hp_ratio = tokens_feat[me_active_idx][0].item()
            max_hp = tokens_feat[me_active_idx][1].item() * 350.0
            current_hp = hp_ratio * max_hp
            
            if current_hp <= 230.0 and me_prize < opp_prize and opp_has_lopunny:
                case1_states.append({
                    "me_prize": me_prize,
                    "opp_prize": opp_prize,
                    "hp": current_hp,
                    "opp_has_lopunny": opp_has_lopunny,
                    "Z": z_val,
                    "pred": pred
                })
                
        # Case 2
        if opp_active_cid == 849:
            hp_ratio = tokens_feat[opp_active_idx][0].item()
            max_hp = tokens_feat[opp_active_idx][1].item() * 350.0
            current_hp = hp_ratio * max_hp
            
            if current_hp <= 230.0 and me_prize > opp_prize and self_has_lopunny:
                case2_states.append({
                    "me_prize": me_prize,
                    "opp_prize": opp_prize,
                    "hp": current_hp,
                    "self_has_lopunny": self_has_lopunny,
                    "Z": z_val,
                    "pred": pred
                })
                
    print("\n" + "="*80)
    print(" MESURE B3 — TEST DECISIF : MENACE DU KO SUR MEGAP LOPUNNY EXPOSE ")
    print("="*80)
    print(f"Nombre total d'états dans le Cas 1 (Moi exposé, en avance aux prizes) : N = {len(case1_states)}")
    print(f"Nombre total d'états dans le Cas 2 (Adversaire exposé, en retard aux prizes) : N = {len(case2_states)}")
    
    # Sample 15-20 states of each case and print
    random.seed(42) # Set seed for deterministic sampling
    sample_size = min(20, len(case1_states))
    c1_sample = random.sample(case1_states, sample_size) if len(case1_states) > 0 else []
    
    print("\nÉCHANTILLON DU CAS 1 (Joueur exposé, en avance aux prizes) :")
    print(f"| {'#':<2} | {'Prizes (me/opp)':<16} | {'PV Lopunny':<12} | {'Lopunny adverse':<16} | {'Z réel':<8} | {'V(s) prédit':<12} |")
    print(f"|{'-'*4}|{'-'*18}|{'-'*14}|{'-'*18}|{'-'*10}|{'-'*14}|")
    for idx, s in enumerate(c1_sample, 1):
        prizes_str = f"{s['me_prize']}/{s['opp_prize']}"
        lop_adv = "Oui" if s["opp_has_lopunny"] else "Non"
        print(f"| {idx:<2} | {prizes_str:<16} | {s['hp']:<12.1f} | {lop_adv:<16} | {s['Z']:+8.1f} | {s['pred']:+12.4f} |")
        
    c1_all_preds = [s["pred"] for s in case1_states]
    c1_mean_pred = np.mean(c1_all_preds) if c1_all_preds else 0.0
    c1_neg_percentage = (sum(1 for p in c1_all_preds if p < 0.0) / len(c1_all_preds) * 100.0) if c1_all_preds else 0.0
    c1_prudent_percentage = (sum(1 for p in c1_all_preds if p <= 0.2) / len(c1_all_preds) * 100.0) if c1_all_preds else 0.0
    print(f"\nMoyenne des V(s) prédits sur le Cas 1 : {c1_mean_pred:+.4f}")
    print(f"Pourcentage de V(s) négatifs (V(s) < 0) : {c1_neg_percentage:.1f}%")
    print(f"Pourcentage de V(s) prudents (V(s) <= +0.2) : {c1_prudent_percentage:.1f}%")
    
    sample_size = min(20, len(case2_states))
    c2_sample = random.sample(case2_states, sample_size) if len(case2_states) > 0 else []
    
    print("\nÉCHANTILLON DU CAS 2 (Adversaire exposé, en retard aux prizes) :")
    print(f"| {'#':<2} | {'Prizes (me/opp)':<16} | {'PV Lopunny Opp':<14} | {'Lopunny allié':<15} | {'Z réel':<8} | {'V(s) prédit':<12} |")
    print(f"|{'-'*4}|{'-'*18}|{'-'*16}|{'-'*17}|{'-'*10}|{'-'*14}|")
    for idx, s in enumerate(c2_sample, 1):
        prizes_str = f"{s['me_prize']}/{s['opp_prize']}"
        lop_allie = "Oui" if s["self_has_lopunny"] else "Non"
        print(f"| {idx:<2} | {prizes_str:<16} | {s['hp']:<14.1f} | {lop_allie:<15} | {s['Z']:+8.1f} | {s['pred']:+12.4f} |")
        
    c2_all_preds = [s["pred"] for s in case2_states]
    c2_mean_pred = np.mean(c2_all_preds) if c2_all_preds else 0.0
    c2_pos_percentage = (sum(1 for p in c2_all_preds if p > 0.0) / len(c2_all_preds) * 100.0) if c2_all_preds else 0.0
    print(f"\nMoyenne des V(s) prédits sur le Cas 2 : {c2_mean_pred:+.4f}")
    print(f"Pourcentage de V(s) positifs (V(s) > 0) : {c2_pos_percentage:.1f}%")
    
    print("\n" + "="*80)
    print(" VERDICT DE SANTE DU RESEAU DE VALEUR ")
    print("="*80)
    print("Question binaire : Le réseau prédit-il une valeur prudente ou négative dans le Cas 1")
    print("malgré un compteur de prizes favorable (preuve de non-cécité au plateau) ?")
    
    if c1_mean_pred < 0.2:
        print(f"\n>>> VERDICT : OUI ! V(s) moyen = {c1_mean_pred:+.4f} (et {c1_neg_percentage:.1f}% de prédictions négatives).")
        print("    Le modèle montre une tendance claire à la prudence face à un Lopunny exposé,")
        print("    prouvant qu'il exploite l'état réel du plateau et évite la cécité d'Abomasnow.")
    else:
        print(f"\n>>> VERDICT : NON. V(s) moyen = {c1_mean_pred:+.4f} (seulement {c1_neg_percentage:.1f}% de prédictions négatives).")
        print("    Le modèle reste aveugle au danger immédiat et se fie principalement au score de prizes.")
    print("="*80)

if __name__ == "__main__":
    main()
