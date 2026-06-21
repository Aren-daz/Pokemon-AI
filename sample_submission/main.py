import os
import sys
import random
import time
import torch
from collections import Counter

from cg.api import (
    Observation,
    to_observation_class,
    OptionType,
    SelectContext,
    SelectType,
    all_card_data,
    all_attack,
    search_begin,
    search_step,
    search_end,
    search_release,
    EnergyType
)

# Global caches for card and attack names to make logs readable
CARDS_CACHE = {}
ATTACKS_CACHE = {}

GLOBAL_MODEL = None
GLOBAL_DEVICE = torch.device("cpu")
B3_RECORDS = []

def initialize_caches():
    """Load card and attack information into memory for logging."""
    global CARDS_CACHE, ATTACKS_CACHE
    if not CARDS_CACHE:
        try:
            CARDS_CACHE = {c.cardId: c.name for c in all_card_data()}
            ATTACKS_CACHE = {a.attackId: a.name for a in all_attack()}
        except Exception:
            pass

def read_deck_csv() -> list[int]:
    """Read deck.csv and return list of card IDs."""
    file_path = "deck.csv"
    if not os.path.exists(file_path):
        file_path = "/kaggle_simulations/agent/" + file_path
    if not os.path.exists(file_path):
        file_path = os.path.join("sample_submission", "deck.csv")
    with open(file_path, "r") as file:
        csv = file.read().split("\n")
    deck = []
    for i in range(60):
        deck.append(int(csv[i]))
    return deck

def get_value_model():
    """Lazily load the Value Network Model B."""
    global GLOBAL_MODEL
    if GLOBAL_MODEL is None:
        from model import ValueNetwork
        GLOBAL_MODEL = ValueNetwork().to(GLOBAL_DEVICE)
        
        # Locate weights file
        model_path = "value_network_lopunny_weighted_best.pth"
        if not os.path.exists(model_path):
            model_path = os.path.join("sample_submission", model_path)
        if not os.path.exists(model_path):
            model_path = os.path.join("/kaggle_simulations/agent/", model_path)
            
        print(f"[NEURAL AGENT] Loading value network weights from {model_path}...")
        GLOBAL_MODEL.load_state_dict(torch.load(model_path, map_location="cpu"))
        GLOBAL_MODEL.eval()
        
        # Set CPU threads for fast CPU inference
        torch.set_num_threads(4)
        
    return GLOBAL_MODEL

def get_b3_records() -> list:
    """Retrieve and clear process-local B3 metrics."""
    global B3_RECORDS
    records = list(B3_RECORDS)
    B3_RECORDS = []
    return records

# ==========================================
# 1. EVALUATION FUNCTIONS
# ==========================================
def evaluate_state_heuristic(state, player_idx) -> float:
    """Calculates the baseline heuristic score from the perspective of player_idx."""
    if state is None:
        return -10000.0
    if state.result != -1:
        if state.result == player_idx:
            return 100000.0
        elif state.result == 2:  # Draw
            return 0.0
        else:
            return -100000.0
            
    me = state.players[player_idx]
    opp = state.players[1 - player_idx]
    
    score = 0.0
    
    # Prizes taken
    prizes_taken = 6 - len(me.prize)
    opp_prizes_taken = 6 - len(opp.prize)
    score += prizes_taken * 500.0
    score -= opp_prizes_taken * 500.0
    
    # Active HP & Energy
    if me.active and me.active[0]:
        act = me.active[0]
        score += act.hp
        score += len(act.energies) * 50.0
    else:
        score -= 2000.0
        
    if opp.active and opp.active[0]:
        act = opp.active[0]
        score -= act.hp
        score -= len(act.energies) * 50.0
    else:
        score += 2000.0
        
    # Bench HP & Energy
    for b in me.bench:
        score += b.hp * 0.5
        score += len(b.energies) * 25.0
    for b in opp.bench:
        score -= b.hp * 0.5
        score -= len(b.energies) * 25.0
        
    # Hand cards count
    score += me.handCount * 10.0
    score -= opp.handCount * 10.0
    
    return score

def evaluate_state_neural(state, root_player_idx, model, device) -> float:
    """Evaluates a state using the trained Value Network from the perspective of root_player_idx."""
    if state is None:
        return -2.0
    if state.result != -1:
        if state.result == root_player_idx:
            return 2.0
        elif state.result == 2:  # Draw
            return 0.0
        else:
            return -2.0
            
    # Import featurizer inside to avoid circular dependencies
    from featurizer import featurize_state
    
    feat = featurize_state(state)
    gf = feat["global_features"].unsqueeze(0).to(device)
    t_cid = feat["tokens_card_id"].unsqueeze(0).to(device)
    t_role = feat["tokens_role"].unsqueeze(0).to(device)
    t_feat = feat["tokens_features"].unsqueeze(0).to(device)
    mask = feat["attention_mask"].unsqueeze(0).to(device)
    
    with torch.no_grad():
        v = model(gf, t_cid, t_role, t_feat, mask).item()
        
    # If the active player in the evaluated state is the opponent,
    # invert the value since the network evaluates relative to state.yourIndex.
    if state.yourIndex != root_player_idx:
        v = -v
        
    return v

