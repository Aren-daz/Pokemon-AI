import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import sys
import random
import time
import json
import ctypes
import torch
import multiprocessing
from collections import Counter

project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

import cg.api
from cg.api import lib, search_end, search_release
from cg.game import battle_start, battle_select, battle_finish

GLOBAL_MODEL = None
GLOBAL_DEVICE = torch.device("cpu")

# Card Role/Position Constants
ROLE_PADDING = 0
ROLE_SELF_ACTIVE = 1
ROLE_OPP_ACTIVE = 2
ROLE_SELF_BENCH = 3
ROLE_OPP_BENCH = 4
ROLE_STADIUM = 5
ROLE_SELF_HAND = 6
ROLE_SELF_DISCARD = 7
ROLE_OPP_DISCARD = 8
ROLE_LOOKING = 9

def get_agent_ptr():
    if not hasattr(cg.api, "agent_ptr"):
        cg.api.agent_ptr = lib.AgentStart()
    return cg.api.agent_ptr

def fast_search_begin(obs_dict: dict,
                      your_deck: list[int],
                      your_prize: list[int],
                      opponent_deck: list[int],
                      opponent_prize: list[int],
                      opponent_hand: list[int],
                      opponent_active: list[int],
                      manual_coin: bool = False) -> dict:
    sbi = obs_dict["search_begin_input"]
    bs = lib.SearchBegin(
        get_agent_ptr(),
        sbi.encode("ascii"),
        len(sbi),
        (ctypes.c_int*len(your_deck))(*your_deck),
        (ctypes.c_int*len(your_prize))(*your_prize),
        (ctypes.c_int*len(opponent_deck))(*opponent_deck),
        (ctypes.c_int*len(opponent_prize))(*opponent_prize),
        (ctypes.c_int*len(opponent_hand))(*opponent_hand),
        (ctypes.c_int*len(opponent_active))(*opponent_active),
        int(manual_coin)
    )
    res_dict = json.loads(bs.decode())
    if res_dict["error"] != 0:
        raise ValueError(f"SearchBegin error: {res_dict['error']}")
    return res_dict["state"]

def fast_search_step(search_id: int, select: list[int]) -> dict:
    bs = lib.SearchStep(get_agent_ptr(), search_id, (ctypes.c_int*len(select))(*select), len(select))
    res_dict = json.loads(bs.decode())
    if res_dict["error"] != 0:
        raise ValueError(f"SearchStep error: {res_dict['error']}")
    return res_dict["state"]

def read_deck(file_path="deck.csv") -> list[int]:
    if not os.path.exists(file_path):
        file_path = os.path.join(project_dir, file_path)
    if not os.path.exists(file_path):
        file_path = "/kaggle_simulations/agent/deck.csv"
    with open(file_path, "r") as file:
        csv = file.read().split("\n")
    deck = []
    for i in range(60):
        deck.append(int(csv[i]))
    return deck

def get_value_model():
    global GLOBAL_MODEL
    if GLOBAL_MODEL is None:
        from model import ValueNetwork
        GLOBAL_MODEL = ValueNetwork().to(GLOBAL_DEVICE)
        model_path = os.path.join(project_dir, "value_network_lopunny_weighted_best.pth")
        if not os.path.exists(model_path):
            model_path = "/kaggle_simulations/agent/value_network_lopunny_weighted_best.pth"
        GLOBAL_MODEL.load_state_dict(torch.load(model_path, map_location="cpu"))
        GLOBAL_MODEL.eval()
        torch.set_num_threads(1) # Restricted to 1 thread for clean parallelism
    return GLOBAL_MODEL

