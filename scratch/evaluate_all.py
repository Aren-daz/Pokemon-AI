import os
import sys
import random
import time
import math
import multiprocessing
import io
import torch

sys.path.append("sample_submission")
from cg.game import battle_start, battle_select, battle_finish
from cg.api import to_observation_class, SelectContext, OptionType
import main
from main import (
    beam_search_agent,
    read_deck_csv,
    get_b3_records
)

# ----------------------------------------------------
# 1. QUALITATIVE PLAY-BY-PLAY RUNNER
# ----------------------------------------------------
def run_qualitative_game(game_id):
    """Run a single mirror game with verbose logging enabled and return logs."""
    # Force single-threaded execution during qualitative check for standard comparison
    torch.set_num_threads(4)
    
    # Enable logging globally in main
    main.ENABLE_LOGGING = True
    
    # Capture all prints to a StringIO buffer
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    deck0 = read_deck_csv()
    deck1 = read_deck_csv()
    
    print(f"# PARTIE DE DÉMONSTRATION {game_id}\n")
    print("Démarrage du combat Lopunny vs Lopunny...")
    
    obs_dict, start_data = battle_start(deck0, deck1)
    if start_data.battlePtr is None or start_data.battlePtr == 0:
        sys.stdout = old_stdout
        return f"Erreur au démarrage de la partie {game_id}."
        
    obs = to_observation_class(obs_dict)
    step = 0
    
    while obs.current.result == -1:
        step += 1
        # Neural vs Neural mirror play using the submission agent wrapper with print logs
        action = main.agent(obs_dict)
        obs_dict = battle_select(action)
        obs = to_observation_class(obs_dict)
        
    winner = obs.current.result
    print(f"\nPartie {game_id} terminée en {step} étapes. Vainqueur : Joueur {winner}")
    battle_finish()
    
    log_content = sys.stdout.getvalue()
    sys.stdout = old_stdout
    main.ENABLE_LOGGING = False
    
    return log_content

# ----------------------------------------------------
# 2. PARALLEL TOURNAMENT WORKER
# ----------------------------------------------------
def run_tournament_game(args):
    """Worker process running a single tournament game."""
    # Crucial: force single-thread inside worker to prevent CPU cores thrashing
    torch.set_num_threads(1)
    
    game_id, p1_neural = args
    deck0 = read_deck_csv()
    deck1 = read_deck_csv()
    
    # Disable logs inside worker processes
    main.ENABLE_LOGGING = False
    
    # Clear any leftover records
    _ = get_b3_records()
    
    try:
        obs_dict, start_data = battle_start(deck0, deck1)
        if start_data.battlePtr is None or start_data.battlePtr == 0:
            return {
                "game_id": game_id,
                "winner": -1,
                "neural_won": False,
                "draw": False,
                "steps": 0,
                "error": True,
                "b3_records": []
            }
            
        obs = to_observation_class(obs_dict)
        step = 0
        
        while obs.current.result == -1:
            step += 1
            your_idx = obs.current.yourIndex
            
            # Identify who is playing this turn
            if your_idx == 0:
                mode = "neural" if p1_neural else "heuristic"
                active_deck = deck0
            else:
                mode = "heuristic" if p1_neural else "neural"
                active_deck = deck1
                
            action = beam_search_agent(
                obs_dict, 
                starting_deck=active_deck, 
                N_determinizations=4, 
                depth_turns=2, 
                width=3, 
                evaluation_mode=mode
            )
            obs_dict = battle_select(action)
            obs = to_observation_class(obs_dict)
            
        winner = obs.current.result
        battle_finish()
        
        neural_won = False
        if winner == 0:
            neural_won = p1_neural
        elif winner == 1:
            neural_won = not p1_neural
            
        # Collect process-local B3 records
        b3_records = get_b3_records()
        
        return {
            "game_id": game_id,
            "winner": winner,
            "neural_won": neural_won,
            "draw": (winner == 2),
            "steps": step,
            "error": False,
            "b3_records": b3_records
        }
    except Exception as e:
        try:
            battle_finish()
        except Exception:
            pass
        return {
            "game_id": game_id,
            "winner": -1,
            "neural_won": False,
            "draw": False,
            "steps": 0,
            "error": True,
            "b3_records": [],
            "error_msg": str(e)
        }