def evaluate_state_generic(state, root_player_idx, evaluation_mode="neural") -> float:
    """Wrapper that routes evaluations to either neural or heuristic logic."""
    if evaluation_mode == "neural":
        model = get_value_model()
        return evaluate_state_neural(state, root_player_idx, model, GLOBAL_DEVICE)
    else:
        return evaluate_state_heuristic(state, root_player_idx)

# ==========================================
# 2. DÉTERMINISATION PRÉCISE
# ==========================================
def get_visible_card_ids(state, target_player_idx):
    """Gathers all visible card IDs owned by target_player_idx."""
    visible = []
    
    def add_card(c):
        if c and c.playerIndex == target_player_idx:
            visible.append(c.id)
            
    for p_idx in [0, 1]:
        p_state = state.players[p_idx]
        if p_state.active and p_state.active[0]:
            act = p_state.active[0]
            if p_idx == target_player_idx:
                visible.append(act.id)
            for c in act.preEvolution: add_card(c)
            for c in act.energyCards: add_card(c)
            for c in act.tools: add_card(c)
            
        for b in p_state.bench:
            if p_idx == target_player_idx:
                visible.append(b.id)
            for c in b.preEvolution: add_card(c)
            for c in b.energyCards: add_card(c)
            for c in b.tools: add_card(c)
            
        for c in p_state.discard:
            add_card(c)
            
        if p_state.hand:
            for c in p_state.hand:
                add_card(c)
                
    if state.stadium:
        add_card(state.stadium[0])
        
    if state.looking:
        for c in state.looking:
            add_card(c)
            
    return visible

def determinize(obs, starting_deck):
    """Generate game-state determinizations for search_begin."""
    state = obs.current
    your_idx = state.yourIndex
    opp_idx = 1 - your_idx
    
    me = state.players[your_idx]
    opp = state.players[opp_idx]
    
    starting_counts = Counter(starting_deck)
    
    # 1. Self unseen cards
    my_visible = get_visible_card_ids(state, your_idx)
    my_visible_counts = Counter(my_visible)
    my_unseen = []
    for cid, count in starting_counts.items():
        unseen_count = max(0, count - my_visible_counts.get(cid, 0))
        my_unseen.extend([cid] * unseen_count)
    random.shuffle(my_unseen)
    
    your_deck = my_unseen[:me.deckCount]
    your_prize = my_unseen[me.deckCount:me.deckCount + len(me.prize)]
    if len(your_deck) < me.deckCount:
        your_deck += [3] * (me.deckCount - len(your_deck))
    if len(your_prize) < len(me.prize):
        your_prize += [3] * (len(me.prize) - len(your_prize))
        
    # 2. Opponent unseen cards
    opp_visible = get_visible_card_ids(state, opp_idx)
    opp_visible_counts = Counter(opp_visible)
    opp_unseen = []
    for cid, count in starting_counts.items():
        unseen_count = max(0, count - opp_visible_counts.get(cid, 0))
        opp_unseen.extend([cid] * unseen_count)
    random.shuffle(opp_unseen)
    
    # Ensure a basic Pokémon is placed at the end of opp_unseen for opponent_active if face down
    opponent_active = []
    if opp.active and opp.active[0] is None:
        found_idx = -1
        for p_id in [722, 721]:
            if p_id in opp_unseen:
                found_idx = opp_unseen.index(p_id)
                break
        if found_idx != -1:
            val = opp_unseen.pop(found_idx)
            opp_unseen.append(val)
        else:
            opp_unseen.append(722)
            
    hand_cnt = opp.handCount
    prize_cnt = len(opp.prize)
    deck_cnt = opp.deckCount
    
    opponent_hand = opp_unseen[:hand_cnt]
    opponent_prize = opp_unseen[hand_cnt:hand_cnt + prize_cnt]
    opponent_deck = opp_unseen[hand_cnt + prize_cnt:hand_cnt + prize_cnt + deck_cnt]
    
    if opp.active and opp.active[0] is None:
        opponent_active = [opp_unseen[-1]]
        
    if len(opponent_hand) < hand_cnt:
        opponent_hand += [3] * (hand_cnt - len(opponent_hand))
    if len(opponent_prize) < prize_cnt:
        opponent_prize += [3] * (prize_cnt - len(opponent_prize))
    if len(opponent_deck) < deck_cnt:
        opponent_deck += [3] * (deck_cnt - len(opponent_deck))
        
    return (your_deck, your_prize, opponent_deck, opponent_prize, opponent_hand, opponent_active)

