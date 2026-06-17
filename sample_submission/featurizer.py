import torch
import torch.nn as nn
from collections import Counter
from cg.api import (
    State,
    PlayerState,
    Pokemon,
    Card,
    all_card_data,
    CardType,
    EnergyType
)

# ==========================================
# CARD ROLE / POSITION CONSTANTS
# ==========================================
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

def featurize_state(state: State) -> dict[str, torch.Tensor]:
    """Featurizes a State object into variable-length PyTorch tensors relative to yourIndex.
    
    Static card attributes (retreatCost, ex, stage, weakness, etc.) are NOT explicitly 
    included in the token features. They must be learned solely by the network's 
    embedding layer for the card_id.
    
    Returns:
        dict: Tensors containing:
            - 'global_features': FloatTensor of shape (22,)
            - 'tokens_card_id': LongTensor of shape (L,) containing nominal card IDs
            - 'tokens_role': LongTensor of shape (L,) containing role zone IDs
            - 'tokens_features': FloatTensor of shape (L, 18) containing dynamic card features
            - 'attention_mask': FloatTensor of shape (L,) filled with 1.0
    """
    if state is None:
        # Return empty tensors of length 0 if state is None
        return {
            "global_features": torch.zeros(22, dtype=torch.float32),
            "tokens_card_id": torch.zeros(0, dtype=torch.long),
            "tokens_role": torch.zeros(0, dtype=torch.long),
            "tokens_features": torch.zeros(0, 18, dtype=torch.float32),
            "attention_mask": torch.zeros(0, dtype=torch.float32),
        }
        
    your_idx = state.yourIndex
    opp_idx = 1 - your_idx
    
    me: PlayerState = state.players[your_idx]
    opp: PlayerState = state.players[opp_idx]
    
    # ----------------------------------------------------
    # 1. GLOBAL FEATURES VECTOR (Perspective-Relative)
    # ----------------------------------------------------
    global_feats = [
        float(state.turn) / 50.0,
        float(state.turnActionCount) / 10.0,
        1.0 if state.supporterPlayed else 0.0,
        1.0 if state.stadiumPlayed else 0.0,
        1.0 if state.energyAttached else 0.0,
        1.0 if state.retreated else 0.0,
        
        # Self counters
        float(me.deckCount) / 60.0,
        float(me.handCount) / 60.0,
        float(len(me.prize)) / 6.0,
        
        # Opponent counters
        float(opp.deckCount) / 60.0,
        float(opp.handCount) / 60.0,
        float(len(opp.prize)) / 6.0,
        
        # Self Active Status
        1.0 if me.poisoned else 0.0,
        1.0 if me.burned else 0.0,
        1.0 if me.asleep else 0.0,
        1.0 if me.paralyzed else 0.0,
        1.0 if me.confused else 0.0,
        
        # Opponent Active Status
        1.0 if opp.poisoned else 0.0,
        1.0 if opp.burned else 0.0,
        1.0 if opp.asleep else 0.0,
        1.0 if opp.paralyzed else 0.0,
        1.0 if opp.confused else 0.0,
    ]
    
    global_tensor = torch.tensor(global_feats, dtype=torch.float32)
    
    # ----------------------------------------------------
    # 2. TOKENS GENERATION
    # ----------------------------------------------------
    tokens = []
    
    def add_pokemon_token(pokemon: Pokemon | None, role: int):
        """Constructs a token representation of a Pokemon on the board."""
        if pokemon is None:
            # Face-down Active / Placeholder
            tokens.append({
                "card_id": 0, # Masked / Unknown
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
            
        # Map energy list to a count vector of shape 12 (EnergyType enum size)
        energy_counts = [0.0] * 12
        if pokemon.energies:
            for e in pokemon.energies:
                if 0 <= int(e) < 12:
                    energy_counts[int(e)] += 1.0
                    
        tokens.append({
            "card_id": pokemon.id,
            "role": role,
            "hp": float(pokemon.hp) / float(max(1, pokemon.maxHp)),
            "max_hp": float(pokemon.maxHp) / 350.0,
            "energies": energy_counts,
            "pre_evolutions_count": float(len(pokemon.preEvolution)) / 3.0 if pokemon.preEvolution else 0.0,
            "tools_count": float(len(pokemon.tools)) / 2.0 if pokemon.tools else 0.0,
            "appear_this_turn": 1.0 if pokemon.appearThisTurn else 0.0,
            "count": 1.0,
        })

    # A. Active Pokemon (exactly 1 token per player)
    add_pokemon_token(me.active[0] if (me.active and me.active[0]) else None, ROLE_SELF_ACTIVE)
    add_pokemon_token(opp.active[0] if (opp.active and opp.active[0]) else None, ROLE_OPP_ACTIVE)
    
    # B. Bench Pokemon (exactly 5 slots per player, padded to benchMax if empty)
    for idx in range(5):
        p = me.bench[idx] if idx < len(me.bench) else None
        add_pokemon_token(p, ROLE_SELF_BENCH)
    for idx in range(5):
        p = opp.bench[idx] if idx < len(opp.bench) else None
        add_pokemon_token(p, ROLE_OPP_BENCH)
        
    # C. Stadium Card (0 or 1 token)
    if state.stadium:
        std = state.stadium[0]
        tokens.append({
            "card_id": std.id,
            "role": ROLE_STADIUM,
            "hp": 0.0,
            "max_hp": 0.0,
            "energies": [0.0] * 12,
            "pre_evolutions_count": 0.0,
            "tools_count": 0.0,
            "appear_this_turn": 0.0,
            "count": 1.0,
        })
        
    # D. Hand Cards (Variable length, own hand only)
    if me.hand:
        for c in me.hand:
            tokens.append({
                "card_id": c.id,
                "role": ROLE_SELF_HAND,
                "hp": 0.0,
                "max_hp": 0.0,
                "energies": [0.0] * 12,
                "pre_evolutions_count": 0.0,
                "tools_count": 0.0,
                "appear_this_turn": 0.0,
                "count": 1.0,
            })
            
    # E. Discard Pile (Group unique card IDs to avoid sequence explosion)
    def add_discard_tokens(discard_cards: list[Card], role: int):
        if not discard_cards:
            return
        counts = Counter(c.id for c in discard_cards)
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
                "count": float(cnt) / 30.0, # Normalized
            })
            
    add_discard_tokens(me.discard, ROLE_SELF_DISCARD)
    add_discard_tokens(opp.discard, ROLE_OPP_DISCARD)
    
    # F. Looking Cards (Variable length, if currently resolving lookup effects)
    if state.looking:
        for c in state.looking:
            if c is not None:
                tokens.append({
                    "card_id": c.id,
                    "role": ROLE_LOOKING,
                    "hp": 0.0,
                    "max_hp": 0.0,
                    "energies": [0.0] * 12,
                    "pre_evolutions_count": 0.0,
                    "tools_count": 0.0,
                    "appear_this_turn": 0.0,
                    "count": 1.0,
                })
                
    # ----------------------------------------------------
    # 3. TENSOR BUILD (NO PADDING - VARIABLE LENGTH L)
    # ----------------------------------------------------
    card_ids = []
    roles = []
    features_list = []
    masks = []
    
    for t in tokens:
        card_ids.append(t["card_id"])
        roles.append(t["role"])
        
        # Build dynamic numerical feature vector (Size: 18)
        f_vec = [
            t["hp"],
            t["max_hp"],
            *t["energies"], # 12 elements
            t["pre_evolutions_count"],
            t["tools_count"],
            t["appear_this_turn"],
            t["count"],
        ]
        features_list.append(f_vec)
        masks.append(1.0)
        
    return {
        "global_features": global_tensor, # (22,)
        "tokens_card_id": torch.tensor(card_ids, dtype=torch.long), # (L,)
        "tokens_role": torch.tensor(roles, dtype=torch.long), # (L,)
        "tokens_features": torch.tensor(features_list, dtype=torch.float32), # (L, 18)
        "attention_mask": torch.tensor(masks, dtype=torch.float32), # (L,)
    }