def get_visible_card_ids_dict(state: dict, target_player_idx: int) -> list[int]:
    visible = []
    def add_card(c):
        if c and c["playerIndex"] == target_player_idx:
            visible.append(c["id"])
            
    for p_idx in [0, 1]:
        p_state = state["players"][p_idx]
        if p_state.get("active") and p_state["active"][0]:
            act = p_state["active"][0]
            if p_idx == target_player_idx:
                visible.append(act["id"])
            for c in act.get("preEvolution") or []: add_card(c)
            for c in act.get("energyCards") or []: add_card(c)
            for c in act.get("tools") or []: add_card(c)
            
        for b in p_state.get("bench") or []:
            if b:
                if p_idx == target_player_idx:
                    visible.append(b["id"])
                for c in b.get("preEvolution") or []: add_card(c)
                for c in b.get("energyCards") or []: add_card(c)
                for c in b.get("tools") or []: add_card(c)
            
        for c in p_state.get("discard") or []:
            add_card(c)
            
        hand = p_state.get("hand")
        if hand:
            for c in hand:
                add_card(c)
                
    stadium = state.get("stadium")
    if stadium:
        add_card(stadium[0])
        
    looking = state.get("looking")
    if looking:
        for c in looking:
            add_card(c)
            
    return visible

def determinize_dict(obs_dict: dict, starting_deck: list[int]):
    state = obs_dict["current"]
    your_idx = state["yourIndex"]
    opp_idx = 1 - your_idx
    
    me = state["players"][your_idx]
    opp = state["players"][opp_idx]
    
    starting_counts = Counter(starting_deck)
    
    my_visible = get_visible_card_ids_dict(state, your_idx)
    my_visible_counts = Counter(my_visible)
    my_unseen = []
    for cid, count in starting_counts.items():
        unseen_count = max(0, count - my_visible_counts.get(cid, 0))
        my_unseen.extend([cid] * unseen_count)
    random.shuffle(my_unseen)
    
    your_deck = my_unseen[:me["deckCount"]]
    your_prize = my_unseen[me["deckCount"]:me["deckCount"] + len(me["prize"])]
    if len(your_deck) < me["deckCount"]:
        your_deck += [3] * (me["deckCount"] - len(your_deck))
    if len(your_prize) < len(me["prize"]):
        your_prize += [3] * (len(me["prize"]) - len(your_prize))
        
    opp_visible = get_visible_card_ids_dict(state, opp_idx)
    opp_visible_counts = Counter(opp_visible)
    opp_unseen = []
    for cid, count in starting_counts.items():
        unseen_count = max(0, count - opp_visible_counts.get(cid, 0))
        opp_unseen.extend([cid] * unseen_count)
    random.shuffle(opp_unseen)
    
    opponent_active = []
    opp_active_list = opp.get("active")
    if opp_active_list and opp_active_list[0] is None:
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
            
    hand_cnt = opp["handCount"]
    prize_cnt = len(opp["prize"])
    deck_cnt = opp["deckCount"]
    
    opponent_hand = opp_unseen[:hand_cnt]
    opponent_prize = opp_unseen[hand_cnt:hand_cnt + prize_cnt]
    opponent_deck = opp_unseen[hand_cnt + prize_cnt:hand_cnt + prize_cnt + deck_cnt]
    
    if opp_active_list and opp_active_list[0] is None:
        opponent_active = [opp_unseen[-1]]
        
    if len(opponent_hand) < hand_cnt:
        opponent_hand += [3] * (hand_cnt - len(opponent_hand))
    if len(opponent_prize) < prize_cnt:
        opponent_prize += [3] * (prize_cnt - len(opponent_prize))
    if len(opponent_deck) < deck_cnt:
        opponent_deck += [3] * (deck_cnt - len(opponent_deck))
        
    return (your_deck, your_prize, opponent_deck, opponent_prize, opponent_hand, opponent_active)