# ==========================================
# 3. PIMC BEAM SEARCH ALGORITHM
# ==========================================
def beam_search_agent(obs_dict: dict, starting_deck: list[int] = None, N_determinizations: int = 4, depth_turns: int = 2, width: int = 3, evaluation_mode: str = "neural") -> list[int]:
    """Execute Perfect Information Monte Carlo search using Beam Search ply-by-ply with minimax opponent play."""
    obs = to_observation_class(obs_dict)
    
    if obs.select is None:
        if starting_deck is None:
            starting_deck = read_deck_csv()
        return starting_deck
        
    select_info = obs.select
    options = select_info.option
    max_c = select_info.maxCount
    
    # If only one choice is possible, return immediately
    if len(options) <= 1:
        return list(range(len(options)))
        
    # If multiple choices are required, fall back to greedy/first elements
    if max_c > 1:
        return list(range(min(max_c, len(options))))
        
    if starting_deck is None:
        starting_deck = read_deck_csv()
        
    root_player_idx = obs.current.yourIndex
    accumulated_scores = [0.0] * len(options)
    static_accumulated_scores = [0.0] * len(options)
    
    # Check if this state satisfies the B3 threatened active Lopunny conditions
    is_b3 = False
    retreat_idx = -1
    danger_context = None
    
    if select_info.context == SelectContext.MAIN and evaluation_mode == "neural":
        state = obs.current
        me = state.players[root_player_idx]
        opp = state.players[1 - root_player_idx]
        
        # 1. Active must be Mega Lopunny (849) and HP <= 230
        if me.active and me.active[0] and me.active[0].id == 849 and me.active[0].hp <= 230:
            # 2. Opponent must have Mega Lopunny (849) in play
            opp_has_lopunny = False
            if opp.active and opp.active[0] and opp.active[0].id == 849:
                opp_has_lopunny = True
            else:
                for b in opp.bench:
                    if b and b.id == 849:
                        opp_has_lopunny = True
                        break
                        
            if opp_has_lopunny:
                # 3. Retreat must be an option
                for idx, opt in enumerate(options):
                    if opt.type == OptionType.RETREAT:
                        retreat_idx = idx
                        break
                        
                if retreat_idx != -1:
                    is_b3 = True
                    opp_prizes = len(opp.prize)
                    if opp_prizes <= 3:
                        danger_context = "high_danger"
                    elif opp_prizes >= 5:
                        danger_context = "low_danger"
                    else:
                        danger_context = "medium_danger"
                        
    for _ in range(N_determinizations):
        # 1. Determinize deck/prizes/opponent cards
        y_deck, y_prize, o_deck, o_prize, o_hand, o_active = determinize(obs, starting_deck)
        
        # 2. Begin Search Session in simulator
        root_state = search_begin(
            obs,
            y_deck, y_prize,
            o_deck, o_prize, o_hand, o_active,
            manual_coin=False
        )
        
        if root_state is None:
            continue
            
        # Beam entry structure: (path, SearchState, transitions_count, prev_player_idx, current_score)
        beam = [([], root_state, 0, root_player_idx, 0.0)]
        
        # Safety max depth limit in plies to prevent timeout in complex turns
        max_plies = 25
        
        for ply_idx in range(max_plies):
            # Check if all paths in the beam have finished their search
            all_done = True
            for path, s_state, transitions, prev_player, _ in beam:
                sel = s_state.observation.select
                if sel is not None and transitions < 2 and s_state.observation.current.result == -1:
                    all_done = False
                    break
            if all_done:
                break
                
            candidates = []
            
            for path, s_state, transitions, prev_player, current_score in beam:
                sel = s_state.observation.select
                # If terminal, or transition count reaches 2, treat as leaf node
                if sel is None or transitions >= 2 or s_state.observation.current.result != -1:
                    candidates.append((path, s_state, transitions, prev_player, current_score))
                    continue
                    
                current_player = s_state.observation.current.yourIndex
                next_transitions = transitions
                if current_player != prev_player:
                    next_transitions += 1
                    
                # Evaluate immediately if we reached our turn limit (2 turns completed)
                if next_transitions >= 2:
                    score = evaluate_state_generic(s_state.observation.current, root_player_idx, evaluation_mode)
                    candidates.append((path, s_state, next_transitions, current_player, score))
                    continue
                    
                # Expand options depending on whose turn it is
                if current_player == root_player_idx:
                    # MAX Node (Our turn)
                    if sel.maxCount > 1 or sel.minCount > 1:
                        # Multi-choice selection: resolve greedily to avoid exceptions and combinatorics
                        num_to_select = sel.maxCount if sel.maxCount > 0 else sel.minCount
                        num_to_select = min(num_to_select, len(sel.option))
                        selection = list(range(num_to_select))
                        try:
                            next_state = search_step(s_state.searchId, selection)
                            if next_state is not None:
                                new_path = path + [0]
                                score = evaluate_state_generic(next_state.observation.current, root_player_idx, evaluation_mode)
                                if ply_idx == 0:
                                    static_accumulated_scores[0] += score
                                candidates.append((new_path, next_state, next_transitions, current_player, score))
                        except Exception:
                            pass
                    else:
                        # Single-choice selection: expand all options
                        for opt_idx in range(len(sel.option)):
                            try:
                                next_state = search_step(s_state.searchId, [opt_idx])
                                if next_state is not None:
                                    new_path = path + [opt_idx]
                                    score = evaluate_state_generic(next_state.observation.current, root_player_idx, evaluation_mode)
                                    if ply_idx == 0:
                                        static_accumulated_scores[opt_idx] += score
                                    candidates.append((new_path, next_state, next_transitions, current_player, score))
                            except Exception:
                                pass
                else:
                    # MIN Node (Opponent turn)
                    if sel.maxCount > 1 or sel.minCount > 1:
                        # Multi-choice selection: resolve greedily
                        num_to_select = sel.maxCount if sel.maxCount > 0 else sel.minCount
                        num_to_select = min(num_to_select, len(sel.option))
                        selection = list(range(num_to_select))
                        try:
                            next_state = search_step(s_state.searchId, selection)
                            if next_state is not None:
                                score = evaluate_state_generic(next_state.observation.current, root_player_idx, evaluation_mode)
                                new_path = path + [0]
                                candidates.append((new_path, next_state, next_transitions, current_player, score))
                        except Exception:
                            pass
                    else:
                        # Single-choice selection: opponent minimizes our score. Keep only the single worst outcome for us.
                        min_score = float('inf')
                        best_next_state = None
                        best_opt_idx = None
                        
                        for opt_idx in range(len(sel.option)):
                            try:
                                next_state = search_step(s_state.searchId, [opt_idx])
                                if next_state is not None:
                                    score = evaluate_state_generic(next_state.observation.current, root_player_idx, evaluation_mode)
                                    if score < min_score:
                                        # Release previous local best state to prevent leaks
                                        if best_next_state is not None:
                                            search_release(best_next_state.searchId)
                                        min_score = score
                                        best_next_state = next_state
                                        best_opt_idx = opt_idx
                                    else:
                                        # Release state immediately since it is not minimizing
                                        search_release(next_state.searchId)
                            except Exception:
                                pass
                                
                        if best_next_state is not None:
                            new_path = path + [best_opt_idx]
                            candidates.append((new_path, best_next_state, next_transitions, current_player, min_score))
                        
            # Sort candidates by score descending (since we want to keep the best overall trajectories for player_idx)
            candidates.sort(key=lambda x: x[4], reverse=True)
            
            # Keep top W paths
            old_beam = beam
            beam = candidates[:width]
            
            # Memory Management: Release search states that are NOT kept in the new beam
            active_ids = {b[1].searchId for b in beam}
            for pb in old_beam:
                if pb[1].searchId not in active_ids and pb[1].searchId != root_state.searchId:
                    try:
                        search_release(pb[1].searchId)
                    except Exception:
                        pass
            for cand in candidates[width:]:
                if cand[1].searchId not in active_ids:
                    try:
                        search_release(cand[1].searchId)
                    except Exception:
                        pass
                        
        # Accumulate leaf scores for root actions
        for path, _, _, _, score in beam:
            if path:
                root_action = path[0]
                accumulated_scores[root_action] += score
                
        # Clean up search session
        search_end()
        
    # Choose best root option index
    best_option = accumulated_scores.index(max(accumulated_scores))
    
    # Record B3 threat compensation data if conditions are met
    if is_b3:
        best_static_option = static_accumulated_scores.index(max(static_accumulated_scores))
        
        record = {
            "danger_context": danger_context,
            "retreat_available": True,
            "static_choice_is_retreat": (best_static_option == retreat_idx),
            "search_choice_is_retreat": (best_option == retreat_idx)
        }
        global B3_RECORDS
        B3_RECORDS.append(record)
        
    return [best_option]

