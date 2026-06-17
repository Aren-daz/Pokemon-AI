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

def collate_fn(batch):
    """Dynamically pads sequences in the batch to the maximum length of this batch."""
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
        "Z": torch.stack(z_list).squeeze(-1) # Shape: (B,)
    }

def get_game_phase(global_features) -> str:
    """Classifies game phase based on total remaining prizes in the global features vector."""
    # Index 8 is len(me.prize)/6.0, Index 11 is len(opp.prize)/6.0
    me_prize = round(global_features[8].item() * 6.0)
    opp_prize = round(global_features[11].item() * 6.0)
    total_prizes = me_prize + opp_prize
    
    if total_prizes >= 11:
        return "debut" # At most 1 prize card taken overall
    elif total_prizes >= 5:
        return "milieu" # Mid game
    else:
        return "fin" # Final sprint, close to victory

def evaluate_metrics(model, dataloader, device):
    model.eval()
    total_loss = 0.0
    criterion = nn.MSELoss()
    
    correct = 0
    total = 0
    
    # Trackers for phase metrics
    phase_counts = {"debut": 0, "milieu": 0, "fin": 0}
    phase_correct = {"debut": 0, "milieu": 0, "fin": 0}
    
    # Majority class baseline tracker
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
            me_prize_batch = torch.round(gf[:, 8] * 6.0)
            opp_prize_batch = torch.round(gf[:, 11] * 6.0)
            total_prizes_batch = me_prize_batch + opp_prize_batch
            
            is_debut = total_prizes_batch >= 11.0
            is_fin = total_prizes_batch < 5.0
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
    # Set seeds for reproducibility
    torch.manual_seed(42)
    np.random.seed(42)
    random.seed(42)
    
    # Optimize CPU threads: set to 8 to avoid thread oversubscription
    torch.set_num_threads(8)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Utilisation de l'appareil d'entraînement: {device}")
    
    # Load dataset
    dataset_path = "selfplay_dataset.pt"
    if not os.path.exists(dataset_path):
        print(f"Dataset non trouvé à l'emplacement: {dataset_path}")
        sys.exit(1)
        
    print("Chargement du dataset en mémoire...")
    dataset = torch.load(dataset_path)
    
    # ----------------------------------------------------
    # Correction 1 : Pré-conversion du dataset en tenseurs du bon dtype
    # ----------------------------------------------------
    print("Pré-conversion du dataset en tenseurs du bon dtype...")
    game_id_list = []
    for item in dataset:
        item["tokens_card_id"] = torch.as_tensor(item["tokens_card_id"], dtype=torch.long)
        item["tokens_role"] = torch.as_tensor(item["tokens_role"], dtype=torch.long)
        item["tokens_features"] = torch.as_tensor(item["tokens_features"], dtype=torch.float32)
        item["global_features"] = torch.as_tensor(item["global_features"], dtype=torch.float32)
        item["attention_mask"] = torch.as_tensor(item["attention_mask"], dtype=torch.float32)
        item["Z"] = torch.as_tensor(item["Z"], dtype=torch.float32)
        item["game_id"] = torch.as_tensor(item["game_id"], dtype=torch.long)
        
        # Save a raw python int for fast list split lookup
        gid_val = int(item["game_id"].item())
        item["game_id_int"] = gid_val
        game_id_list.append(gid_val)
        
    # Vérification des dtypes sur un échantillon
    print("Vérification des dtypes après conversion (échantillon 0) :")
    for k, v in dataset[0].items():
        if isinstance(v, torch.Tensor):
            print(f"  - {k} : dtype={v.dtype}, shape={list(v.shape)}")
            
    # ----------------------------------------------------
    # PIÈGE CRITIQUE 1 : Split par partie (game_id), jamais par état
    # Fast split using the pre-extracted game_id_int
    # ----------------------------------------------------
    print("Séparation du dataset en Train/Val (80/20)...")
    game_ids = list(set(game_id_list))
    random.shuffle(game_ids)
    
    split_idx = int(0.8 * len(game_ids))
    train_game_ids = set(game_ids[:split_idx])
    val_game_ids = set(game_ids[split_idx:])
    
    train_data = [item for item in dataset if item["game_id_int"] in train_game_ids]
    val_data = [item for item in dataset if item["game_id_int"] in val_game_ids]
    
    print(f"Dataset chargé : {len(dataset)} états au total (issus de {len(game_ids)} parties)")
    print(f"  - Entraînement : {len(train_data)} états (de {len(train_game_ids)} parties)")
    print(f"  - Validation    : {len(val_data)} états (de {len(val_game_ids)} parties)")
    
    # ----------------------------------------------------
    # Correction 2 & Bonus : DataLoader avec Workers et Batch=512
    # ----------------------------------------------------
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
    criterion = nn.MSELoss()
    
    epochs = 30
    print("\nLancement de l'entraînement...")
    
    train_losses = []
    val_losses = []
    best_val_loss = float('inf')
    best_epoch = 0
    
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
            
            optimizer.zero_grad()
            predictions = model(gf, t_cid, t_role, t_feat, mask)
            loss = criterion(predictions, z)
            loss.backward()
            optimizer.step()
            
            epoch_loss += loss.item() * gf.size(0)
            total_samples += gf.size(0)
            
            if batch_idx % 100 == 0 or batch_idx == len(train_loader):
                print(f"  [Époque {epoch}] Batch {batch_idx}/{len(train_loader)} | Loss: {loss.item():.4f}", end="\r", flush=True)
                
        print()
        train_loss = epoch_loss / total_samples
        train_losses.append(train_loss)
        
        # Evaluate validation metrics
        val_metrics = evaluate_metrics(model, val_loader, device)
        val_loss = val_metrics["loss"]
        val_losses.append(val_loss)
        
        # Early stopping checkpoint saving
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_epoch = epoch
            torch.save(model.state_dict(), "value_network_best.pth")
            
        print(f"Époque {epoch:02d}/{epochs} | Loss Train: {train_loss:.4f} | Loss Val: {val_loss:.4f} | Val Accuracy: {val_metrics['accuracy']:.1f}%")
        
        # Check early stopping patience
        if epoch - best_epoch >= 3:
            print(f"\n[Early Stopping] Arrêt précoce déclenché après {epoch} époques sans amélioration de la loss de validation.")
            break
            
    # Load the best checkpoint for final evaluation
    print(f"\nChargement du meilleur checkpoint (Époque {best_epoch:02d} avec Loss Val: {best_val_loss:.4f}) pour les métriques...")
    model.load_state_dict(torch.load("value_network_best.pth"))
    
    # Final evaluation
    final_val_metrics = evaluate_metrics(model, val_loader, device)
    
    print("\n" + "="*60)
    print(" RÉSULTATS DE L'ENTRAÎNEMENT DU RÉSEAU DE VALEUR ")
    print("="*60)
    print(f" Final Loss Train : {train_losses[-1]:.4f}")
    print(f" Final Loss Val   : {val_losses[-1]:.4f}")
    print(f" Accuracy de signe globale (Validation) : {final_val_metrics['accuracy']:.2f}%")
    print(f" Comparaison aux baselines :")
    print(f"   - Baseline Aléatoire          : 50.00%")
    print(f"   - Baseline Classe Majoritaire : {final_val_metrics['majority_accuracy']:.2f}%")
    
    # Check if we beat the majority class baseline
    if final_val_metrics['accuracy'] > final_val_metrics['majority_accuracy']:
        print(f"   >>> SUCCÈS : Le modèle bat la classe majoritaire de {final_val_metrics['accuracy'] - final_val_metrics['majority_accuracy']:.2f}% !")
    else:
        print(f"   >>> ATTENTION : Le modèle ne parvient pas encore à battre la classe majoritaire (Overfitting / manque de données).")
        
    print(f"\n Accuracy par phase de jeu (Décomposition) :")
    for phase, acc in final_val_metrics['phase_accuracies'].items():
        cnt = final_val_metrics['phase_counts'][phase]
        print(f"   - Phase {phase:<7} : {acc:6.2f}% ({cnt:3d} états évalués)")
        
    # Check for overfitting
    print("\n Analyse de l'entraînement :")
    if val_losses[-1] > min(val_losses) * 1.15:
        print(f"   >>> ALERTE : Risque d'overfitting détecté. La loss Val minimale était de {min(val_losses):.4f} et a remonté à {val_losses[-1]:.4f}.")
    else:
        print("   >>> STABILITÉ : La loss Val est stable et n'a pas remonté de manière significative.")
    print("="*60)

    # Save training curves as a plot
    try:
        import matplotlib.pyplot as plt
        import shutil
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, len(train_losses) + 1), train_losses, label='Train Loss', marker='o')
        plt.plot(range(1, len(val_losses) + 1), val_losses, label='Val Loss', marker='s')
        plt.xlabel('Epoch')
        plt.ylabel('Loss (MSE)')
        plt.title('Training and Validation Loss Curves')
        plt.legend()
        plt.grid(True)
        plt.savefig('loss_curves.png', dpi=150)
        print("Courbe de loss sauvegardée sous loss_curves.png")
        
        # Copy to artifacts directory if it exists
        art_dir = r"C:\Users\adamt\.gemini\antigravity\brain\8a040cdd-6fc2-4393-9208-7c74c8421b6a"
        if os.path.exists(art_dir):
            shutil.copy("loss_curves.png", os.path.join(art_dir, "loss_curves.png"))
            print(f"Courbe de loss copiée dans le dossier d'artifacts: {art_dir}")
    except Exception as e:
        print(f"Erreur lors de la génération du graphique: {e}")

    # Save metrics as JSON for automatic parsing
    try:
        import json
        metrics_to_save = {
            "train_losses": train_losses,
            "val_losses": val_losses,
            "final_val_metrics": {
                "accuracy": final_val_metrics["accuracy"],
                "majority_accuracy": final_val_metrics["majority_accuracy"],
                "phase_accuracies": final_val_metrics["phase_accuracies"],
                "phase_counts": final_val_metrics["phase_counts"]
            }
        }
        with open("training_metrics.json", "w") as f:
            json.dump(metrics_to_save, f, indent=4)
        print("Métriques d'entraînement sauvegardées sous training_metrics.json")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des métriques JSON: {e}")

    # Save model weights
    torch.save(model.state_dict(), "value_network.pth")
    print("Modèle sauvegardé sous le nom value_network.pth")

if __name__ == "__main__":
    train_value_network()