def featurize_state_dict(state: dict) -> dict[str, torch.Tensor]:
    if state is None:
        return {
            "global_features": torch.zeros(22, dtype=torch.float32),
            "tokens_card_id": torch.zeros(0, dtype=torch.long),
            "tokens_role": torch.zeros(0, dtype=torch.long),
            "tokens_features": torch.zeros(0, 18, dtype=torch.float32),
            "attention_mask": torch.zeros(0, dtype=torch.float32),
        }
        
    your_idx = state["yourIndex"]
    opp_idx = 1 - your_idx
    
    me = state["players"][your_idx]
    opp = state["players"][opp_idx]
    
    global_feats = [
        float(state["turn"]) / 50.0,
        float(state["turnActionCount"]) / 10.0,
        1.0 if state["supporterPlayed"] else 0.0,
        1.0 if state["stadiumPlayed"] else 0.0,
        1.0 if state["energyAttached"] else 0.0,
        1.0 if state["retreated"] else 0.0,
        
        # Self counters
        float(me["deckCount"]) / 60.0,
        float(me["handCount"]) / 60.0,
        float(len(me["prize"])) / 6.0,
        
        # Opponent counters
        float(opp["deckCount"]) / 60.0,
        float(opp["handCount"]) / 60.0,
        float(len(opp["prize"])) / 6.0,
        
        # Self Active Status
        1.0 if me["poisoned"] else 0.0,
        1.0 if me["burned"] else 0.0,
        1.0 if me["asleep"] else 0.0,
        1.0 if me["paralyzed"] else 0.0,
        1.0 if me["confused"] else 0.0,
        
        # Opponent Active Status
        1.0 if opp["poisoned"] else 0.0,
        1.0 if opp["burned"] else 0.0,
        1.0 if opp["asleep"] else 0.0,
        1.0 if opp["paralyzed"] else 0.0,
        1.0 if opp["confused"] else 0.0,
    ]
    global_tensor = torch.tensor(global_feats, dtype=torch.float32)
    
    tokens = []
    
    def add_pokemon_token(pokemon: dict | None, role: int):
        if pokemon is None:
            tokens.append({
                "card_id": 0,
                "role": role,
                "hp": 0.0,
                "max_hp": 0.0,
                "energies": [0.0] * 12,
                "pre_evolutions_count": 0.0,
                "tools_count": 0.0,
                "appear_this_turn": 0.0,
                "count": 1.0,
            })
            return
            
        energy_counts = [0.0] * 12
        p_energies = pokemon.get("energies")
        if p_energies:
            for e in p_energies:
                if 0 <= int(e) < 12:
                    energy_counts[int(e)] += 1.0
                    
        tokens.append({
            "card_id": pokemon["id"],
            "role": role,
            "hp": float(pokemon["hp"]) / float(max(1, pokemon["maxHp"])),
            "max_hp": float(pokemon["maxHp"]) / 350.0,
            "energies": energy_counts,
            "pre_evolutions_count": float(len(pokemon["preEvolution"])) / 3.0 if pokemon.get("preEvolution") else 0.0,
            "tools_count": float(len(pokemon["tools"])) / 2.0 if pokemon.get("tools") else 0.0,
            "appear_this_turn": 1.0 if pokemon["appearThisTurn"] else 0.0,
            "count": 1.0,
        })

    # A. Active Pokemon
    add_pokemon_token(me["active"][0] if (me.get("active") and me["active"]) else None, ROLE_SELF_ACTIVE)
    add_pokemon_token(opp["active"][0] if (opp.get("active") and opp["active"]) else None, ROLE_OPP_ACTIVE)
    
    # B. Bench Pokemon
    for idx in range(5):
        p = me["bench"][idx] if idx < len(me["bench"]) else None
        add_pokemon_token(p, ROLE_SELF_BENCH)
    for idx in range(5):
        p = opp["bench"][idx] if idx < len(opp["bench"]) else None
        add_pokemon_token(p, ROLE_OPP_BENCH)
        
    # C. Stadium Card
    stadium = state.get("stadium")
    if stadium:
        std = stadium[0]
        tokens.append({
            "card_id": std["id"],
            "role": ROLE_STADIUM,
            "hp": 0.0,
            "max_hp": 0.0,
            "energies": [0.0] * 12,
            "pre_evolutions_count": 0.0,
            "tools_count": 0.0,
            "appear_this_turn": 0.0,
            "count": 1.0,
        })
        
    # D. Hand Cards
    hand = me.get("hand")
    if hand:
        for c in hand:
            tokens.append({
                "card_id": c["id"],
                "role": ROLE_SELF_HAND,
                "hp": 0.0,
                "max_hp": 0.0,
                "energies": [0.0] * 12,
                "pre_evolutions_count": 0.0,
                "tools_count": 0.0,
                "appear_this_turn": 0.0,
                "count": 1.0,
            })
            
    # E. Discard Pile
    def add_discard_tokens(discard_cards: list[dict], role: int):
        if not discard_cards:
            return
        counts = Counter(c["id"] for c in discard_cards)
        for cid, cnt in counts.items():
            tokens.append({
                "card_id": cid,
                "role": role,
                "hp": 0.0,
                "max_hp": 0.0,
                "energies": [0.0] * 12,
                "pre_evolutions_count": 0.0,
                "tools_count": 0.0,
                "appear_this_turn": 0.0,
                "count": float(cnt) / 30.0,
            })
            
    add_discard_tokens(me.get("discard"), ROLE_SELF_DISCARD)
    add_discard_tokens(opp.get("discard"), ROLE_OPP_DISCARD)
    
    # F. Looking Cards
    looking = state.get("looking")
    if looking:
        for c in looking:
            if c is not None:
                tokens.append({
                    "card_id": c["id"],
                    "role": ROLE_LOOKING,
                    "hp": 0.0,
                    "max_hp": 0.0,
                    "energies": [0.0] * 12,
                    "pre_evolutions_count": 0.0,
                    "tools_count": 0.0,
                    "appear_this_turn": 0.0,
                    "count": 1.0,
                })
                
    card_ids = []
    roles = []
    features_list = []
    masks = []
    
    for t in tokens:
        card_ids.append(t["card_id"])
        roles.append(t["role"])
        f_vec = [
            t["hp"],
            t["max_hp"],
            *t["energies"],
            t["pre_evolutions_count"],
            t["tools_count"],
            t["appear_this_turn"],
            t["count"],
        ]
        features_list.append(f_vec)
        masks.append(1.0)
        
    return {
        "global_features": global_tensor,
        "tokens_card_id": torch.tensor(card_ids, dtype=torch.long),
        "tokens_role": torch.tensor(roles, dtype=torch.long),
        "tokens_features": torch.tensor(features_list, dtype=torch.float32),
        "attention_mask": torch.tensor(masks, dtype=torch.float32),
    }