# ==========================================
# 4. KAGGLE SUBMISSION AGENT INTERFACE
# ==========================================
# Control logging from environment or globally
ENABLE_LOGGING = False

PREVIOUS_OBS = None
LAST_ACTION_INFO = None

def clean_card_name(name: str) -> str:
    if not name:
        return name
    name = name.replace("’", "'").replace("'", "'").replace("\u2019", "'").replace("\u0092", "'")
    name = name.replace("é", "e").replace("é", "e").replace("\u00e9", "e")
    return name

def get_card_display_name(cid):
    if cid is None or cid == 0:
        return "Inconnu (0)"
    name = CARDS_CACHE.get(cid, f"ID {cid}")
    name = clean_card_name(name)
    return f"{name} ({cid})"

def get_pokemon_by_pos(state, player_idx, area, index):
    p_state = state.players[player_idx]
    if area == 4: # Active
        return p_state.active[0] if (p_state.active and p_state.active[0]) else None
    elif area == 5: # Bench
        return p_state.bench[index] if (index < len(p_state.bench) and p_state.bench[index]) else None
    return None

SELECT_CONTEXT_FR = {
    0: "Choix Principal",
    1: "Active Setup",
    2: "Bench Setup",
    3: "Echange/Retrait",
    4: "Active de Secours",
    5: "Placement Banc",
    6: "Mise en Jeu",
    7: "Main",
    8: "Defausse",
    9: "Deck",
    10: "Dessous du Deck",
    11: "Prize",
    12: "Garder en Jeu",
    13: "Cible de Degats",
    14: "Cible de Degats Libre",
    15: "Infliger Degats",
    16: "Retrait de Degats",
    17: "Soin",
    18: "Evolution (Depuis)",
    19: "Evolution (Vers)",
    20: "Devolution",
    21: "Cible d'Attachement"
}

