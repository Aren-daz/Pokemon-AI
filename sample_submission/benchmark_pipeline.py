import os
import sys
import time
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import numpy as np
import random

# Import model & train components
from model import ValueNetwork
from train import collate_fn

def benchmark_dataloader(dataset, batch_size, num_workers, pre_convert=False, persistent_workers=False):
    # Prepare data
    data = dataset.copy()
    
    if pre_convert:
        # Cause 1: Pre-convert to tensors once
        for item in data:
            item["tokens_card_id"] = torch.as_tensor(item["tokens_card_id"], dtype=torch.long)
            item["tokens_role"] = torch.as_tensor(item["tokens_role"], dtype=torch.long)
            item["tokens_features"] = torch.as_tensor(item["tokens_features"], dtype=torch.float32)
            item["global_features"] = torch.as_tensor(item["global_features"], dtype=torch.float32)
            item["attention_mask"] = torch.as_tensor(item["attention_mask"], dtype=torch.float32)
            item["Z"] = torch.as_tensor(item["Z"], dtype=torch.float32)
            item["game_id"] = torch.as_tensor(item["game_id"], dtype=torch.long)
            
    # Setup Dataloader
    loader = DataLoader(
        data,
        batch_size=batch_size,
        shuffle=True,
        collate_fn=collate_fn,
        num_workers=num_workers,
        persistent_workers=persistent_workers,
        pin_memory=False
    )
    
    # Measure iteration speed
    start_time = time.perf_counter()
    num_batches = 0
    max_batches = 100
    
    # Warm up first batch
    iterator = iter(loader)
    try:
        next(iterator)
    except StopIteration:
        pass
        
    start_time = time.perf_counter()
    for i in range(max_batches):
        try:
            batch = next(iterator)
            num_batches += 1
        except StopIteration:
            break
            
    elapsed = time.perf_counter() - start_time
    time_per_batch = elapsed / num_batches if num_batches > 0 else 0
    return time_per_batch

def benchmark_model_steps(num_threads, batch_size=512):
    torch.set_num_threads(num_threads)
    device = torch.device("cpu")
    
    # Mock batch
    gf = torch.randn(batch_size, 22, device=device)
    t_cid = torch.randint(0, 1000, (batch_size, 30), dtype=torch.long, device=device)
    t_role = torch.randint(0, 5, (batch_size, 30), dtype=torch.long, device=device)
    t_feat = torch.randn(batch_size, 30, 18, device=device)
    mask = torch.ones(batch_size, 30, device=device)
    z = torch.randn(batch_size, device=device)
    
    model = ValueNetwork().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.MSELoss()
    
    # Warm up
    pred = model(gf, t_cid, t_role, t_feat, mask)
    loss = criterion(pred, z)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    
    # Measure
    start_time = time.perf_counter()
    steps = 30
    for _ in range(steps):
        optimizer.zero_grad()
        pred = model(gf, t_cid, t_role, t_feat, mask)
        loss = criterion(pred, z)
        loss.backward()
        optimizer.step()
        
    elapsed = time.perf_counter() - start_time
    time_per_step = elapsed / steps
    return time_per_step

def main():
    print("="*60)
    print(" PIPELINE BENCHMARK UTILITY ")
    print("="*60)
    
    dataset_path = "selfplay_dataset.pt"
    if not os.path.exists(dataset_path):
        print(f"Dataset not found at {dataset_path}")
        return
        
    print("Loading dataset (takes a few seconds)...")
    dataset = torch.load(dataset_path)
    # Subset of dataset to keep it fast
    subset = dataset[:10000]
    print(f"Loaded subset of {len(subset)} states for benchmarking.")
    
    # ----------------------------------------------------
    # 1. DATALOADER BENCHMARK
    # ----------------------------------------------------
    print("\n--- 1. DataLoader & Conversion Benchmark ---")
    
    # Original Config (No pre-conversion, num_workers=0, batch=256)
    print("Testing Original Config (No pre-convert, num_workers=0, batch=256)...")
    t0 = benchmark_dataloader(subset, batch_size=256, num_workers=0, pre_convert=False, persistent_workers=False)
    print(f"  >>> Time per batch (Original): {t0:.4f}s")
    
    # Cause 1 Optimized (Pre-convert, num_workers=0, batch=256)
    print("Testing Cause 1 (Pre-convert, num_workers=0, batch=256)...")
    t1 = benchmark_dataloader(subset, batch_size=256, num_workers=0, pre_convert=True, persistent_workers=False)
    print(f"  >>> Time per batch (Cause 1 only): {t1:.4f}s (Speedup: {t0/t1:.2f}x)")
    
    # Cause 1 + 2 Optimized (Pre-convert, num_workers=4, batch=256)
    print("Testing Cause 1 + 2 (Pre-convert, num_workers=4, batch=256)...")
    try:
        t2 = benchmark_dataloader(subset, batch_size=256, num_workers=4, pre_convert=True, persistent_workers=True)
        print(f"  >>> Time per batch (Cause 1 + 2, NW=4): {t2:.4f}s (Speedup vs Original: {t0/t2:.2f}x)")
    except Exception as e:
        print(f"  >>> num_workers=4 failed: {e}")
        t2 = None
        
    # Cause 1 + 2 Optimized with num_workers=2
    print("Testing Cause 1 + 2 (Pre-convert, num_workers=2, batch=256)...")
    try:
        t2_nw2 = benchmark_dataloader(subset, batch_size=256, num_workers=2, pre_convert=True, persistent_workers=True)
        print(f"  >>> Time per batch (Cause 1 + 2, NW=2): {t2_nw2:.4f}s (Speedup vs Original: {t0/t2_nw2:.2f}x)")
    except Exception as e:
        print(f"  >>> num_workers=2 failed: {e}")
        t2_nw2 = None
        
    # Bonus Optimized (Pre-convert, num_workers=2/4, batch=512)
    print("Testing Bonus Config (Pre-convert, num_workers=4, batch=512)...")
    try:
        t3 = benchmark_dataloader(subset, batch_size=512, num_workers=4, pre_convert=True, persistent_workers=True)
        print(f"  >>> Time per batch (Batch=512, NW=4): {t3:.4f}s")
    except Exception as e:
        print(f"  >>> num_workers=4, batch=512 failed: {e}")
        t3 = None

    # ----------------------------------------------------
    # 2. CPU THREADS BENCHMARK
    # ----------------------------------------------------
    print("\n--- 2. CPU Threads Optimization (Model steps) ---")
    for threads in [6, 8, 16]:
        print(f"Testing PyTorch set_num_threads({threads}) with batch=512...")
        t_step = benchmark_model_steps(threads, batch_size=512)
        print(f"  >>> Time per model step: {t_step:.4f}s")
        
    print("="*60)

if __name__ == "__main__":
    # Windows multiprocessing protection
    import multiprocessing
    multiprocessing.freeze_support()
    main()
