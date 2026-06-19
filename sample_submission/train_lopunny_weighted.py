import os
import sys
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import numpy as np
import random
from collections import Counter
from model import ValueNetwork

def get_state_weight(item, factor=5.0) -> float:
    """Calculates training loss weight for a state.
    
    If the player's active or opponent's active Mega Lopunny ex (ID 849) has HP <= 230,
    or if any active Pokemon is damaged (HP < 95% of maxHP), we weight the state higher.
    """
    tokens_cid = item["tokens_card_id"]
    tokens_role = item["tokens_role"]
    tokens_feat = item["tokens_features"]
    
    # Find active indices
    me_active_idx = -1
    opp_active_idx = -1
    for idx, r in enumerate(tokens_role):
        role_val = int(r.item() if isinstance(r, torch.Tensor) else r)
        if role_val == 1: # ROLE_SELF_ACTIVE
            me_active_idx = idx
        elif role_val == 2: # ROLE_OPP_ACTIVE
            opp_active_idx = idx
            
    # Check if either active is damaged
    is_damaged = False
    for idx in [me_active_idx, opp_active_idx]:
        if idx != -1:
            cid = int(tokens_cid[idx].item() if isinstance(tokens_cid[idx], torch.Tensor) else tokens_cid[idx])
            hp_ratio = tokens_feat[idx][0].item() if isinstance(tokens_feat[idx][0], torch.Tensor) else tokens_feat[idx][0]
            max_hp = tokens_feat[idx][1].item() if isinstance(tokens_feat[idx][1], torch.Tensor) else tokens_feat[idx][1]
            current_hp = hp_ratio * max_hp * 350.0
            
            if cid == 849:
                if current_hp <= 230.0:
                    is_damaged = True
                    break
            elif cid != 0: # Other non-zero active pokemon
                if hp_ratio < 0.95:
                    is_damaged = True
                    break
                    
    return factor if is_damaged else 1.0

def collate_fn(batch):
    """Dynamically pads sequences in the batch and computes loss weights."""
    max_L = max(item["tokens_card_id"].shape[0] for item in batch)
    
    global_features_list = []
    tokens_card_id_list = []
    tokens_role_list = []
    tokens_features_list = []
    attention_mask_list = []
    z_list = []
    weights_list = []
    
    for item in batch:
        L = item["tokens_card_id"].shape[0]
        padding_needed = max_L - L
        
        global_features_list.append(item["global_features"])
        z_list.append(item["Z"])
        weights_list.append(get_state_weight(item, factor=5.0))
        
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
        "Z": torch.stack(z_list).squeeze(-1),
        "weight": torch.tensor(weights_list, dtype=torch.float32)
    }

def get_game_phase(global_features) -> str:
    me_prize = round(global_features[8].item() * 6.0)
    opp_prize = round(global_features[11].item() * 6.0)
    total_prizes = me_prize + opp_prize
    turn = round(global_features[0].item() * 50.0)
    
    if turn == 0 or total_prizes >= 11:
        return "debut"
    elif total_prizes >= 5:
        return "milieu"
    else:
        return "fin"

def evaluate_metrics(model, dataloader, device):
    model.eval()
    total_loss = 0.0
    criterion = nn.MSELoss()
    
    correct = 0
    total = 0
    
    # Trackers for phase metrics
    phase_counts = {"debut": 0, "milieu": 0, "fin": 0}
    phase_correct = {"debut": 0, "milieu": 0, "fin": 0}
    
    z_all = []
    
    with torch.no_grad():
        for batch in dataloader:
            gf = batch["global_features"].to(device)
            t_cid = batch["tokens_card_id"].to(device)
            t_role = batch["tokens_role"].to(device)
            t_feat = batch["tokens_features"].to(device)
            mask = batch["attention_mask"].to(device)
            z = batch["Z"].to(device)
            
            predictions = model(gf, t_cid, t_role, t_feat, mask)
            loss = criterion(predictions, z)
            total_loss += loss.item() * gf.size(0)
            
            # Vectorized sign accuracy
            is_correct_batch = (predictions >= 0.0) == (z >= 0.0)
            correct += is_correct_batch.sum().item()
            total += gf.size(0)
            
            # Vectorized game phase classification
            turn_batch = torch.round(gf[:, 0] * 50.0)
            me_prize_batch = torch.round(gf[:, 8] * 6.0)
            opp_prize_batch = torch.round(gf[:, 11] * 6.0)
            total_prizes_batch = me_prize_batch + opp_prize_batch
            
            is_turn_zero = (turn_batch == 0.0)
            is_debut = (total_prizes_batch >= 11.0) | is_turn_zero
            is_fin = (total_prizes_batch < 5.0) & (~is_turn_zero)
            is_milieu = ~(is_debut | is_fin)
            
            phase_counts["debut"] += is_debut.sum().item()
            phase_counts["milieu"] += is_milieu.sum().item()
            phase_counts["fin"] += is_fin.sum().item()
            
            phase_correct["debut"] += (is_debut & is_correct_batch).sum().item()
            phase_correct["milieu"] += (is_milieu & is_correct_batch).sum().item()
            phase_correct["fin"] += (is_fin & is_correct_batch).sum().item()
            
            z_all.extend(z.tolist())
            
    avg_loss = total_loss / total if total > 0 else 0
    accuracy = (correct / total) * 100.0 if total > 0 else 0.0
    
    # Baselines calculation
    z_counter = Counter(z_all)
    majority_class = max(z_counter.keys(), key=lambda k: z_counter[k]) if z_counter else 1.0
    majority_count = z_counter[majority_class] if z_counter else 0
    majority_accuracy = (majority_count / len(z_all)) * 100.0 if z_all else 50.0
    
    phase_accuracies = {}
    for phase in ["debut", "milieu", "fin"]:
        cnt = phase_counts[phase]
        phase_accuracies[phase] = (phase_correct[phase] / cnt) * 100.0 if cnt > 0 else 0.0
        
    return {
        "loss": avg_loss,
        "accuracy": accuracy,
        "majority_accuracy": majority_accuracy,
        "phase_accuracies": phase_accuracies,
        "phase_counts": phase_counts
    }