def resolve_option_card_name(prev_obs, opt):
    if opt is None:
        return None
        
    # 1. Direct cardId if available and > 0
    if hasattr(opt, "cardId") and opt.cardId is not None and opt.cardId > 0:
        return get_card_display_name(opt.cardId)
        
    # 2. Extract area, index, and playerIndex
    area = getattr(opt, "area", None)
    index = getattr(opt, "index", None)
    player_idx = getattr(opt, "playerIndex", None)
    
    if area is None or index is None:
        return None
        
    try:
        area_val = int(area)
        index_val = int(index)
    except (ValueError, TypeError):
        return None
        
    # Check for TOOL_CARD or ENERGY_CARD which require special lookups if not direct
    opt_type = getattr(opt, "type", None)
    
    # AreaType.DECK = 1, HAND = 2, DISCARD = 3, ACTIVE = 4, BENCH = 5, PRIZE = 6, STADIUM = 7, LOOKING = 12
    if area_val == 1: # DECK
        if prev_obs and prev_obs.select and prev_obs.select.deck:
            if index_val < len(prev_obs.select.deck):
                c = prev_obs.select.deck[index_val]
                if c and hasattr(c, "id") and c.id > 0:
                    return get_card_display_name(c.id)
        return None
        
    if prev_obs is None or prev_obs.current is None:
        return None
        
    state = prev_obs.current
    
    if player_idx is None:
        player_idx = state.yourIndex
        
    try:
        player_idx_val = int(player_idx)
    except (ValueError, TypeError):
        return None
        
    if player_idx_val < 0 or player_idx_val >= len(state.players):
        return None
        
    p_state = state.players[player_idx_val]
    
    if opt_type == OptionType.TOOL_CARD:
        tool_idx = getattr(opt, "toolIndex", None)
        if tool_idx is not None:
            try:
                tool_idx_val = int(tool_idx)
            except (ValueError, TypeError):
                return None
            pokemon = None
            if area_val == 4: # ACTIVE
                pokemon = p_state.active[0] if (p_state.active and p_state.active[0]) else None
            elif area_val == 5: # BENCH
                pokemon = p_state.bench[index_val] if (index_val < len(p_state.bench) and p_state.bench[index_val]) else None
            if pokemon and pokemon.tools and tool_idx_val < len(pokemon.tools):
                t_card = pokemon.tools[tool_idx_val]
                if t_card and hasattr(t_card, "id") and t_card.id > 0:
                    return get_card_display_name(t_card.id)
        return None
        
    elif opt_type in (OptionType.ENERGY_CARD, OptionType.ENERGY):
        energy_idx = getattr(opt, "energyIndex", None)
        if energy_idx is not None:
            try:
                energy_idx_val = int(energy_idx)
            except (ValueError, TypeError):
                return None
            pokemon = None
            if area_val == 4: # ACTIVE
                pokemon = p_state.active[0] if (p_state.active and p_state.active[0]) else None
            elif area_val == 5: # BENCH
                pokemon = p_state.bench[index_val] if (index_val < len(p_state.bench) and p_state.bench[index_val]) else None
            if pokemon and pokemon.energyCards and energy_idx_val < len(pokemon.energyCards):
                e_card = pokemon.energyCards[energy_idx_val]
                if e_card and hasattr(e_card, "id") and e_card.id > 0:
                    return get_card_display_name(e_card.id)
        return None
        
    # Standard CARD option resolution
    if area_val == 2: # HAND
        if p_state.hand and index_val < len(p_state.hand):
            c = p_state.hand[index_val]
            if c and hasattr(c, "id") and c.id > 0:
                return get_card_display_name(c.id)
                
    elif area_val == 3: # DISCARD
        if p_state.discard and index_val < len(p_state.discard):
            c = p_state.discard[index_val]
            if c and hasattr(c, "id") and c.id > 0:
                return get_card_display_name(c.id)
                
    elif area_val == 4: # ACTIVE
        if p_state.active and len(p_state.active) > 0:
            c = p_state.active[0]
            if c and hasattr(c, "id") and c.id > 0:
                return get_card_display_name(c.id)
                
    elif area_val == 5: # BENCH
        if p_state.bench and index_val < len(p_state.bench):
            c = p_state.bench[index_val]
            if c and hasattr(c, "id") and c.id > 0:
                return get_card_display_name(c.id)
                
    elif area_val == 6: # PRIZE
        if p_state.prize and index_val < len(p_state.prize):
            c = p_state.prize[index_val]
            if c and hasattr(c, "id") and c.id > 0:
                return get_card_display_name(c.id)
                
    elif area_val == 7: # STADIUM
        if state.stadium and index_val < len(state.stadium):
            c = state.stadium[index_val]
            if c and hasattr(c, "id") and c.id > 0:
                return get_card_display_name(c.id)
                
    elif area_val == 12: # LOOKING
        if state.looking and index_val < len(state.looking):
            c = state.looking[index_val]
            if c and hasattr(c, "id") and c.id > 0:
                return get_card_display_name(c.id)
                
    return None

def serialize_pokemon(p):
    if p is None:
        return None
    return {
        "id": p.id,
        "name": CARDS_CACHE.get(p.id, f"ID {p.id}"),
        "hp": p.hp,
        "maxHp": p.maxHp,
        "energies": [get_card_display_name(e.id) for e in p.energyCards if e],
        "tools": [get_card_display_name(t.id) for t in p.tools if t],
        "preEvolution": [get_card_display_name(c.id) for c in p.preEvolution if c]
    }

def serialize_player_board(player_state):
    active_pokemon = player_state.active[0] if (player_state.active and player_state.active[0]) else None
    return {
        "deck_count": player_state.deckCount,
        "hand_count": player_state.handCount,
        "prize_count": len(player_state.prize),
        "active": serialize_pokemon(active_pokemon),
        "bench": [serialize_pokemon(b) for b in player_state.bench if b],
        "discard": [get_card_display_name(c.id) for c in player_state.discard if c]
    }

