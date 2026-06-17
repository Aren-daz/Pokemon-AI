import time
from collect_selfplay import collect_selfplay_dataset

def main():
    for w in [4, 6, 8, 12]:
        print(f"\n--- Test avec {w} workers ---")
        start = time.perf_counter()
        collect_selfplay_dataset(num_games=100, num_workers=w, output_file="temp.pt")
        elapsed = time.perf_counter() - start
        rate = 100.0 / elapsed
        print(f"Workers: {w} | Temps: {elapsed:.2f}s | Débit: {rate:.2f} games/sec")

if __name__ == "__main__":
    main()