def train_value_network():
    torch.manual_seed(42)
    np.random.seed(42)
    random.seed(42)
    
    torch.set_num_threads(8)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Utilisation de l'appareil d'entraînement: {device}")
    
    # Load dataset
    dataset_path = "selfplay_dataset_lopunny.pt"
    if not os.path.exists(dataset_path):
        if os.path.exists(os.path.join("sample_submission", dataset_path)):
            dataset_path = os.path.join("sample_submission", dataset_path)
        else:
            print(f"Dataset non trouvé: {dataset_path}")
            sys.exit(1)
        
    print(f"Chargement du dataset {dataset_path} en mémoire...")
    dataset = torch.load(dataset_path)
    
    print("Pré-conversion du dataset en tenseurs...")
    game_id_list = []
    for item in dataset:
        item["tokens_card_id"] = torch.as_tensor(item["tokens_card_id"], dtype=torch.long)
        item["tokens_role"] = torch.as_tensor(item["tokens_role"], dtype=torch.long)
        item["tokens_features"] = torch.as_tensor(item["tokens_features"], dtype=torch.float32)
        item["global_features"] = torch.as_tensor(item["global_features"], dtype=torch.float32)
        item["attention_mask"] = torch.as_tensor(item["attention_mask"], dtype=torch.float32)
        item["Z"] = torch.as_tensor(item["Z"], dtype=torch.float32)
        item["game_id"] = torch.as_tensor(item["game_id"], dtype=torch.long)
        
        gid_val = int(item["game_id"].item())
        item["game_id_int"] = gid_val
        game_id_list.append(gid_val)
        
    print("Séparation du dataset en Train/Val (80/20)...")
    game_ids = list(set(game_id_list))
    random.shuffle(game_ids)
    
    split_idx = int(0.8 * len(game_ids))
    train_game_ids = set(game_ids[:split_idx])
    val_game_ids = set(game_ids[split_idx:])
    
    train_data = [item for item in dataset if item["game_id_int"] in train_game_ids]
    val_data = [item for item in dataset if item["game_id_int"] in val_game_ids]
    
    print(f"Dataset chargé : {len(dataset)} états (issus de {len(game_ids)} parties)")
    print(f"  - Entraînement : {len(train_data)} états (de {len(train_game_ids)} parties)")
    print(f"  - Validation    : {len(val_data)} états (de {len(val_game_ids)} parties)")
    
    # Print fraction of weighted states in training dataset
    weighted_states_count = sum(1 for item in train_data if get_state_weight(item, 5.0) > 1.0)
    print(f"  - États pondérés (exposés) dans l'entraînement : {weighted_states_count} ({weighted_states_count/len(train_data)*100.0:.2f}%)")
    
    batch_size = 512
    train_loader = DataLoader(
        train_data, 
        batch_size=batch_size, 
        shuffle=True, 
        collate_fn=collate_fn,
        num_workers=0,
        pin_memory=False
    )
    val_loader = DataLoader(
        val_data, 
        batch_size=batch_size, 
        shuffle=False, 
        collate_fn=collate_fn,
        num_workers=0,
        pin_memory=False
    )
    
    # Model
    model = ValueNetwork().to(device)
    optimizer = optim.Adam(model.parameters(), lr=1.4e-3, weight_decay=1e-4)
    criterion = nn.MSELoss(reduction='none') # Compute element-wise loss for custom weighting
    
    epochs = 30
    print("\nLancement de l'entraînement avec Loss Pondérée (Facteur 5.0x)...")
    
    train_losses = []
    val_losses = []
    best_val_loss = float('inf')
    best_epoch = 0
    
    out_dir = "sample_submission"
    if not os.path.exists(out_dir):
        out_dir = "."
        
    best_model_path = os.path.join(out_dir, "value_network_lopunny_weighted_best.pth")
    final_model_path = os.path.join(out_dir, "value_network_lopunny_weighted.pth")
    
    for epoch in range(1, epochs + 1):
        model.train()
        epoch_loss = 0.0
        total_samples = 0
        
        for batch_idx, batch in enumerate(train_loader, 1):
            gf = batch["global_features"].to(device)
            t_cid = batch["tokens_card_id"].to(device)
            t_role = batch["tokens_role"].to(device)
            t_feat = batch["tokens_features"].to(device)
            mask = batch["attention_mask"].to(device)
            z = batch["Z"].to(device)
            w = batch["weight"].to(device)
            
            optimizer.zero_grad()
            predictions = model(gf, t_cid, t_role, t_feat, mask)
            
            # Element-wise MSE loss, weighted, then reduced to mean
            loss = criterion(predictions, z)
            weighted_loss = (loss * w).mean()
            
            weighted_loss.backward()
            optimizer.step()
            
            epoch_loss += loss.mean().item() * gf.size(0)
            total_samples += gf.size(0)
            
            if batch_idx % 100 == 0 or batch_idx == len(train_loader):
                print(f"  [Époque {epoch}] Batch {batch_idx}/{len(train_loader)} | Loss: {loss.mean().item():.4f}", end="\r", flush=True)
                
        print()
        train_loss = epoch_loss / total_samples
        train_losses.append(train_loss)
        
        # Evaluate validation metrics (unweighted, to evaluate real distribution)
        val_metrics = evaluate_metrics(model, val_loader, device)
        val_loss = val_metrics["loss"]
        val_losses.append(val_loss)
        
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_epoch = epoch
            torch.save(model.state_dict(), best_model_path)
            
        print(f"Époque {epoch:02d}/{epochs} | Loss Train (unweighted): {train_loss:.4f} | Loss Val (unweighted): {val_loss:.4f} | Val Accuracy: {val_metrics['accuracy']:.1f}%")
        
        # Early stopping patience 3 epochs
        if epoch - best_epoch >= 3:
            print(f"\n[Early Stopping] Arrêt précoce déclenché après {epoch} époques sans amélioration de la loss de validation.")
            break
            
    print(f"\nChargement du meilleur checkpoint (Époque {best_epoch:02d} avec Loss Val: {best_val_loss:.4f})...")
    model.load_state_dict(torch.load(best_model_path))
    
    torch.save(model.state_dict(), final_model_path)
    print(f"Modèle final sauvegardé sous {final_model_path}")
    print(f"Meilleur checkpoint sauvegardé sous {best_model_path}")
    
    # Save training curves as a plot
    try:
        import matplotlib.pyplot as plt
        import shutil
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, len(train_losses) + 1), train_losses, label='Train Loss (unweighted)', marker='o')
        plt.plot(range(1, len(val_losses) + 1), val_losses, label='Val Loss', marker='s')
        plt.xlabel('Epoch')
        plt.ylabel('Loss (MSE)')
        plt.title('Lopunny Weighted Training Loss Curves')
        plt.legend()
        plt.grid(True)
        plot_name = "loss_curves_lopunny_weighted.png"
        plt.savefig(plot_name, dpi=150)
        print(f"Courbe de loss sauvegardée sous {plot_name}")
        
        art_dir = r"C:\Users\adamt\.gemini\antigravity\brain\8a040cdd-6fc2-4393-9208-7c74c8421b6a"
        if os.path.exists(art_dir):
            shutil.copy(plot_name, os.path.join(art_dir, plot_name))
            print(f"Courbe de loss copiée dans le dossier d'artifacts: {art_dir}")
    except Exception as e:
        print(f"Erreur lors de la génération du graphique: {e}")
        
    # Save metrics JSON
    try:
        import json
        final_val_metrics = evaluate_metrics(model, val_loader, device)
        metrics_to_save = {
            "train_losses": train_losses,
            "val_losses": val_losses,
            "best_epoch": best_epoch,
            "best_val_loss": best_val_loss,
            "final_val_metrics": {
                "accuracy": final_val_metrics["accuracy"],
                "majority_accuracy": final_val_metrics["majority_accuracy"],
                "phase_accuracies": final_val_metrics["phase_accuracies"],
                "phase_counts": final_val_metrics["phase_counts"]
            }
        }
        metrics_path = os.path.join(out_dir, "training_metrics_lopunny_weighted.json")
        with open(metrics_path, "w") as f:
            json.dump(metrics_to_save, f, indent=4)
        print(f"Métriques sauvegardées sous {metrics_path}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des métriques JSON: {e}")

if __name__ == "__main__":
    train_value_network()