def get_hand_list(player_state):
    if not player_state.hand:
        return []
    return [get_card_display_name(c.id) for c in player_state.hand if c]

def get_state_diff(prev_state, curr_state, player_idx):
    p_prev = prev_state.players[player_idx]
    p_curr = curr_state.players[player_idx]
    
    # Hand diff
    prev_hand_ids = [c.id for c in p_prev.hand if c] if p_prev.hand else []
    curr_hand_ids = [c.id for c in p_curr.hand if c] if p_curr.hand else []
    added_hand_counts = Counter(curr_hand_ids) - Counter(prev_hand_ids)
    added_to_hand = []
    for cid, cnt in added_hand_counts.items():
        added_to_hand.extend([get_card_display_name(cid)] * cnt)
        
    removed_hand_counts = Counter(prev_hand_ids) - Counter(curr_hand_ids)
    removed_from_hand = []
    for cid, cnt in removed_hand_counts.items():
        removed_from_hand.extend([get_card_display_name(cid)] * cnt)
        
    # Bench diff
    prev_bench_ids = [b.id for b in p_prev.bench if b]
    curr_bench_ids = [b.id for b in p_curr.bench if b]
    added_bench_counts = Counter(curr_bench_ids) - Counter(prev_bench_ids)
    added_to_bench = []
    for cid, cnt in added_bench_counts.items():
        added_to_bench.extend([get_card_display_name(cid)] * cnt)
        
    # Discard diff
    prev_discard_ids = [c.id for c in p_prev.discard if c] if p_prev.discard else []
    curr_discard_ids = [c.id for c in p_curr.discard if c] if p_curr.discard else []
    added_discard_counts = Counter(curr_discard_ids) - Counter(prev_discard_ids)
    added_to_discard = []
    for cid, cnt in added_discard_counts.items():
        added_to_discard.extend([get_card_display_name(cid)] * cnt)
        
    return {
        "added_to_hand": added_to_hand,
        "removed_from_hand": removed_from_hand,
        "added_to_bench": added_to_bench,
        "added_to_discard": added_to_discard
    }

def print_table_state(obs):
    import json
    state = obs.current
    p0 = state.players[0]
    p1 = state.players[1]
    
    event_data = {
        "event": "turn_start",
        "turn": state.turn,
        "active_player": state.yourIndex,
        "hands": {
            "player_0": get_hand_list(p0),
            "player_1": get_hand_list(p1)
        },
        "board": {
            "player_0": serialize_player_board(p0),
            "player_1": serialize_player_board(p1)
        }
    }
    print(json.dumps(event_data))