def evaluate_states_neural_batch_dict(states, root_player_idx, model, device) -> list[float]:
    if not states:
        return []
        
    scores = [0.0] * len(states)
    non_terminal_indices = []
    feats = []
    
    for idx, s in enumerate(states):
        if s is None:
            scores[idx] = -2.0
        elif s["result"] != -1:
            if s["result"] == root_player_idx:
                scores[idx] = 2.0
            elif s["result"] == 2:
                scores[idx] = 0.0
            else:
                scores[idx] = -2.0
        else:
            non_terminal_indices.append(idx)
            feats.append(featurize_state_dict(s))
            
    if not feats:
        return scores
        
    max_L = max(f["tokens_card_id"].shape[0] for f in feats)
    
    gf_list = []
    t_cid_list = []
    t_role_list = []
    t_feat_list = []
    mask_list = []
    
    for f in feats:
        L = f["tokens_card_id"].shape[0]
        padding_needed = max_L - L
        
        gf_list.append(f["global_features"])
        
        if padding_needed > 0:
            t_cid_list.append(torch.cat([f["tokens_card_id"], torch.zeros(padding_needed, dtype=torch.long)]))
            t_role_list.append(torch.cat([f["tokens_role"], torch.zeros(padding_needed, dtype=torch.long)]))
            t_feat_list.append(torch.cat([f["tokens_features"], torch.zeros(padding_needed, 18, dtype=torch.float32)], dim=0))
            mask_list.append(torch.cat([f["attention_mask"], torch.zeros(padding_needed, dtype=torch.float32)]))
        else:
            t_cid_list.append(f["tokens_card_id"])
            t_role_list.append(f["tokens_role"])
            t_feat_list.append(f["tokens_features"])
            mask_list.append(f["attention_mask"])
            
    gf = torch.stack(gf_list).to(device)
    t_cid = torch.stack(t_cid_list).to(device)
    t_role = torch.stack(t_role_list).to(device)
    t_feat = torch.stack(t_feat_list).to(device)
    mask = torch.stack(mask_list).to(device)
    
    with torch.no_grad():
        v_batch = model(gf, t_cid, t_role, t_feat, mask)
        v_list = v_batch.squeeze(-1).tolist() if v_batch.dim() > 1 else v_batch.tolist()
        if not isinstance(v_list, list):
            v_list = [v_list]
            
    for list_idx, original_idx in enumerate(non_terminal_indices):
        s = states[original_idx]
        v = v_list[list_idx]
        if s["yourIndex"] != root_player_idx:
            v = -v
        scores[original_idx] = v
        
    return scores

