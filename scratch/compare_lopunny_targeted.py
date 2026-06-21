import os
import sys
sys.path.append("sample_submission")
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import numpy as np
import random
from model import ValueNetwork
from evaluate_lopunny import collate_fn

def evaluate_model(model, val_data, device):
    model.eval()
    val_loader = DataLoader(val_data, batch_size=512, shuffle=False, collate_fn=collate_fn)
    
    preds_all = []
    z_all = []
    
    with torch.no_grad():
        for batch in val_loader:
            gf = batch["global_features"].to(device)
            t_cid = batch["tokens_card_id"].to(device)
            t_role = batch["tokens_role"].to(device)
            t_feat = batch["tokens_features"].to(device)
            mask = batch["attention_mask"].to(device)
            
            preds = model(gf, t_cid, t_role, t_feat, mask)
            preds_all.extend(preds.cpu().tolist())
            z_all.extend(batch["Z"].tolist())
            
    # B1) Phase Accuracies
    phase_counts = {"debut": 0, "milieu": 0, "fin": 0}
    phase_correct = {"debut": 0, "milieu": 0, "fin": 0}
    
    # B2) Calibration
    bins = [[] for _ in range(10)]
    
    # B3) Threatened States
    case1_preds = []
    case1_z = []
    case1_hps = []
    
    case2_preds = []
    case2_z = []
    
    group_high_hp_preds = []
    group_low_hp_preds = []
    
    global_correct = 0
    
    for item, pred, z_val in zip(val_data, preds_all, z_all):
        gf = item["global_features"]
        tokens_cid = item["tokens_card_id"]
        tokens_role = item["tokens_role"]
        tokens_feat = item["tokens_features"]
        
        turn = round(gf[0].item() * 50.0)
        me_prize = round(gf[8].item() * 6.0)
        opp_prize = round(gf[11].item() * 6.0)
        total_prizes = me_prize + opp_prize
        
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
            global_correct += 1
            
        bin_idx = int((pred + 1.0) / 2.0 * 10.0)
        bin_idx = min(9, max(0, bin_idx))
        bins[bin_idx].append(z_val)
        
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
                
        me_hp = tokens_feat[me_active_idx][0].item() * tokens_feat[me_active_idx][1].item() * 350.0 if me_active_cid == 849 else 0.0
        opp_hp = tokens_feat[opp_active_idx][0].item() * tokens_feat[opp_active_idx][1].item() * 350.0 if opp_active_cid == 849 else 0.0
        
        if me_active_cid == 849 and me_prize < opp_prize and opp_has_lopunny:
            if me_hp > 230.0:
                group_high_hp_preds.append(pred)
            else:
                group_low_hp_preds.append(pred)
                
        if me_active_cid == 849 and me_hp <= 230.0 and me_prize < opp_prize and opp_has_lopunny:
            case1_preds.append(pred)
            case1_z.append(z_val)
            case1_hps.append(me_hp)
            
        if opp_active_cid == 849 and opp_hp <= 230.0 and me_prize > opp_prize and self_has_lopunny:
            case2_preds.append(pred)
            case2_z.append(z_val)
            
    global_acc = global_correct / len(val_data) * 100.0
    
    phase_accs = {}
    for phase in ["debut", "milieu", "fin"]:
        cnt = phase_counts[phase]
        phase_accs[phase] = phase_correct[phase] / cnt * 100.0 if cnt > 0 else 0.0
        
    cal_errors = []
    for i in range(10):
        center = -0.9 + i * 0.2
        bin_z = bins[i]
        if bin_z:
            cal_errors.append(abs(np.mean(bin_z) - center))
    mean_cal_error = np.mean(cal_errors) if cal_errors else 0.0
    
    c1_mean_pred = np.mean(case1_preds) if case1_preds else 0.0
    c1_neg_pct = sum(1 for p in case1_preds if p < 0.0) / len(case1_preds) * 100.0 if case1_preds else 0.0
    c1_hp_corr = np.corrcoef(case1_hps, case1_preds)[0, 1] if len(case1_preds) > 5 else 0.0
    
    c2_mean_pred = np.mean(case2_preds) if case2_preds else 0.0
    c2_pos_pct = sum(1 for p in case2_preds if p > 0.0) / len(case2_preds) * 100.0 if case2_preds else 0.0
    
    v_sain = np.mean(group_high_hp_preds) if group_high_hp_preds else 0.0
    v_menace = np.mean(group_low_hp_preds) if group_low_hp_preds else 0.0
    
    criterion = nn.MSELoss()
    val_loss = 0.0
    with torch.no_grad():
        for batch in val_loader:
            gf = batch["global_features"].to(device)
            t_cid = batch["tokens_card_id"].to(device)
            t_role = batch["tokens_role"].to(device)
            t_feat = batch["tokens_features"].to(device)
            mask = batch["attention_mask"].to(device)
            z = batch["Z"].to(device)
            predictions = model(gf, t_cid, t_role, t_feat, mask)
            loss = criterion(predictions, z)
            val_loss += loss.item() * gf.size(0)
    val_loss /= len(val_data)
    
    return {
        "val_loss": val_loss,
        "global_acc": global_acc,
        "phase_accs": phase_accs,
        "mean_cal_error": mean_cal_error,
        "c1_mean_pred": c1_mean_pred,
        "c1_neg_pct": c1_neg_pct,
        "c1_hp_corr": c1_hp_corr,
        "c2_mean_pred": c2_mean_pred,
        "c2_pos_pct": c2_pos_pct,
        "v_sain": v_sain,
        "v_menace": v_menace,
        "bins": [np.mean(b) if b else 0.0 for b in bins],
        "bins_n": [len(b) for b in bins]
    }

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    dataset_path = "selfplay_dataset_lopunny.pt"
    if not os.path.exists(dataset_path):
        dataset_path = os.path.join("sample_submission", dataset_path)
    dataset = torch.load(dataset_path)
    
    torch.manual_seed(42)
    random.seed(42)
    game_ids = list(set(int(item["game_id"]) for item in dataset))
    random.shuffle(game_ids)
    split_idx = int(0.8 * len(game_ids))
    val_game_ids = set(game_ids[split_idx:])
    val_data = [item for item in dataset if int(item["game_id"].item()) in val_game_ids]
    
    # 1. Load Model A (Unweighted)
    path_a = "sample_submission/value_network_lopunny_best.pth"
    model_a = ValueNetwork()
    model_a.load_state_dict(torch.load(path_a, map_location="cpu"))
    model_a.to(device)
    print("Évaluation du modèle d'origine (Non-pondéré)...")
    res_a = evaluate_model(model_a, val_data, device)
    
    # 2. Load Model B (Broad weighted)
    path_b = "sample_submission/value_network_lopunny_weighted_best.pth"
    model_b = ValueNetwork()
    model_b.load_state_dict(torch.load(path_b, map_location="cpu"))
    model_b.to(device)
    print("Évaluation du modèle pondéré large (5.0x)...")
    res_b = evaluate_model(model_b, val_data, device)
    
    # 3. Load Model C (Targeted weighted)
    path_c = "sample_submission/value_network_lopunny_targeted_best.pth"
    if not os.path.exists(path_c):
        print(f"Modèle ciblé non trouvé à {path_c}.")
        return
    model_c = ValueNetwork()
    model_c.load_state_dict(torch.load(path_c, map_location="cpu"))
    model_c.to(device)
    print("Évaluation du modèle pondéré ciblé (10.0x)...")
    res_c = evaluate_model(model_c, val_data, device)
    
    print("\n" + "="*95)
    print(" COMPARATIF 3-VOIES : AVANT vs PONDERE LARGE (5.0x) vs PONDERE CIBLE (10.0x) ")
    print("="*95)
    print(f"| {'Métrique / Mesure':<35} | {'AVANT (Non-pond.)':<18} | {'LARGE (5.0x)':<14} | {'CIBLE (10.0x)':<14} |")
    print(f"|{'-'*37}|{'-'*20}|{'-'*16}|{'-'*16}|")
    
    # Global
    print(f"| Loss de Validation (MSE)           | {res_a['val_loss']:<18.4f} | {res_b['val_loss']:<14.4f} | {res_c['val_loss']:<14.4f} |")
    print(f"| Accuracy Globale (Validation)      | {res_a['global_acc']:<17.2f}% | {res_b['global_acc']:<13.2f}% | {res_c['global_acc']:<13.2f}% |")
    
    # B1 Phases
    print(f"|   - Phase Début (Acc)              | {res_a['phase_accs']['debut']:<17.2f}% | {res_b['phase_accs']['debut']:<13.2f}% | {res_c['phase_accs']['debut']:<13.2f}% |")
    print(f"|   - Phase Milieu (Acc)             | {res_a['phase_accs']['milieu']:<17.2f}% | {res_b['phase_accs']['milieu']:<13.2f}% | {res_c['phase_accs']['milieu']:<13.2f}% |")
    print(f"|   - Phase Fin (Acc)                | {res_a['phase_accs']['fin']:<17.2f}% | {res_b['phase_accs']['fin']:<13.2f}% | {res_c['phase_accs']['fin']:<13.2f}% |")
    
    # B2 Calibration error
    print(f"| Erreur de Calibration Moyenne (B2) | {res_a['mean_cal_error']:<18.4f} | {res_b['mean_cal_error']:<14.4f} | {res_c['mean_cal_error']:<14.4f} |")
    
    # B3 Case 1
    print(f"| Cas 1 : V(s) Moyen (Exp/En avance) | {res_a['c1_mean_pred']:<18.4f} | {res_b['c1_mean_pred']:<14.4f} | {res_c['c1_mean_pred']:<14.4f} |")
    print(f"| Cas 1 : % de prédictions négatives | {res_a['c1_neg_pct']:<17.2f}% | {res_b['c1_neg_pct']:<13.2f}% | {res_c['c1_neg_pct']:<13.2f}% |")
    print(f"| Cas 1 : Corrélation HP / V(s)      | {res_a['c1_hp_corr']:<18.4f} | {res_b['c1_hp_corr']:<14.4f} | {res_c['c1_hp_corr']:<14.4f} |")
    
    # B3 Case 2
    print(f"| Cas 2 : V(s) Moyen (Adv exp/Retard)| {res_a['c2_mean_pred']:<18.4f} | {res_b['c2_mean_pred']:<14.4f} | {res_c['c2_mean_pred']:<14.4f} |")
    print(f"| Cas 2 : % de prédictions positives | {res_a['c2_pos_pct']:<17.2f}% | {res_b['c2_pos_pct']:<13.2f}% | {res_c['c2_pos_pct']:<13.2f}% |")
    
    # Sensitivity
    print(f"| V(s) Moyen Lopunny Sain (HP > 230) | {res_a['v_sain']:<18.4f} | {res_b['v_sain']:<14.4f} | {res_c['v_sain']:<14.4f} |")
    print(f"| V(s) Moyen Lopunny Menacé (HP<=230)| {res_a['v_menace']:<18.4f} | {res_b['v_menace']:<14.4f} | {res_c['v_menace']:<14.4f} |")
    delta_a = res_a['v_sain'] - res_a['v_menace']
    delta_b = res_b['v_sain'] - res_b['v_menace']
    delta_c = res_c['v_sain'] - res_c['v_menace']
    print(f"| Sensibilité (V_sain - V_menace)   | {delta_a:<18.4f} | {delta_b:<14.4f} | {delta_c:<14.4f} |")
    
    print("="*95)
    
    print("\n" + "="*80)
    print(" VERDICT ET DIAGNOSTIC FINAL (CIBLE 10.0x) ")
    print("="*80)
    
    hp_corr_satisf = res_c['c1_hp_corr'] > 0.05
    delta_satisf = delta_c > 0.0
    cal_satisf = res_c['mean_cal_error'] <= 0.08
    
    print(f"1. Sensibilité HP correcte (Delta > 0)    : {'OUI' if delta_satisf else 'NON'} (Delta = {delta_c:+.4f})")
    print(f"2. Corrélation HP/V(s) positive (> 0.05)   : {'OUI' if hp_corr_satisf else 'NON'} (Corr = {res_c['c1_hp_corr']:+.4f})")
    print(f"3. Calibration maintenue (Erreur <= 0.08) : {'OUI' if cal_satisf else 'NON'} (Erreur = {res_c['mean_cal_error']:.4f})")
    
    if delta_satisf and hp_corr_satisf and cal_satisf:
        print("\n>>> VERDICT FINAL : SUCCÈS !")
        print("    L'entraînement ciblé a permis d'orienter le modèle dans la bonne direction.")
        print("    Le modèle est sensible à la menace des PV tout en maintenant sa calibration intacte.")
        print("    Nous pouvons passer à l'étape 1 de recherche.")
    else:
        print("\n>>> VERDICT FINAL : ÉCHEC.")
        print("    Les critères de santé ne sont pas tous réunis. Veuillez analyser le comparatif.")
    print("="*80)

if __name__ == "__main__":
    main()