def log_transition_result(prev_obs, curr_obs, last_action_info):
    import json
    opt = last_action_info["option"]
    opt_type = last_action_info["type"]
    player_idx = last_action_info["player_idx"]
    
    prev_state = prev_obs.current
    curr_state = curr_obs.current
    
    diff = get_state_diff(prev_state, curr_state, player_idx)
    
    event_data = {
        "event": "action",
        "turn": prev_state.turn,
        "player": player_idx,
        "action_type": opt_type.name if hasattr(opt_type, "name") else str(opt_type),
        "action_detail": "",
        "resolved": None,
        "hands": {
            "player_0": get_hand_list(curr_state.players[0]),
            "player_1": get_hand_list(curr_state.players[1])
        },
        "board": {
            "player_0": serialize_player_board(curr_state.players[0]),
            "player_1": serialize_player_board(curr_state.players[1])
        },
        "result": {
            "added_to_hand": diff["added_to_hand"],
            "removed_from_hand": diff["removed_from_hand"],
            "added_to_bench": diff["added_to_bench"],
            "added_to_discard": diff["added_to_discard"]
        }
    }
    
    if opt_type == OptionType.EVOLVE:
        p_before = get_pokemon_by_pos(prev_state, player_idx, opt.inPlayArea, opt.inPlayIndex)
        p_after = get_pokemon_by_pos(curr_state, player_idx, opt.inPlayArea, opt.inPlayIndex)
        
        cid_before = p_before.id if p_before else None
        hp_before = p_before.hp if p_before else 0
        max_hp_before = p_before.maxHp if p_before else 0
        
        cid_after = p_after.id if p_after else None
        hp_after = p_after.hp if p_after else 0
        max_hp_after = p_after.maxHp if p_after else 0
        
        damage_conserved = max_hp_before - hp_before
        event_data["action_detail"] = f"Evolue {get_card_display_name(cid_before)} en {get_card_display_name(cid_after)}"
        event_data["resolved"] = get_card_display_name(cid_before)
        event_data["result"]["evolution"] = {
            "from_card": get_card_display_name(cid_before),
            "to_card": get_card_display_name(cid_after),
            "hp_before": hp_before,
            "max_hp_before": max_hp_before,
            "hp_after": hp_after,
            "max_hp_after": max_hp_after,
            "damage_conserved": damage_conserved
        }
        
    elif opt_type == OptionType.ATTACH:
        hand_before = prev_state.players[player_idx].hand
        cid = None
        if opt.index is not None and hand_before and opt.index < len(hand_before):
            card = hand_before[opt.index]
            cid = card.id if card else None
        elif opt.cardId is not None:
            cid = opt.cardId
            
        target = get_pokemon_by_pos(prev_state, player_idx, opt.inPlayArea, opt.inPlayIndex)
        target_name = get_card_display_name(target.id) if target else "Inconnu"
        
        is_tool = False
        if cid is not None:
            try:
                card_data = [c for c in all_card_data() if c.cardId == cid]
                if card_data:
                    from cg.api import CardType
                    is_tool = (card_data[0].cardType == CardType.TOOL)
            except Exception:
                pass
                
        type_str = "Outil" if is_tool else "Energie"
        event_data["action_detail"] = f"Attache {type_str} {get_card_display_name(cid)} sur {target_name}"
        event_data["resolved"] = get_card_display_name(cid)
        event_data["result"]["attached_card"] = get_card_display_name(cid)
        event_data["result"]["attached_target"] = target_name
        event_data["result"]["is_tool"] = is_tool
        
    elif opt_type == OptionType.ABILITY:
        # Bug fix: ABILITY options use area and index, not inPlayArea and inPlayIndex
        user = get_pokemon_by_pos(prev_state, player_idx, opt.area, opt.index)
        user_name = get_card_display_name(user.id) if user else "Pokémon"
        
        ability_name = "Talent"
        if user:
            try:
                card_data = [c for c in all_card_data() if c.cardId == user.id]
                if card_data and card_data[0].skills:
                    ability_name = clean_card_name(card_data[0].skills[0].name)
            except Exception:
                pass
                
        event_data["action_detail"] = f"{user_name} utilise {ability_name}"
        event_data["resolved"] = user_name
        event_data["result"]["ability_name"] = ability_name
        event_data["result"]["ability_user"] = user_name
        
    elif opt_type == OptionType.RETREAT:
        p_prev = prev_state.players[player_idx].active[0] if (prev_state.players[player_idx].active and prev_state.players[player_idx].active[0]) else None
        p_curr = curr_state.players[player_idx].active[0] if (curr_state.players[player_idx].active and curr_state.players[player_idx].active[0]) else None
        
        name_prev = get_card_display_name(p_prev.id) if p_prev else "Inconnu"
        name_curr = get_card_display_name(p_curr.id) if p_curr else "Inconnu"
        
        event_data["action_detail"] = f"Retraite {name_prev} -> {name_curr}"
        event_data["resolved"] = name_prev
        event_data["result"]["retreated_from"] = name_prev
        event_data["result"]["retreated_to"] = name_curr
        
    elif opt_type == OptionType.ATTACK:
        attacker = prev_state.players[player_idx].active[0]
        attacker_name = get_card_display_name(attacker.id) if attacker else "Inconnu"
        
        attack_name = clean_card_name(ATTACKS_CACHE.get(opt.attackId, f"Attaque ID {opt.attackId}"))
        
        opp_idx = 1 - player_idx
        target_prev = prev_state.players[opp_idx].active[0] if (prev_state.players[opp_idx].active and prev_state.players[opp_idx].active[0]) else None
        target_curr = curr_state.players[opp_idx].active[0] if (curr_state.players[opp_idx].active and curr_state.players[opp_idx].active[0]) else None
        
        target_name = get_card_display_name(target_prev.id) if target_prev else "Inconnu"
        hp_before = target_prev.hp if target_prev else 0
        hp_after = 0
        if target_curr is not None and target_prev is not None and target_curr.id == target_prev.id:
            hp_after = target_curr.hp
            
        real_damage_dealt = max(0, hp_before - hp_after)
        ko = (hp_before > 0 and hp_after == 0)
        
        # Determine engine_damage from logs
        engine_damage = None
        damage_source = "hp_delta_truncated"
        
        if target_prev is not None and curr_obs and curr_obs.logs:
            for log in curr_obs.logs:
                # LogType.HP_CHANGE is 16
                if log.type == 16 and log.value is not None:
                    # Match by serial or card ID
                    serial_match = (log.serial == target_prev.serial) if (hasattr(log, "serial") and target_prev.serial) else False
                    card_id_match = (log.cardId == target_prev.id) if hasattr(log, "cardId") else False
                    if serial_match or card_id_match:
                        engine_damage = -log.value
                        damage_source = "engine_log"
                        break
                        
        if engine_damage is None:
            engine_damage = real_damage_dealt
            
        event_data["action_detail"] = f"{attacker_name} utilise {attack_name} sur {target_name} (Degats: {engine_damage}, KO: {ko})"
        event_data["resolved"] = attacker_name
        event_data["result"]["attack_name"] = attack_name
        event_data["result"]["attack_target"] = target_name
        event_data["result"]["hp_before"] = hp_before
        event_data["result"]["hp_after"] = hp_after
        event_data["result"]["real_damage_dealt"] = real_damage_dealt
        event_data["result"]["engine_damage"] = engine_damage
        event_data["result"]["damage_source"] = damage_source
        event_data["result"]["ko"] = ko
        
    elif opt_type == OptionType.PLAY:
        hand_before = prev_state.players[player_idx].hand
        cid = None
        if opt.index is not None and hand_before and opt.index < len(hand_before):
            card = hand_before[opt.index]
            cid = card.id if card else None
        elif opt.cardId is not None:
            cid = opt.cardId
            
        event_data["action_detail"] = f"Joue la carte {get_card_display_name(cid)}"
        event_data["resolved"] = get_card_display_name(cid)
        event_data["result"]["played_card"] = get_card_display_name(cid)
        
    elif opt_type == OptionType.END:
        event_data["action_detail"] = "Termine son tour"
        
    elif opt_type == OptionType.YES:
        event_data["action_detail"] = "Choisit Oui"
        
    elif opt_type == OptionType.NO:
        event_data["action_detail"] = "Choisit Non"
        
    elif opt_type == OptionType.NUMBER:
        event_data["action_detail"] = f"Choisit le nombre {opt.number}"
        
    elif opt_type in (OptionType.CARD, OptionType.TOOL_CARD, OptionType.ENERGY_CARD):
        card_name = resolve_option_card_name(prev_obs, opt)
        context_val = prev_obs.select.context if (prev_obs and prev_obs.select) else None
        context_str = SELECT_CONTEXT_FR.get(int(context_val), "Selection") if context_val is not None else "Selection"
        
        if card_name:
            event_data["action_detail"] = f"Selectionne la carte {card_name} ({context_str})"
            event_data["resolved"] = card_name
        else:
            idx_val = getattr(opt, "index", None)
            if idx_val is not None:
                event_data["action_detail"] = f"Selectionne option index {idx_val} ({context_str})"
            else:
                event_data["action_detail"] = f"Selectionne une carte ({context_str})"
            event_data["resolved"] = None
            
    elif opt_type == OptionType.ENERGY:
        card_name = resolve_option_card_name(prev_obs, opt)
        if card_name:
            event_data["action_detail"] = f"Selectionne l'energie {card_name}"
            event_data["resolved"] = card_name
        else:
            event_data["action_detail"] = f"Selectionne l'energie {get_card_display_name(opt.cardId)}"
            event_data["resolved"] = get_card_display_name(opt.cardId) if opt.cardId else None
        
    elif opt_type == OptionType.DISCARD:
        event_data["action_detail"] = f"Defausse la carte {get_card_display_name(opt.cardId)}"
        event_data["resolved"] = get_card_display_name(opt.cardId)
        
    # Post-facto resolution from transition result/diff
    if event_data.get("action_type") in ("CARD", "3"):
        removed_hand = event_data["result"].get("removed_from_hand", [])
        added_hand = event_data["result"].get("added_to_hand", [])
        
        # 1. Mulligan detection
        if len(removed_hand) >= 6 and len(added_hand) >= 6:
            event_data["resolved"] = "Mulligan (main remélangée)"
            event_data["action_detail"] = "Mulligan (main remélangée)"
            
        # 2. Extract card name from single-card results if not resolved yet
        elif not event_data.get("resolved"):
            context_val = prev_obs.select.context if (prev_obs and prev_obs.select) else None
            if len(added_hand) == 1:
                card_name = added_hand[0]
                event_data["resolved"] = card_name
                context_str = SELECT_CONTEXT_FR.get(int(context_val), "Main") if context_val is not None else "Main"
                event_data["action_detail"] = f"Selectionne la carte {card_name} ({context_str})"
            # Setup/active spots or benches
            elif context_val in (1, 2, 3, 4, 5):
                added_bench = event_data["result"].get("added_to_bench", [])
                if len(added_bench) == 1:
                    card_name = added_bench[0]
                    event_data["resolved"] = card_name
                    context_str = SELECT_CONTEXT_FR.get(int(context_val), "Selection")
                    event_data["action_detail"] = f"Selectionne la carte {card_name} ({context_str})"
        
    print(json.dumps(event_data))

