import os
import random
import sys

from cg.api import (
    Observation,
    to_observation_class,
    OptionType,
    SelectContext,
    SelectType,
    all_card_data,
    all_attack
)

# Global caches for card and attack names to make logs readable
CARDS_CACHE = {}
ATTACKS_CACHE = {}

def initialize_caches():
    """Load card and attack information into memory for logging."""
    global CARDS_CACHE, ATTACKS_CACHE
    if not CARDS_CACHE:
        try:
            CARDS_CACHE = {c.cardId: c.name for c in all_card_data()}
            ATTACKS_CACHE = {a.attackId: a.name for a in all_attack()}
        except Exception as e:
            # Fallback if simulator library is not fully initialized yet
            pass

def read_deck_csv() -> list[int]:
    """Read deck.csv.
    
    Returns:
        list[int]: A list of card IDs in the deck.
    """
    file_path = "deck.csv"
    if not os.path.exists(file_path):
        file_path = "/kaggle_simulations/agent/" + file_path
    with open(file_path, "r") as file:
        csv = file.read().split("\n")
    deck = []
    for i in range(60):
        deck.append(int(csv[i]))
    return deck

def log_game_state(obs: Observation):
    """Print a clean summary of the current visible game state."""
    state = obs.current
    if not state:
        return
        
    your_idx = state.yourIndex
    opponent_idx = 1 - your_idx
    
    me = state.players[your_idx]
    opp = state.players[opponent_idx]
    
    print("\n" + "="*50)
    print(f" [TOUR {state.turn}] - JOUEUR ACTIF: Joueur {your_idx}")
    print(f" Mon Deck: {me.deckCount} cartes | Ma Main: {me.handCount} cartes | Récompenses restantes: {len(me.prize)}")
    print(f" Opp Deck: {opp.deckCount} cartes | Opp Main: {opp.handCount} cartes | Récompenses rest. (Opp): {len(opp.prize)}")
    
    # Active Pokemon
    from cg.api import EnergyType
    if me.active and me.active[0]:
        p = me.active[0]
        name = CARDS_CACHE.get(p.id, f"ID {p.id}")
        energies_str = ", ".join(EnergyType(e).name for e in p.energies) if p.energies else "Aucune"
        print(f" Mon Actif: {name} (HP: {p.hp}/{p.maxHp}) | Énergies: {energies_str}")
    else:
        print(" Mon Actif: Aucun")
        
    if opp.active and opp.active[0]:
        p = opp.active[0]
        name = CARDS_CACHE.get(p.id, f"ID {p.id}")
        energies_str = ", ".join(EnergyType(e).name for e in p.energies) if p.energies else "Aucune"
        print(f" Opp Actif: {name} (HP: {p.hp}/{p.maxHp}) | Énergies: {energies_str}")
    else:
        print(" Opp Actif: Aucun")
        
    # Bench
    if me.bench:
        bench_names = [CARDS_CACHE.get(p.id, f"ID {p.id}") for p in me.bench]
        print(f" Mon Banc: {', '.join(bench_names)}")
    if opp.bench:
        bench_names = [CARDS_CACHE.get(p.id, f"ID {p.id}") for p in opp.bench]
        print(f" Opp Banc: {', '.join(bench_names)}")
    print("="*50)

