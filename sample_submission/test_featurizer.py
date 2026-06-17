import sys
import os
import random
import torch
import numpy as np
from collections import Counter

from cg.api import to_observation_class
from cg.game import battle_start, battle_select, battle_finish
from featurizer import featurize_state

def read_deck(file_path="deck.csv") -> list[int]:
    if not os.path.exists(file_path):
        file_path = "/kaggle_simulations/agent/" + file_path
    with open(file_path, "r") as file:
        csv = file.read().split("\n")
    deck = []
    for i in range(60):
        deck.append(int(csv[i]))
    return deck

def main():
    print("="*60)
    print(" DÉMARRAGE DU BENCHMARK STATISTIQUE DES TOKENS ")
    print("="*60)
    
    deck0 = read_deck()
    deck1 = read_deck()
    
    # We will simulate 5 complete games to get robust statistics across long battles
    num_games = 5
    token_lengths = []
    total_states_tested = 0
    
    for game_idx in range(1, num_games + 1):
        print(f"Simulation du combat {game_idx}/{num_games}...")
        obs_dict, start_data = battle_start(deck0, deck1)
        if start_data.battlePtr is None or start_data.battlePtr == 0:
            print("Erreur au démarrage du combat.")
            sys.exit(1)
            
        obs = to_observation_class(obs_dict)
        step = 0
        
        while obs.current.result == -1:
            step += 1
            
            # 1. Featurize
            tensors = featurize_state(obs.current)
            total_states_tested += 1
            
            global_features = tensors["global_features"]
            tokens_card_id = tensors["tokens_card_id"]
            tokens_role = tensors["tokens_role"]
            tokens_features = tensors["tokens_features"]
            attention_mask = tensors["attention_mask"]
            
            L = tokens_card_id.shape[0]
            token_lengths.append(L)
            
            # 2. Assertions
            assert global_features.shape == (22,), f"Invalid global shape: {global_features.shape}"
            assert tokens_role.shape == (L,), f"Invalid roles shape: {tokens_role.shape}"
            assert tokens_features.shape == (L, 18), f"Invalid features shape: {tokens_features.shape}"
            assert attention_mask.shape == (L,), f"Invalid mask shape: {attention_mask.shape}"
            
            # NaN / Inf assertions
            assert not torch.isnan(global_features).any(), "NaN found in global_features"
            assert not torch.isinf(global_features).any(), "Inf found in global_features"
            assert not torch.isnan(tokens_features).any(), "NaN found in tokens_features"
            assert not torch.isinf(tokens_features).any(), "Inf found in tokens_features"
            
            # Value assertions
            assert (attention_mask == 1.0).all(), "All active attention mask elements must be 1.0"
            assert tokens_card_id.dtype == torch.long, "tokens_card_id must be Long tensor"
            assert tokens_role.dtype == torch.long, "tokens_role must be Long tensor"
            assert tokens_features.dtype == torch.float32, "tokens_features must be Float tensor"
            
            # Check active elements correspond to non-padding roles
            for idx in range(L):
                role_val = tokens_role[idx].item()
                assert role_val != 0, "Variable sequence should not contain padding roles (0)"
            
            # Choose a random action to progress the game
            options = obs.select.option
            max_c = obs.select.maxCount
            action = random.sample(list(range(len(options))), max_c)
            
            # Apply action
            obs_dict = battle_select(action)
            obs = to_observation_class(obs_dict)
            
        battle_finish()
        print(f"  -> Combat {game_idx} terminé en {step} étapes.")
        
    # Compile Statistics
    min_tokens = min(token_lengths)
    max_tokens = max(token_lengths)
    median_tokens = int(np.median(token_lengths))
    mean_tokens = float(np.mean(token_lengths))
    
    print("\n" + "="*60)
    print(" RÉSULTATS DES ASSERTIONS ET STATISTIQUES DE LONGUEUR ")
    print("="*60)
    print(f" Nombre total d'états validés : {total_states_tested}")
    print(f" Nombre de tokens par état :")
    print(f"   - Minimum : {min_tokens}")
    print(f"   - Médiane : {median_tokens}")
    print(f"   - Moyenne : {mean_tokens:.2f}")
    print(f"   - Maximum : {max_tokens}")
    
    # Distribution summary print
    print("\n Distribution des longueurs de tokens :")
    lengths_counter = Counter(token_lengths)
    for l in sorted(lengths_counter.keys()):
        count = lengths_counter[l]
        percentage = (count / total_states_tested) * 100.0
        bar = "#" * int(percentage / 2.0)
        print(f"   {l:2d} tokens : {count:3d} occurrences ({percentage:5.1f}%) {bar}")
    print("="*60)

if __name__ == "__main__":
    main()