def agent(obs_dict: dict) -> list[int]:
    """Your main submitted agent function running neural PIMC Beam Search."""
    global PREVIOUS_OBS, LAST_ACTION_INFO
    initialize_caches()
    obs = to_observation_class(obs_dict)
    
    if obs.select is None:
        print("[AGENT] Initialisation : Envoi du deck de 60 cartes.")
        PREVIOUS_OBS = None
        LAST_ACTION_INFO = None
        return read_deck_csv()
        
    if ENABLE_LOGGING:
        # If there was a previous action, log its outcome
        if PREVIOUS_OBS is not None and LAST_ACTION_INFO is not None:
            log_transition_result(PREVIOUS_OBS, obs, LAST_ACTION_INFO)
            PREVIOUS_OBS = None
            LAST_ACTION_INFO = None
            
        # Display the table state in the MAIN context
        if obs.select and obs.select.context == SelectContext.MAIN:
            print_table_state(obs)
            
    # Call PIMC Beam Search in neural evaluation mode
    action = beam_search_agent(
        obs_dict, 
        starting_deck=None, 
        N_determinizations=4, 
        depth_turns=2, 
        width=3, 
        evaluation_mode="neural"
    )
    
    # Save the chosen option details for the next step logging
    if ENABLE_LOGGING:
        select_info = obs.select
        chosen_idx = action[0]
        opt = select_info.option[chosen_idx]
        
        # Save info globally
        PREVIOUS_OBS = obs
        LAST_ACTION_INFO = {
            "type": opt.type,
            "option": opt,
            "player_idx": obs.current.yourIndex
        }
        
    return action