# ----------------------------------------------------
# 3. MAIN EVALUATION CONTROLLER
# ----------------------------------------------------
def main_run():
    # Seeds for reproducibility
    random.seed(42)
    torch.manual_seed(42)
    
    print("="*60)
    print(" DÉMARRAGE DE L'ÉVALUATION COMPLÈTE ÉTAPE 1 ")
    print("="*60)
    
    # ----------------------------------------------------
    # PHASE A : RECUEIL DE L'EXAMEN QUALITATIF (5 Parties)
    # ----------------------------------------------------
    print("\n[PHASE A] Génération des 5 parties de démonstration qualitative...")
    qualitative_file = "scratch/qualitative_logs.md"
    
    with open(qualitative_file, "w", encoding="utf-8") as f:
        f.write("# EXAMEN QUALITATIF : LOGS DE DÉROULEMENT LOPUNNY NEURAL\n\n")
        f.write("Ce fichier contient le déroulé complet de 5 parties jouées par l'agent neural. ")
        f.write("L'objectif est d'analyser le séquencement des cartes de setup (Lillie's, Poffin, Ultra Ball) ")
        f.write("et de vérifier l'absence de myopie.\n\n")
        
        for g_id in range(1, 6):
            print(f"  - Génération de la partie {g_id}/5...")
            logs = run_qualitative_game(g_id)
            f.write(f"## PARTIE {g_id}\n\n")
            f.write("```text\n")
            f.write(logs)
            f.write("\n```\n\n")
            f.write("---\n\n")
            
    print(f">>> Logs qualitatifs enregistrés avec succès dans : {qualitative_file}")
    
    # ----------------------------------------------------
    # PHASE B : TOURNOI PARALLÈLE (400 Parties)
    # ----------------------------------------------------
    print("\n[PHASE B] Lancement du tournoi de 400 parties miroir en parallèle...")
    
    # 200 parties P1 Neural (True), 200 parties P1 Heuristique (False)
    args_list = []
    for i in range(200):
        args_list.append((i, True))
    for i in range(200):
        args_list.append((200 + i, False))
        
    # Shuffle args list to mix configurations
    random.shuffle(args_list)
    
    num_workers = min(multiprocessing.cpu_count(), 8)
    print(f"  - Utilisation de {num_workers} processus CPU en parallèle.")
    
    completed = 0
    neural_wins = 0
    heuristic_wins = 0
    draws = 0
    errors = 0
    
    b3_all_records = []
    
    start_time = time.perf_counter()
    
    # Start pool with single-thread initializer
    with multiprocessing.Pool(processes=num_workers) as pool:
        for res in pool.imap_unordered(run_tournament_game, args_list):
            completed += 1
            
            if res["error"]:
                errors += 1
            elif res["draw"]:
                draws += 1
            elif res["neural_won"]:
                neural_wins += 1
            else:
                heuristic_wins += 1
                
            b3_all_records.extend(res["b3_records"])
            
            # Print periodic progress
            if completed % 10 == 0 or completed == 400:
                pct = completed / 400.0 * 100.0
                cur_winrate = (neural_wins / completed * 100.0) if completed > 0 else 0.0
                elapsed_min = (time.perf_counter() - start_time) / 60.0
                print(f"  Progress: {completed:3d}/400 ({pct:5.1f}%) | Neural Wins: {neural_wins:3d} | Heuristic Wins: {heuristic_wins:3d} | Draws: {draws} | Winrate: {cur_winrate:6.2f}% | Temps écoulé: {elapsed_min:.2f} min")
                
    elapsed_total = time.perf_counter() - start_time
    print(f"\n>>> Tournoi terminé en {elapsed_total/60.0:.2f} minutes.")
    
    # ----------------------------------------------------
    # PHASE C : ANALYSE STATISTIQUE & COMPENSATOIRE
    # ----------------------------------------------------
    valid_games = neural_wins + heuristic_wins
    if valid_games > 0:
        winrate = neural_wins / valid_games
        se = math.sqrt(winrate * (1 - winrate) / valid_games)
        ci_lower = winrate - 1.96 * se
        ci_upper = winrate + 1.96 * se
        
        # One-sided z-test vs 50% Null Hypothesis
        z = (winrate - 0.5) / (0.5 / math.sqrt(valid_games))
        p_val = 0.5 * (1.0 - math.erf(z / math.sqrt(2.0)))
    else:
        winrate = 0.0
        se = 0.0
        ci_lower, ci_upper = 0.0, 0.0
        p_val = 1.0
        
    print("\n" + "="*60)
    print(" MESURE 1 : RÉSULTATS DU TOURNOI ")
    print("="*60)
    print(f"Total parties valides : {valid_games}")
    print(f"Victoires Agent Neural : {neural_wins} ({winrate*100.0:.2f}%)")
    print(f"Victoires Agent Heuristique : {heuristic_wins} ({(1-winrate)*100.0:.2f}%)")
    print(f"Matchs nuls / Draws : {draws}")
    print(f"Erreurs de simulation : {errors}")
    print(f"Winrate Neural : {winrate*100.0:.2f}% (95% CI: [{ci_lower*100.0:.2f}%, {ci_upper*100.0:.2f}%])")
    print(f"Erreur d'intervalle : ±{1.96*se*100.0:.2f}%")
    print(f"Test statistique : z = {z:.4f} | p-value = {p_val:.6f}")
    
    tourney_success = (winrate >= 0.55) and (p_val < 0.025)
    print(f"Critère de succès winrate >= 55.0% et p < 0.025 : {'SUCCÈS' if tourney_success else 'ÉCHEC'}")
    print("="*60)
    
    # B3 Threat Compensation analysis
    danger_counts = {"high_danger": 0, "low_danger": 0, "medium_danger": 0}
    static_retreats = {"high_danger": 0, "low_danger": 0, "medium_danger": 0}
    search_retreats = {"high_danger": 0, "low_danger": 0, "medium_danger": 0}
    
    for r in b3_all_records:
        ctx = r["danger_context"]
        danger_counts[ctx] += 1
        if r["static_choice_is_retreat"]:
            static_retreats[ctx] += 1
        if r["search_choice_is_retreat"]:
            search_retreats[ctx] += 1
            
    print("\n" + "="*60)
    print(" MESURE 2 : ANALYSE DE LA COMPENSATION CONTEXTUELLE B3 ")
    print("="*60)
    print(f"| {'Contexte de Danger':<18} | {'N':<6} | {'% Retraite Statique':<21} | {'% Retraite Recherche':<22} | {'Différence':<10} |")
    print(f"|{'-'*20}|{'-'*8}|{'-'*23}|{'-'*24}|{'-'*12}|")
    
    for ctx in ["high_danger", "low_danger"]:
        n = danger_counts[ctx]
        static_rate = (static_retreats[ctx] / n * 100.0) if n > 0 else 0.0
        search_rate = (search_retreats[ctx] / n * 100.0) if n > 0 else 0.0
        diff = search_rate - static_rate
        ctx_title = "DANGER RÉEL" if ctx == "high_danger" else "DANGER FAIBLE"
        print(f"| {ctx_title:<18} | {n:<6d} | {static_rate:<20.2f}% | {search_rate:<21.2f}% | {diff:+.2f}% |")
        
    print("="*60)
    
    # Check threat compensation success criteria:
    # 1. Search retreat rate should be significantly higher than static in high danger (e.g. diff > 30%)
    # 2. Search retreat rate in low danger should be low and similar to static (e.g. diff < 15%)
    high_danger_diff = (search_retreats["high_danger"] / danger_counts["high_danger"] - static_retreats["high_danger"] / danger_counts["high_danger"]) * 100.0 if danger_counts["high_danger"] > 0 else 0.0
    low_danger_diff = (search_retreats["low_danger"] / danger_counts["low_danger"] - static_retreats["low_danger"] / danger_counts["low_danger"]) * 100.0 if danger_counts["low_danger"] > 0 else 0.0
    
    comp_success = (high_danger_diff >= 30.0) and (low_danger_diff <= 15.0)
    print(f"Vérification de la compensation sélective :")
    print(f"  - Danger réel : Augmentation de la prudence : {high_danger_diff:+.1f}% (Attendu >= +30.0%)")
    print(f"  - Danger faible : Stabilité de l'agressivité : {low_danger_diff:+.1f}% (Attendu <= +15.0%)")
    print(f"Critère de compensation contextuelle validé : {'SUCCÈS' if comp_success else 'ÉCHEC'}")
    print("="*60)

    # ----------------------------------------------------
    # UPDATE WALKTHROUGH.MD
    # ----------------------------------------------------
    walkthrough_file = "walkthrough.md"
    if not os.path.exists(walkthrough_file):
        walkthrough_file = os.path.join("C:/Users/adamt/.gemini/antigravity/brain/8a040cdd-6fc2-4393-9208-7c74c8421b6a", walkthrough_file)
        
    print(f"\nMise à jour de walkthrough.md...")
    
    # Create or append walkthrough markdown content
    with open(walkthrough_file, "w", encoding="utf-8") as f_walk:
        f_walk.write("# Walkthrough Étape 1 — Rapport d'Évaluation de la Recherche Neurale\n\n")
        f_walk.write("## 1. Résultats du Tournoi Miroir (400 Parties)\n")
        f_walk.write(f"- **Volume** : 400 parties (200 P1 / 200 P2)\n")
        f_walk.write(f"- **Victoires Neural Agent (PIMC + Model B)** : {neural_wins} ({winrate*100.0:.2f}%)\n")
        f_walk.write(f"- **Victoires Heuristique (PIMC + evaluate_state)** : {heuristic_wins} ({(1-winrate)*100.0:.2f}%)\n")
        f_walk.write(f"- **Taux de Victoire** : **{winrate*100.0:.2f}%** (CI à 95% : **[{ci_lower*100.0:.2f}%, {ci_upper*100.0:.2f}%]**)\n")
        f_walk.write(f"- **Intervalle d'erreur** : ±{1.96*se*100.0:.2f}%\n")
        f_walk.write(f"- **Signification statistique** : z = {z:.4f}, p-value = {p_val:.6f} (seuil p < 0.025)\n")
        f_walk.write(f"- **Verdict** : **{'RÉUSSI' if tourney_success else 'ÉCHEC'}**\n\n")
        
        f_walk.write("## 2. Analyse de la Compensation Contextuelle B3\n")
        f_walk.write("| Contexte de Danger | N | % Retraite Statique | % Retraite Recherche | Différence |\n")
        f_walk.write("|---|---|---|---|---|\n")
        for ctx in ["high_danger", "low_danger"]:
            n = danger_counts[ctx]
            static_rate = (static_retreats[ctx] / n * 100.0) if n > 0 else 0.0
            search_rate = (search_retreats[ctx] / n * 100.0) if n > 0 else 0.0
            diff = search_rate - static_rate
            ctx_title = "Danger Réel (Prizes Opp <= 3)" if ctx == "high_danger" else "Danger Faible (Prizes Opp == 6)"
            f_walk.write(f"| {ctx_title} | {n} | {static_rate:.2f}% | {search_rate:.2f}% | {diff:+.2f}% |\n")
        f_walk.write("\n")
        f_walk.write(f"- **Ajustement en danger réel** : {high_danger_diff:+.1f}% (Cible >= +30.0%)\n")
        f_walk.write(f"- **Stabilité en danger faible** : {low_danger_diff:+.1f}% (Cible <= +15.0%)\n")
        f_walk.write(f"- **Verdict** : **{'RÉUSSI' if comp_success else 'ÉCHEC'}**\n\n")
        
        f_walk.write("## 3. Examen Qualitatif Anti-Myopie\n")
        f_walk.write("Les déroulés complets de 5 parties ont été enregistrés dans [qualitative_logs.md](file:///c:/Users/adamt/Desktop/Code/Developpement%20IA/pokemon-tcg-ai-battle/scratch/qualitative_logs.md).\n")
        f_walk.write("L'utilisateur peut inspecter ces déroulés pour s'assurer que l'agent joue ses cartes de setup (Lillie's, Poffin, Ultra Ball) dans le bon ordre.\n")
        
    print("walkthrough.md mis à jour.")

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main_run()
