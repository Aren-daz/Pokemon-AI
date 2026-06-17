import sys
import os
import random
from cg.api import to_observation_class, all_card_data
from cg.game import battle_start, battle_select, battle_finish

def read_deck(file_path="deck.csv") -> list[int]:
    with open(file_path, "r") as file:
        csv = file.read().split("\n")
    deck = []
    for i in range(60):
        deck.append(int(csv[i]))
    return deck

def simple_agent(obs_dict: dict) -> list[int]:
    obs = to_observation_class(obs_dict)
    if obs.select is None:
        return read_deck()
    
    # Select a random sample of options from minCount to maxCount
    # Or just select maxCount options as in main.py
    # Let's make sure we satisfy minCount <= selection size <= maxCount
    num_to_select = obs.select.maxCount
    # If we need to select, option length must be >= num_to_select
    opt_indices = list(range(len(obs.select.option)))
    return random.sample(opt_indices, num_to_select)

from main import agent

def main():
    print("Loading decks...")
    deck0 = read_deck()
    deck1 = read_deck()
    
    print("Starting battle...")
    obs_dict, start_data = battle_start(deck0, deck1)
    
    if start_data.battlePtr is None or start_data.battlePtr == 0:
        print(f"Failed to start battle. Error Player: {start_data.errorPlayer}, Error Type: {start_data.errorType}")
        return
        
    step = 0
    obs = to_observation_class(obs_dict)
    
    while obs.current.result == -1:
        step += 1
        
        # Get action from our new agent in main.py
        action = agent(obs_dict)
        
        # Apply the action
        obs_dict = battle_select(action)
        obs = to_observation_class(obs_dict)
        
    print(f"\nBattle finished in {step} steps!")
    winner = obs.current.result
    print(f"Winner: Player {winner}")
    battle_finish()

if __name__ == "__main__":
    main()
