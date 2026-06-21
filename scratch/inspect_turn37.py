import os
import sys
import random
import torch

project_dir = r"c:\Users\adamt\Desktop\Code\Developpement IA\pokemon-tcg-ai-battle\sample_submission"
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

import main
from cg.api import to_observation_class, OptionType
from cg.game import battle_start, battle_select, battle_finish

def read_deck() -> list[int]:
    full_path = os.path.join(project_dir, "deck.csv")
    with open(full_path, "r") as file:
        csv = file.read().split("\n")
    deck = []
    for i in range(60):
        deck.append(int(csv[i]))
    return deck

def play_game(game_idx):
    deck0 = read_deck()
    deck1 = read_deck()
    
    obs_dict, start_data = battle_start(deck0, deck1)
    obs = to_observation_class(obs_dict)
    
    step = 0
    while obs.current.result == -1:
        step += 1
        prev_obs = obs
        action = main.agent(obs_dict)
        chosen_idx = action[0]
        opt = prev_obs.select.option[chosen_idx]
        
        # Print for ANY game that reaches turn 37
        if prev_obs.current.turn == 37:
            print(f"\n--- GAME {game_idx} STEP {step} (Turn {prev_obs.current.turn}, Player {prev_obs.current.yourIndex}) ---")
            print(f"Action choice: chosen_idx={chosen_idx}")
            print(f"Option fields: type={opt.type}, area={getattr(opt, 'area', None)}, index={getattr(opt, 'index', None)}, playerIndex={getattr(opt, 'playerIndex', None)}, cardId={getattr(opt, 'cardId', None)}")
            if prev_obs.select:
                print(f"Select Context: {prev_obs.select.context}")
                print(f"Select Options Count: {len(prev_obs.select.option)}")
                for idx, o in enumerate(prev_obs.select.option):
                    print(f"  Option {idx}: type={o.type}, area={o.area}, index={o.index}, playerIndex={o.playerIndex}, cardId={o.cardId}")
            
        obs_dict = battle_select(action)
        obs = to_observation_class(obs_dict)
            
    battle_finish()

def main_runner():
    random.seed(42)
    torch.manual_seed(42)
    for i in range(1, 15):
        print(f"Running game {i}...")
        play_game(i)

if __name__ == "__main__":
    main_runner()