def beam_search_agent_batch_dict(obs_dict, starting_deck, N_determinizations=4, depth_turns=2, width=3) -> list[int]:
    select_info = obs_dict.get("select")
    if select_info is None:
        return starting_deck
    options = select_info["option"]
    
    if len(options) <= 1:
        return list(range(len(options)))
    if select_info["maxCount"] > 1:
        return list(range(min(select_info["maxCount"], len(options))))
        
    root_player_idx = obs_dict["current"]["yourIndex"]
    accumulated_scores = [0.0] * len(options)
    
    model = get_value_model()
    device = GLOBAL_DEVICE
    
    for _ in range(N_determinizations):
        y_deck, y_prize, o_deck, o_prize, o_hand, o_active = determinize_dict(obs_dict, starting_deck)
        
        root_state = fast_search_begin(
            obs_dict,
            y_deck, y_prize,
            o_deck, o_prize, o_hand, o_active,
            manual_coin=False
        )
        if root_state is None:
            continue
            
        beam = [([], root_state, 0, root_player_idx, 0.0)]
        max_plies = 25
        
        for ply_idx in range(max_plies):
            all_done = True
            for path, s_state, transitions, prev_player, _ in beam:
                sel = s_state["observation"]["select"]
                if sel is not None and transitions < 2 and s_state["observation"]["current"]["result"] == -1:
                    all_done = False
                    break
            if all_done:
                break
                
            to_evaluate_states = []
            to_evaluate_metadata = []
            candidates = []
            
            for path_idx, (path, s_state, transitions, prev_player, current_score) in enumerate(beam):
                sel = s_state["observation"]["select"]
                if sel is None or transitions >= 2 or s_state["observation"]["current"]["result"] != -1:
                    candidates.append((path, s_state, transitions, prev_player, current_score))
                    continue
                    
                current_player = s_state["observation"]["current"]["yourIndex"]
                next_transitions = transitions
                if current_player != prev_player:
                    next_transitions += 1
                    
                if next_transitions >= 2:
                    to_evaluate_states.append(s_state["observation"]["current"])
                    to_evaluate_metadata.append((path, s_state, next_transitions, current_player, path_idx, -1))
                    continue
                    
                if current_player == root_player_idx:
                    # MAX Node
                    if sel["maxCount"] > 1 or sel["minCount"] > 1:
                        num_to_select = sel["maxCount"] if sel["maxCount"] > 0 else sel["minCount"]
                        num_to_select = min(num_to_select, len(sel["option"]))
                        selection = list(range(num_to_select))
                        try:
                            next_state = fast_search_step(s_state["searchId"], selection)
                            if next_state is not None:
                                to_evaluate_states.append(next_state["observation"]["current"])
                                to_evaluate_metadata.append((path + [0], next_state, next_transitions, current_player, path_idx, -1))
                        except Exception:
                            pass
                    else:
                        for opt_idx in range(len(sel["option"])):
                            try:
                                next_state = fast_search_step(s_state["searchId"], [opt_idx])
                                if next_state is not None:
                                    to_evaluate_states.append(next_state["observation"]["current"])
                                    to_evaluate_metadata.append((path + [opt_idx], next_state, next_transitions, current_player, path_idx, opt_idx))
                            except Exception:
                                pass
                else:
                    # MIN Node
                    if sel["maxCount"] > 1 or sel["minCount"] > 1:
                        num_to_select = sel["maxCount"] if sel["maxCount"] > 0 else sel["minCount"]
                        num_to_select = min(num_to_select, len(sel["option"]))
                        selection = list(range(num_to_select))
                        try:
                            next_state = fast_search_step(s_state["searchId"], selection)
                            if next_state is not None:
                                to_evaluate_states.append(next_state["observation"]["current"])
                                to_evaluate_metadata.append((path + [0], next_state, next_transitions, current_player, path_idx, -1))
                        except Exception:
                            pass
                    else:
                        for opt_idx in range(len(sel["option"])):
                            try:
                                next_state = fast_search_step(s_state["searchId"], [opt_idx])
                                if next_state is not None:
                                    to_evaluate_states.append(next_state["observation"]["current"])
                                    to_evaluate_metadata.append((path + [opt_idx], next_state, next_transitions, current_player, path_idx, opt_idx))
                            except Exception:
                                pass
                                
            scores = evaluate_states_neural_batch_dict(to_evaluate_states, root_player_idx, model, device)
            
            opp_groups = {}
            for idx, score in enumerate(scores):
                path, next_state, next_transitions, current_player, path_idx, opt_idx = to_evaluate_metadata[idx]
                is_opp_single = (current_player != root_player_idx) and (opt_idx != -1)
                
                if is_opp_single:
                    if path_idx not in opp_groups:
                        opp_groups[path_idx] = []
                    opp_groups[path_idx].append((score, next_state, path, next_transitions, current_player))
                else:
                    candidates.append((path, next_state, next_transitions, current_player, score))
                    
            for path_idx, choices in opp_groups.items():
                choices.sort(key=lambda x: x[0])
                best_choice = choices[0]
                candidates.append((best_choice[2], best_choice[1], best_choice[3], best_choice[4], best_choice[0]))
                for choice in choices[1:]:
                    try: search_release(choice[1]["searchId"])
                    except Exception: pass
                        
            candidates.sort(key=lambda x: x[4], reverse=True)
            old_beam = beam
            beam = candidates[:width]
            
            active_ids = {b[1]["searchId"] for b in beam}
            for pb in old_beam:
                if pb[1]["searchId"] not in active_ids and pb[1]["searchId"] != root_state["searchId"]:
                    try: search_release(pb[1]["searchId"])
                    except Exception: pass
            for cand in candidates[width:]:
                if cand[1]["searchId"] not in active_ids:
                    try: search_release(cand[1]["searchId"])
                    except Exception: pass
                    
        for path, _, _, _, score in beam:
            if path:
                root_action = path[0]
                accumulated_scores[root_action] += score
                
        search_end()
        
    best_option = accumulated_scores.index(max(accumulated_scores))
    return [best_option]