def agent(obs_dict: dict) -> list[int]:
    """Implement Your Pokémon Trading Card Game Agent with heuristics and detailed logging."""
    initialize_caches()
    obs: Observation = to_observation_class(obs_dict)
    
    if obs.select is None:
        print("[AGENT] Initialisation : Envoi du deck de 60 cartes.")
        return read_deck_csv()
        
    log_game_state(obs)
    
    select_info = obs.select
    context = select_info.context
    select_type = select_info.type
    options = select_info.option
    
    context_name = SelectContext(context).name if context is not None else "UNKNOWN"
    type_name = SelectType(select_type).name if select_type is not None else "UNKNOWN"
    
    print(f"[CHOIX REQUIS] Contexte: {context_name} | Type: {type_name}")
    print(f"  Min choix: {select_info.minCount} | Max choix: {select_info.maxCount} | Options dispos: {len(options)}")
    
    # Detailed printing of options to the console
    for idx, opt in enumerate(options):
        opt_type_name = OptionType(opt.type).name
        details = []
        if opt.cardId is not None:
            details.append(f"Card: {CARDS_CACHE.get(opt.cardId, f'ID {opt.cardId}')}")
        if opt.attackId is not None:
            details.append(f"Attack: {ATTACKS_CACHE.get(opt.attackId, f'ID {opt.attackId}')}")
        if opt.number is not None:
            details.append(f"Number: {opt.number}")
        details_str = f" ({', '.join(details)})" if details else ""
        print(f"    [{idx}] {opt_type_name}{details_str}")
        
    # Heuristic Decision-Making
    selected_indices = []
    
    if context == SelectContext.MAIN:
        print("[REFLEXION] Phase principale : Analyse des priorités.")
        
        # Categorize option indices
        attacks = [i for i, opt in enumerate(options) if opt.type == OptionType.ATTACK]
        attaches = [i for i, opt in enumerate(options) if opt.type == OptionType.ATTACH]
        play_cards = [i for i, opt in enumerate(options) if opt.type == OptionType.PLAY]
        abilities = [i for i, opt in enumerate(options) if opt.type == OptionType.ABILITY]
        evolves = [i for i, opt in enumerate(options) if opt.type == OptionType.EVOLVE]
        retreats = [i for i, opt in enumerate(options) if opt.type == OptionType.RETREAT]
        ends = [i for i, opt in enumerate(options) if opt.type == OptionType.END]
        
        # Heuristics Rule 1: Prioritize setup actions (Play cards, Attach energy, Evolve, Use Abilities)
        # before attacking or ending the turn, to build up the board.
        setup_options = play_cards + attaches + evolves + abilities
        if setup_options:
            chosen = setup_options[0]
            opt = options[chosen]
            opt_type_name = OptionType(opt.type).name
            card_name = CARDS_CACHE.get(opt.cardId, "Inconnue") if opt.cardId else ""
            print(f"[DECISION] Action de préparation priorisée -> Index [{chosen}] : {opt_type_name} {card_name}")
            selected_indices = [chosen]
            
        # Heuristics Rule 2: If no setup actions are available, search for attacks!
        elif attacks:
            chosen = attacks[0]
            attack_name = ATTACKS_CACHE.get(options[chosen].attackId, "Inconnue")
            print(f"[DECISION] Pas d'action de préparation dispo. Attaque lancée -> Index [{chosen}] : {attack_name}")
            selected_indices = [chosen]
            
        # Heuristics Rule 3: End the turn if that is the only rational choice.
        elif ends:
            chosen = ends[0]
            print(f"[DECISION] Plus d'actions constructives possibles. Fin du tour -> Index [{chosen}]")
            selected_indices = [chosen]
            
        else:
            # Fallback
            print("[DECISION] Aucune règle heuristique MAIN ne correspond, choix par défaut.")
            selected_indices = [0]
            
    elif context in (SelectContext.SETUP_ACTIVE_POKEMON, SelectContext.TO_ACTIVE):
        # We need to select an Active Pokemon
        print("[REFLEXION] Choix du Pokémon Actif.")
        # Prioritize Pokemon with higher HP if card details are accessible, otherwise first option.
        selected_indices = [0]
        card_id = options[0].cardId
        print(f"[DECISION] Sélection du Pokémon Actif -> Index [0] ({CARDS_CACHE.get(card_id, 'Inconnu')})")
        
    elif context == SelectContext.IS_FIRST:
        # Deciding if we want to go first
        # In TCG, going first can be advantageous or disadvantageous depending on the deck,
        # but let's choose Yes (usually Option 0 is Yes or OptionType.YES)
        yes_opts = [i for i, opt in enumerate(options) if opt.type == OptionType.YES]
        chosen = yes_opts[0] if yes_opts else 0
        print(f"[DECISION] Décision d'ordre de jeu (Aller en premier ?) -> Index [{chosen}] (Oui)")
        selected_indices = [chosen]
        
    else:
        # Fallback generic logic for choosing options (e.g. drawing cards, selecting targets, etc.)
        # Simply choose the first required number of options.
        min_c = select_info.minCount
        max_c = select_info.maxCount
        
        # Avoid choosing duplicate options and stay within bounds
        count_to_select = max_c if max_c > 0 else min_c
        count_to_select = min(count_to_select, len(options))
        
        selected_indices = list(range(count_to_select))
        
        chosen_names = []
        for idx in selected_indices:
            opt = options[idx]
            name = CARDS_CACHE.get(opt.cardId, f"ID {opt.cardId}") if opt.cardId else OptionType(opt.type).name
            chosen_names.append(name)
            
        print(f"[DECISION] Sélection par défaut de {count_to_select} option(s) -> Indices {selected_indices} ({', '.join(chosen_names)})")

    # Final safety check: enforce minCount and maxCount
    if len(selected_indices) < select_info.minCount:
        # Add more options to satisfy minCount
        for i in range(len(options)):
            if i not in selected_indices:
                selected_indices.append(i)
                if len(selected_indices) == select_info.minCount:
                    break
    elif len(selected_indices) > select_info.maxCount:
        selected_indices = selected_indices[:select_info.maxCount]

    return selected_indices
