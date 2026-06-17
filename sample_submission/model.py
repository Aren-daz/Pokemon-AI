import torch
import torch.nn as nn

class ValueNetwork(nn.Module):
    """Transformer Encoder network evaluating board states in Pokémon TCG."""
    def __init__(self, vocab_size=1300, d_model=64, nhead=4, num_layers=3, dim_feedforward=128, dropout=0.1):
        super().__init__()
        # Learned embeddings
        self.card_emb = nn.Embedding(vocab_size, 32, padding_idx=0)
        self.role_emb = nn.Embedding(10, 8, padding_idx=0)
        
        # Token feature projection layer
        # Card ID Embedding (32) + Role Embedding (8) + Dynamic Features (18) = 58 dims
        self.project = nn.Linear(58, d_model)
        
        # Transformer encoder layers (processes relations between entities on the board)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            batch_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        
        # MLP value head:
        # Pooled Transformer sequence representation (64) + Global Features (22) = 86 dims
        self.mlp = nn.Sequential(
            nn.Linear(d_model + 22, 32),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(32, 1),
            nn.Tanh() # Restricts V(s) to [-1, 1] representing win/loss expectation
        )
        
    def forward(self, global_features, tokens_card_id, tokens_role, tokens_features, attention_mask):
        # 1. Embeddings
        c_emb = self.card_emb(tokens_card_id) # Shape: (B, L, 32)
        r_emb = self.role_emb(tokens_role) # Shape: (B, L, 8)
        
        # 2. Concat & project to d_model
        x = torch.cat([c_emb, r_emb, tokens_features], dim=-1) # Shape: (B, L, 58)
        x = self.project(x) # Shape: (B, L, 64)
        
        # 3. Transformer attention masking
        # In PyTorch TransformerEncoder, key_padding_mask should be True for keys to ignore.
        # Since attention_mask is 1.0 for valid and 0.0 for padding, key_padding_mask = (attention_mask == 0.0)
        key_padding_mask = (attention_mask == 0.0)
        
        # 4. Transformer forward pass
        out = self.transformer(x, src_key_padding_mask=key_padding_mask) # Shape: (B, L, 64)
        
        # 5. Masked Mean Pooling
        mask_expanded = attention_mask.unsqueeze(-1) # Shape: (B, L, 1)
        masked_out = out * mask_expanded
        sum_out = torch.sum(masked_out, dim=1) # Shape: (B, 64)
        count_out = torch.sum(attention_mask, dim=1, keepdim=True).clamp(min=1.0) # Shape: (B, 1)
        pooled = sum_out / count_out # Shape: (B, 64)
        
        # 6. Injection of global features (Concatenation at final pooling layer)
        # Justification: Prepended CLS token requires projecting global_features to d_model and
        # expanding sequence length, adding compute. Final concatenation is structurally simpler,
        # separates global game variables from token self-attention, and runs faster.
        joint = torch.cat([pooled, global_features], dim=-1) # Shape: (B, 86)
        
        # 7. MLP prediction
        val = self.mlp(joint).squeeze(-1) # Shape: (B,)
        return val