# ==========================================
# SIMULATION WORKER PROCESS
# ==========================================
def worker_simulate_game(game_id: int) -> list[dict] | None:
    torch.set_num_threads(1)
    random.seed(os.getpid() + int(time.time() * 1000) % 100000 + game_id)
    
    deck0 = read_deck()
    deck1 = read_deck()
    
    obs_dict, start_data = battle_start(deck0, deck1)
    if start_data.battlePtr is None or start_data.battlePtr == 0:
        return None
        
    game_history = []
    step = 0
    MAX_STEPS = 300
    
    try:
        while obs_dict["current"]["result"] == -1:
            step += 1
            if step > MAX_STEPS:
                battle_finish()
                return None
                
            tensors = featurize_state_dict(obs_dict["current"])
            game_history.append((tensors, obs_dict["current"]["yourIndex"]))
            
            action = beam_search_agent_batch_dict(obs_dict, deck0, N_determinizations=4, depth_turns=2, width=3)
            obs_dict = battle_select(action)
            
        result = obs_dict["current"]["result"]
        battle_finish()
        
        game_states = []
        for tensors, decider_idx in game_history:
            if result == decider_idx:
                z_val = 1.0
            elif result in (0, 1):
                z_val = -1.0
            else:
                z_val = 0.0
                
            state_data = {
                "global_features": tensors["global_features"].tolist(),
                "tokens_card_id": tensors["tokens_card_id"].tolist(),
                "tokens_role": tensors["tokens_role"].tolist(),
                "tokens_features": tensors["tokens_features"].tolist(),
                "attention_mask": tensors["attention_mask"].tolist(),
                "Z": z_val,
                "game_id": game_id
            }
            game_states.append(state_data)
            
        return game_states
        
    except Exception:
        try: battle_finish()
        except Exception: pass
        return None

# ==========================================
# PARALLEL DATA COLLECTOR ENGINE
# ==========================================
def collect_selfplay_dataset(num_games=1000, num_workers=6, output_file="selfplay_dataset_lopunny_gen2.pt"):
    print("="*60)
    print(f" DEMARRAGE DU COLLECTEUR SELF-PLAY GEN 2 DICT-BASED (Workers: {num_workers}) ")
    print(f" Volume cible : {num_games} parties en N_det=4 ")
    print("="*60)
    
    start_time = time.perf_counter()
    
    pool = multiprocessing.Pool(processes=num_workers, maxtasksperchild=10)
    results = pool.imap_unordered(worker_simulate_game, range(num_games))
    
    dataset = []
    completed_games = 0
    discarded_games = 0
    total_states = 0
    
    for res in results:
        if res is not None:
            for state_data in res:
                tensor_dict = {
                    "global_features": torch.tensor(state_data["global_features"], dtype=torch.float32),
                    "tokens_card_id": torch.tensor(state_data["tokens_card_id"], dtype=torch.long),
                    "tokens_role": torch.tensor(state_data["tokens_role"], dtype=torch.long),
                    "tokens_features": torch.tensor(state_data["tokens_features"], dtype=torch.float32),
                    "attention_mask": torch.tensor(state_data["attention_mask"], dtype=torch.float32),
                    "Z": torch.tensor([state_data["Z"]], dtype=torch.float32),
                    "game_id": torch.tensor([state_data["game_id"]], dtype=torch.long)
                }
                dataset.append(tensor_dict)
            completed_games += 1
            total_states += len(res)
        else:
            discarded_games += 1
            
        elapsed = time.perf_counter() - start_time
        print(f"  Progres: {completed_games + discarded_games}/{num_games} | "
              f"Enregistrees: {completed_games} | Jetees: {discarded_games} | Tenseurs: {total_states} | "
              f"Temps: {elapsed:.1f}s", end="\r", flush=True)
              
    pool.close()
    pool.join()
    
    total_time = time.perf_counter() - start_time
    
    if dataset:
        torch.save(dataset, output_file)
        print(f"\n\nDataset Gen 2 sauvegarde avec succes dans: {output_file}")
        print(f"Temps total de calcul : {total_time/60.0:.2f} minutes")
    else:
        print("\n\nAucune donnee collectee.")
        
if __name__ == "__main__":
    multiprocessing.freeze_support()
    collect_selfplay_dataset(num_games=1000, num_workers=6, output_file="selfplay_dataset_lopunny_gen2.pt")
