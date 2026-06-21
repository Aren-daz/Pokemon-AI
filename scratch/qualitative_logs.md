# EXAMEN QUALITATIF : LOGS DE DÉROULEMENT LOPUNNY NEURAL

Ce fichier contient le déroulé complet de 5 parties jouées par l'agent neural. L'objectif est d'analyser le séquencement des cartes de setup (Lillie's, Poffin, Ultra Ball) et de vérifier l'absence de myopie.

## PARTIE 1

```text
# PARTIE DE DÉMONSTRATION 1

Démarrage du combat Lopunny vs Lopunny...

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 60 | Ma Main: 0 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 60 | Opp Main: 0 | Opp Banc: 0 | Prizes: 0
==================================================
[NEURAL AGENT] Loading value network weights from sample_submission\value_network_lopunny_weighted_best.pth...
[DECISION] Action choisie -> Index [0]: YES

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 53 | Ma Main: 7 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 53 | Opp Main: 7 | Opp Banc: 0 | Prizes: 0
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 53 | Ma Main: 7 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 47 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
==================================================
[DECISION] Action choisie -> Index [1]: NUMBER (Number: 1)

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 46 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 46 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 46 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 44 | Ma Main: 6 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [3]: ATTACH

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 44 | Ma Main: 5 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [3]: PLAY

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 44 | Ma Main: 4 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 44 | Ma Main: 3 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 44 | Ma Main: 1 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [5]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 43 | Ma Main: 2 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 43 | Ma Main: 1 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 42 | Ma Main: 2 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: RETREAT

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 42 | Ma Main: 2 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: ENERGY

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 42 | Ma Main: 2 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 42 | Ma Main: 2 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 45 | Ma Main: 7 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 42 | Opp Main: 2 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [6]: ATTACH

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 45 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 42 | Opp Main: 2 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 45 | Ma Main: 5 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 42 | Opp Main: 2 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [5]: ATTACK (Attack: Fighting Wings)

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 41 | Ma Main: 3 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 45 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 50/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 41 | Ma Main: 2 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 45 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 310/330)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [1]: EVOLVE

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 41 | Ma Main: 1 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 45 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 310/330)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [1]: ABILITY

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 40 | Ma Main: 4 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 45 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 310/330)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [3]: ATTACH

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 40 | Ma Main: 3 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 45 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 310/330)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [5]: END

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Mega Lopunny ex (HP: 310/330)
==================================================
[DECISION] Action choisie -> Index [7]: RETREAT

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Mega Lopunny ex (HP: 310/330)
==================================================
[DECISION] Action choisie -> Index [0]: ENERGY

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Mega Lopunny ex (HP: 310/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 310/330)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 5 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 310/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 310/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 2 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 310/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 3 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 310/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 2 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 310/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 42 | Ma Main: 3 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 310/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 41 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 310/330)
==================================================
[DECISION] Action choisie -> Index [2]: ATTACH

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 41 | Ma Main: 3 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 310/330)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 41 | Ma Main: 2 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 310/330)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 5] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 39 | Ma Main: 4 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 41 | Opp Main: 2 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 250/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 5] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 39 | Ma Main: 3 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 41 | Opp Main: 2 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 250/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 5] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 37 | Ma Main: 3 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 41 | Opp Main: 2 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 250/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [3]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 40 | Ma Main: 3 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 37 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 270/330)
 Opp Actif: Mega Lopunny ex (HP: 250/330)
==================================================
[DECISION] Action choisie -> Index [2]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 7] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 36 | Ma Main: 4 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 190/330)
 Opp Actif: Mega Lopunny ex (HP: 270/330)
==================================================
[DECISION] Action choisie -> Index [3]: ATTACH

==================================================
 [TOUR 7] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 36 | Ma Main: 3 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 40 | Opp Main: 3 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 190/330)
 Opp Actif: Mega Lopunny ex (HP: 270/330)
==================================================
[DECISION] Action choisie -> Index [4]: ATTACK (Attack: Spiky Hopper)

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 39 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 36 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 110/330)
 Opp Actif: Mega Lopunny ex (HP: 190/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 39 | Ma Main: 3 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 36 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 110/330)
 Opp Actif: Mega Lopunny ex (HP: 190/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 38 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 36 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 110/330)
 Opp Actif: Mega Lopunny ex (HP: 190/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 31 | Ma Main: 3 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 36 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 110/330)
 Opp Actif: Mega Lopunny ex (HP: 190/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 37 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 36 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 110/330)
 Opp Actif: Mega Lopunny ex (HP: 190/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 37 | Ma Main: 3 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 36 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 110/330)
 Opp Actif: Mega Lopunny ex (HP: 190/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 31 | Ma Main: 8 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 36 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 110/330)
 Opp Actif: Mega Lopunny ex (HP: 190/330)
==================================================
[DECISION] Action choisie -> Index [3]: PLAY

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 31 | Ma Main: 7 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 36 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 110/330)
 Opp Actif: Mega Lopunny ex (HP: 190/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 31 | Ma Main: 6 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 36 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 110/330)
 Opp Actif: Mega Lopunny ex (HP: 190/330)
==================================================
[DECISION] Action choisie -> Index [2]: PLAY

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 24 | Ma Main: 5 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 36 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 110/330)
 Opp Actif: Mega Lopunny ex (HP: 190/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 30 | Ma Main: 6 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 36 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 110/330)
 Opp Actif: Mega Lopunny ex (HP: 190/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 30 | Ma Main: 5 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 36 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 110/330)
 Opp Actif: Mega Lopunny ex (HP: 190/330)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 26 | Ma Main: 8 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 36 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 110/330)
 Opp Actif: Mega Lopunny ex (HP: 190/330)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 35 | Ma Main: 4 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 26 | Opp Main: 8 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 130/330)
 Opp Actif: Mega Lopunny ex (HP: 110/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 35 | Ma Main: 3 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 26 | Opp Main: 8 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 130/330)
 Opp Actif: Mega Lopunny ex (HP: 110/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 35 | Ma Main: 2 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 26 | Opp Main: 8 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 130/330)
 Opp Actif: Mega Lopunny ex (HP: 110/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 35 | Ma Main: 0 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 26 | Opp Main: 8 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 130/330)
 Opp Actif: Mega Lopunny ex (HP: 110/330)
==================================================
[DECISION] Action choisie -> Index [5]: CARD

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 34 | Ma Main: 1 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 26 | Opp Main: 8 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 130/330)
 Opp Actif: Mega Lopunny ex (HP: 110/330)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 34 | Ma Main: 0 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 26 | Opp Main: 8 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 130/330)
 Opp Actif: Mega Lopunny ex (HP: 110/330)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACK (Attack: Spiky Hopper)

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 34 | Ma Main: 0 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 26 | Opp Main: 8 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 130/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 26 | Ma Main: 8 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 34 | Opp Main: 3 | Opp Banc: 5 | Prizes: 3
 Opp Actif: Mega Lopunny ex (HP: 130/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 25 | Ma Main: 9 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 34 | Opp Main: 3 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Mega Lopunny ex (HP: 130/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 25 | Ma Main: 8 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 34 | Opp Main: 3 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Mega Lopunny ex (HP: 130/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 25 | Ma Main: 8 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 34 | Opp Main: 3 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 25 | Ma Main: 7 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 34 | Opp Main: 3 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 25 | Ma Main: 6 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 34 | Opp Main: 3 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 25 | Ma Main: 5 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 34 | Opp Main: 3 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 25 | Ma Main: 4 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 34 | Opp Main: 3 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 25 | Ma Main: 3 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 34 | Opp Main: 3 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 24 | Ma Main: 4 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 34 | Opp Main: 3 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [3]: END

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 33 | Ma Main: 4 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 24 | Opp Main: 4 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 33 | Ma Main: 3 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 24 | Opp Main: 4 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [3]: RETREAT

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 33 | Ma Main: 3 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 24 | Opp Main: 4 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: ENERGY

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 33 | Ma Main: 3 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 24 | Opp Main: 4 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 33 | Ma Main: 3 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 24 | Opp Main: 4 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 130/330)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [2]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 33 | Ma Main: 3 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 24 | Opp Main: 4 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 130/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 24 | Ma Main: 4 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 33 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Opp Actif: Mega Lopunny ex (HP: 130/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 23 | Ma Main: 5 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 33 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 130/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 23 | Ma Main: 4 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 33 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 130/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 23 | Ma Main: 4 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 33 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 23 | Ma Main: 3 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 33 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [3]: ABILITY

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 22 | Ma Main: 6 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 33 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 22 | Ma Main: 5 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 33 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 22 | Ma Main: 3 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 33 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 21 | Ma Main: 4 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 33 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: EVOLVE

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 21 | Ma Main: 3 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 33 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: ABILITY

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 20 | Ma Main: 6 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 33 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 20 | Ma Main: 5 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 33 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [3]: END

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 32 | Ma Main: 5 | Mon Banc: 5 | Prizes: 2
 Opp Deck: 20 | Opp Main: 5 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce (HP: 140/140)
==================================================
[DECISION] Action choisie -> Index [5]: ATTACH

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 28 | Ma Main: 8 | Mon Banc: 5 | Prizes: 2
 Opp Deck: 20 | Opp Main: 5 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce (HP: 140/140)
==================================================
[DECISION] Action choisie -> Index [2]: EVOLVE

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 28 | Ma Main: 7 | Mon Banc: 5 | Prizes: 2
 Opp Deck: 20 | Opp Main: 5 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce (HP: 140/140)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 28 | Ma Main: 6 | Mon Banc: 5 | Prizes: 2
 Opp Deck: 20 | Opp Main: 5 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce (HP: 140/140)
==================================================
[DECISION] Action choisie -> Index [3]: EVOLVE

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 28 | Ma Main: 5 | Mon Banc: 5 | Prizes: 2
 Opp Deck: 20 | Opp Main: 5 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce (HP: 140/140)
==================================================
[DECISION] Action choisie -> Index [3]: ABILITY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 27 | Ma Main: 8 | Mon Banc: 4 | Prizes: 2
 Opp Deck: 20 | Opp Main: 5 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce (HP: 140/140)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 27 | Ma Main: 7 | Mon Banc: 5 | Prizes: 2
 Opp Deck: 20 | Opp Main: 5 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce (HP: 140/140)
==================================================
[DECISION] Action choisie -> Index [3]: PLAY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 27 | Ma Main: 6 | Mon Banc: 5 | Prizes: 2
 Opp Deck: 20 | Opp Main: 5 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce (HP: 140/140)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 27 | Ma Main: 4 | Mon Banc: 5 | Prizes: 2
 Opp Deck: 20 | Opp Main: 5 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce (HP: 140/140)
==================================================
[DECISION] Action choisie -> Index [4]: CARD

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 26 | Ma Main: 5 | Mon Banc: 5 | Prizes: 2
 Opp Deck: 20 | Opp Main: 5 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce (HP: 140/140)
==================================================
[DECISION] Action choisie -> Index [2]: PLAY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 26 | Ma Main: 4 | Mon Banc: 5 | Prizes: 2
 Opp Deck: 20 | Opp Main: 5 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce (HP: 140/140)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 26 | Ma Main: 4 | Mon Banc: 5 | Prizes: 2
 Opp Deck: 20 | Opp Main: 5 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 14] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 19 | Ma Main: 6 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 26 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Abra (HP: 50/50)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 14] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 16 | Ma Main: 8 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 26 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Abra (HP: 50/50)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 14] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 16 | Ma Main: 7 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 26 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Abra (HP: 50/50)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 14] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 16 | Ma Main: 6 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 26 | Opp Main: 4 | Opp Banc: 5 | Prizes: 2
 Mon Actif: Abra (HP: 50/50)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: END

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 25 | Ma Main: 5 | Mon Banc: 5 | Prizes: 2
 Opp Deck: 16 | Opp Main: 6 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [2]: ATTACH

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 25 | Ma Main: 4 | Mon Banc: 5 | Prizes: 2
 Opp Deck: 16 | Opp Main: 6 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [3]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 25 | Ma Main: 4 | Mon Banc: 5 | Prizes: 2
 Opp Deck: 16 | Opp Main: 6 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 16 | Ma Main: 6 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 15 | Ma Main: 7 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 13 | Ma Main: 8 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 13 | Ma Main: 7 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 13 | Ma Main: 6 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 13 | Ma Main: 4 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 12 | Ma Main: 5 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 12 | Ma Main: 4 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 11 | Ma Main: 4 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 11 | Ma Main: 3 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: ABILITY

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 11 | Ma Main: 6 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 11 | Ma Main: 6 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 11 | Ma Main: 5 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 11 | Ma Main: 4 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: ABILITY

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 10 | Ma Main: 7 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 10 | Ma Main: 6 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [3]: CARD

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 9 | Ma Main: 7 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACK (Attack: Trading Places)

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 9 | Ma Main: 7 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 25 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 24 | Ma Main: 6 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [5]: RETREAT

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 24 | Ma Main: 6 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ENERGY

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 24 | Ma Main: 6 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 24 | Ma Main: 6 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 130/330)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [4]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 24 | Ma Main: 6 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 130/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

Partie 1 terminée en 135 étapes. Vainqueur : Joueur 0

```

---

## PARTIE 2

```text
# PARTIE DE DÉMONSTRATION 2

Démarrage du combat Lopunny vs Lopunny...

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 60 | Ma Main: 0 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 60 | Opp Main: 0 | Opp Banc: 0 | Prizes: 0
==================================================
[DECISION] Action choisie -> Index [0]: YES

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 53 | Ma Main: 7 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 53 | Opp Main: 7 | Opp Banc: 0 | Prizes: 0
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 53 | Ma Main: 7 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 47 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
==================================================
[DECISION] Action choisie -> Index [1]: NUMBER (Number: 1)

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 46 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 46 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 46 | Opp Main: 5 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 45 | Ma Main: 6 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 46 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 45 | Ma Main: 5 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 46 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 45 | Ma Main: 4 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 46 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [3]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 5 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 46 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [3]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 4 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 3 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 4 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 3 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 1 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [6]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 42 | Ma Main: 2 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 46 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 45 | Ma Main: 8 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 2 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: PLAY

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 44 | Ma Main: 8 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 2 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: PLAY

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 44 | Ma Main: 7 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 42 | Opp Main: 2 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 44 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 42 | Opp Main: 2 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [4]: END

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 41 | Ma Main: 3 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 44 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: EVOLVE

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 41 | Ma Main: 2 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 44 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [3]: ATTACH

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 41 | Ma Main: 1 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 44 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 41 | Ma Main: 0 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 44 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ABILITY

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 40 | Ma Main: 3 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 44 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 40 | Ma Main: 3 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 44 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [4]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 40 | Ma Main: 3 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 44 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 44 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 40 | Opp Main: 4 | Opp Banc: 2 | Prizes: 5
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 5] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 43 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 40 | Opp Main: 4 | Opp Banc: 2 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 5] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 36 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 40 | Opp Main: 4 | Opp Banc: 2 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 5] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 42 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 40 | Opp Main: 4 | Opp Banc: 2 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 5] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 42 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 40 | Opp Main: 4 | Opp Banc: 2 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 5] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 42 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 40 | Opp Main: 4 | Opp Banc: 2 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: END

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 39 | Ma Main: 5 | Mon Banc: 2 | Prizes: 5
 Opp Deck: 42 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [6]: ATTACH

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 35 | Ma Main: 8 | Mon Banc: 2 | Prizes: 5
 Opp Deck: 42 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [8]: ATTACH

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 35 | Ma Main: 7 | Mon Banc: 2 | Prizes: 5
 Opp Deck: 42 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [5]: PLAY

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 35 | Ma Main: 6 | Mon Banc: 3 | Prizes: 5
 Opp Deck: 42 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: ATTACH

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 35 | Ma Main: 5 | Mon Banc: 3 | Prizes: 5
 Opp Deck: 42 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 28 | Ma Main: 4 | Mon Banc: 3 | Prizes: 5
 Opp Deck: 42 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 34 | Ma Main: 5 | Mon Banc: 3 | Prizes: 5
 Opp Deck: 42 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 34 | Ma Main: 4 | Mon Banc: 4 | Prizes: 5
 Opp Deck: 42 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 34 | Ma Main: 3 | Mon Banc: 4 | Prizes: 5
 Opp Deck: 42 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [3]: CARD

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 33 | Ma Main: 4 | Mon Banc: 4 | Prizes: 5
 Opp Deck: 42 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 32 | Ma Main: 5 | Mon Banc: 4 | Prizes: 5
 Opp Deck: 42 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: EVOLVE

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 32 | Ma Main: 4 | Mon Banc: 4 | Prizes: 5
 Opp Deck: 42 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 32 | Ma Main: 3 | Mon Banc: 4 | Prizes: 5
 Opp Deck: 42 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 31 | Ma Main: 3 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 42 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 7] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 41 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 31 | Opp Main: 3 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [2]: PLAY

==================================================
 [TOUR 7] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 34 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 31 | Opp Main: 3 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 7] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 40 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 31 | Opp Main: 3 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [2]: PLAY

==================================================
 [TOUR 7] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 40 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 31 | Opp Main: 3 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 7] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 39 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 31 | Opp Main: 3 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 7] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 38 | Ma Main: 8 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 31 | Opp Main: 3 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [2]: END

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 30 | Ma Main: 4 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 38 | Opp Main: 8 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 30 | Ma Main: 3 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 38 | Opp Main: 8 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: EVOLVE

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 30 | Ma Main: 2 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 38 | Opp Main: 8 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACK (Attack: Tenacious Tail)

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 37 | Ma Main: 9 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 30 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 37 | Ma Main: 8 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 30 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 37 | Ma Main: 7 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 30 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [2]: ATTACH

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 33 | Ma Main: 10 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 30 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 33 | Ma Main: 9 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 30 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 33 | Ma Main: 8 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 30 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 32 | Ma Main: 9 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 30 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [2]: END

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 29 | Ma Main: 3 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 32 | Opp Main: 9 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 29 | Ma Main: 2 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 32 | Opp Main: 9 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACK (Attack: Tenacious Tail)

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 31 | Ma Main: 10 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 29 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 31 | Ma Main: 9 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 29 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 30 | Ma Main: 10 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 29 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [3]: CARD

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 29 | Ma Main: 11 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 29 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 29 | Ma Main: 10 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 29 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 29 | Ma Main: 9 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 29 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 29 | Ma Main: 7 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 29 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 28 | Ma Main: 8 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 29 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 28 | Ma Main: 7 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 29 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 28 | Ma Main: 6 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 29 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: END

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 28 | Ma Main: 3 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 28 | Opp Main: 6 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 28 | Ma Main: 2 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 28 | Opp Main: 6 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: END

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 27 | Ma Main: 7 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 28 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 27 | Ma Main: 6 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 28 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 27 | Ma Main: 6 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 28 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: END

==================================================
 [TOUR 14] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 27 | Ma Main: 3 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 27 | Opp Main: 6 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 14] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 27 | Ma Main: 2 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 27 | Opp Main: 6 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: RETREAT

==================================================
 [TOUR 14] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 27 | Ma Main: 2 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 27 | Opp Main: 6 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [4]: CARD

==================================================
 [TOUR 14] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 27 | Ma Main: 2 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 27 | Opp Main: 6 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 26 | Ma Main: 7 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 27 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 26 | Ma Main: 6 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 27 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 26 | Ma Main: 5 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 27 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 24 | Ma Main: 5 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 27 | Opp Main: 2 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: END

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 26 | Ma Main: 3 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 24 | Opp Main: 5 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 22 | Ma Main: 6 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 24 | Opp Main: 5 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: ATTACH

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 22 | Ma Main: 5 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 24 | Opp Main: 5 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 15 | Ma Main: 4 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 24 | Opp Main: 5 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 21 | Ma Main: 5 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 24 | Opp Main: 5 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 21 | Ma Main: 4 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 24 | Opp Main: 5 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: RETREAT

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 21 | Ma Main: 4 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 24 | Opp Main: 5 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 21 | Ma Main: 4 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 24 | Opp Main: 5 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 21 | Ma Main: 3 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 24 | Opp Main: 5 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 20 | Ma Main: 4 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 24 | Opp Main: 5 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 23 | Ma Main: 6 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 20 | Opp Main: 4 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 100/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 23 | Ma Main: 5 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 20 | Opp Main: 4 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 100/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 23 | Ma Main: 5 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 20 | Opp Main: 4 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [3]: EVOLVE

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 23 | Ma Main: 4 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 20 | Opp Main: 4 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 23 | Ma Main: 3 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 20 | Opp Main: 4 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 16 | Ma Main: 2 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 20 | Opp Main: 4 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 22 | Ma Main: 3 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 20 | Opp Main: 4 | Opp Banc: 5 | Prizes: 5
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: END

==================================================
 [TOUR 18] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 19 | Ma Main: 5 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 22 | Opp Main: 3 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 18] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 19 | Ma Main: 4 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 22 | Opp Main: 3 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 18] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 19 | Ma Main: 4 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 22 | Opp Main: 3 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: ATTACK (Attack: Spiky Hopper)

==================================================
 [TOUR 18] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 19 | Ma Main: 4 | Mon Banc: 5 | Prizes: 5
 Opp Deck: 22 | Opp Main: 3 | Opp Banc: 5 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 18] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 22 | Ma Main: 3 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 21 | Ma Main: 4 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 21 | Ma Main: 3 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 20 | Ma Main: 3 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 14 | Ma Main: 8 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 14 | Ma Main: 7 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 14 | Ma Main: 5 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 13 | Ma Main: 6 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 13 | Ma Main: 5 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 13 | Ma Main: 4 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 12 | Ma Main: 5 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 12 | Ma Main: 4 | Mon Banc: 5 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: ABILITY

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 11 | Ma Main: 7 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: EVOLVE

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 11 | Ma Main: 6 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: ABILITY

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 10 | Ma Main: 9 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 10 | Ma Main: 8 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 10 | Ma Main: 6 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 9 | Ma Main: 7 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 19 | Opp Main: 5 | Opp Banc: 5 | Prizes: 4
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 18 | Ma Main: 6 | Mon Banc: 5 | Prizes: 4
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 270/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: PLAY

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 18 | Ma Main: 5 | Mon Banc: 5 | Prizes: 4
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 270/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 18 | Ma Main: 3 | Mon Banc: 5 | Prizes: 4
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 270/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 17 | Ma Main: 4 | Mon Banc: 5 | Prizes: 4
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 270/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [3]: RETREAT

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 17 | Ma Main: 4 | Mon Banc: 5 | Prizes: 4
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 270/330)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 17 | Ma Main: 4 | Mon Banc: 5 | Prizes: 4
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 10 | Ma Main: 3 | Mon Banc: 5 | Prizes: 4
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 16 | Ma Main: 4 | Mon Banc: 5 | Prizes: 4
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 16 | Ma Main: 3 | Mon Banc: 5 | Prizes: 4
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 16 | Ma Main: 3 | Mon Banc: 5 | Prizes: 4
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACK (Attack: Tenacious Tail)

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 16 | Ma Main: 3 | Mon Banc: 5 | Prizes: 4
 Opp Deck: 9 | Opp Main: 7 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 9 | Ma Main: 7 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 16 | Opp Main: 4 | Opp Banc: 5 | Prizes: 3
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 21] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 8 | Ma Main: 8 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 16 | Opp Main: 4 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 21] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 8 | Ma Main: 7 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 16 | Opp Main: 4 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 21] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 7 | Ma Main: 8 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 16 | Opp Main: 4 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 21] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 7 | Ma Main: 7 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 16 | Opp Main: 4 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 21] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 7 | Ma Main: 6 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 16 | Opp Main: 4 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 22] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 15 | Ma Main: 5 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 7 | Opp Main: 6 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 210/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 22] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 15 | Ma Main: 4 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 7 | Opp Main: 6 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 210/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 22] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 15 | Ma Main: 6 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 7 | Opp Main: 6 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 210/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [7]: ATTACH

==================================================
 [TOUR 22] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 15 | Ma Main: 5 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 7 | Opp Main: 6 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 210/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACK (Attack: Tenacious Tail)

==================================================
 [TOUR 23] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 6 | Ma Main: 7 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 15 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 150/330)
 Opp Actif: Dudunsparce ex (HP: 210/270)
==================================================
[DECISION] Action choisie -> Index [2]: PLAY

==================================================
 [TOUR 23] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 6 | Ma Main: 6 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 15 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 150/330)
 Opp Actif: Dudunsparce ex (HP: 210/270)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 23] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 6 | Ma Main: 7 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 15 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 210/270)
==================================================
[DECISION] Action choisie -> Index [2]: EVOLVE

==================================================
 [TOUR 23] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 6 | Ma Main: 6 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 15 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 210/270)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 23] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 6 | Ma Main: 5 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 15 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 210/270)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 23] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 5 | Ma Main: 5 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 15 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 210/270)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 23] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 5 | Ma Main: 4 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 15 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 210/270)
==================================================
[DECISION] Action choisie -> Index [1]: ABILITY

==================================================
 [TOUR 23] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 4 | Ma Main: 7 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 15 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 210/270)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 23] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 4 | Ma Main: 6 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 15 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 210/270)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 23] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 4 | Ma Main: 5 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 15 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 210/270)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 24] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 14 | Ma Main: 6 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 4 | Opp Main: 5 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 150/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [4]: ATTACH

==================================================
 [TOUR 24] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 14 | Ma Main: 5 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 4 | Opp Main: 5 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 150/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 24] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 14 | Ma Main: 4 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 4 | Opp Main: 5 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 150/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 24] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 13 | Ma Main: 5 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 4 | Opp Main: 5 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 150/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: END

==================================================
 [TOUR 25] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 3 | Ma Main: 6 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 150/270)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 25] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 3 | Ma Main: 5 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 150/270)
==================================================
[DECISION] Action choisie -> Index [1]: EVOLVE

==================================================
 [TOUR 25] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 3 | Ma Main: 4 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 150/270)
==================================================
[DECISION] Action choisie -> Index [0]: ABILITY

==================================================
 [TOUR 25] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 2 | Ma Main: 7 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 150/270)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 25] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 2 | Ma Main: 6 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 150/270)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 25] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 2 | Ma Main: 4 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 150/270)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 25] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 1 | Ma Main: 5 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 150/270)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 25] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 1 | Ma Main: 4 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 150/270)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 26] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 12 | Ma Main: 6 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 1 | Opp Main: 4 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 90/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [3]: ATTACH

==================================================
 [TOUR 26] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 12 | Ma Main: 5 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 1 | Opp Main: 4 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 90/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 26] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 12 | Ma Main: 4 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 1 | Opp Main: 4 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 90/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 26] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 12 | Ma Main: 2 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 1 | Opp Main: 4 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 90/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: END

==================================================
 [TOUR 27] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 0 | Ma Main: 5 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 12 | Opp Main: 2 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 90/270)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 27] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 0 | Ma Main: 4 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 12 | Opp Main: 2 | Opp Banc: 5 | Prizes: 3
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce ex (HP: 90/270)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 28] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 11 | Ma Main: 3 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 0 | Opp Main: 4 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 30/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 28] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 11 | Ma Main: 2 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 0 | Opp Main: 4 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 30/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 28] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 11 | Ma Main: 2 | Mon Banc: 5 | Prizes: 3
 Opp Deck: 0 | Opp Main: 4 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 30/270)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACK (Attack: Tenacious Tail)

Partie 2 terminée en 179 étapes. Vainqueur : Joueur 1

```

---

## PARTIE 3

```text
# PARTIE DE DÉMONSTRATION 3

Démarrage du combat Lopunny vs Lopunny...

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 60 | Ma Main: 0 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 60 | Opp Main: 0 | Opp Banc: 0 | Prizes: 0
==================================================
[DECISION] Action choisie -> Index [0]: YES

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 53 | Ma Main: 7 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 53 | Opp Main: 7 | Opp Banc: 0 | Prizes: 0
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 53 | Ma Main: 7 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 53 | Opp Main: 6 | Opp Banc: 0 | Prizes: 0
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 47 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 46 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 47 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 46 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 47 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 46 | Ma Main: 5 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 47 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 46 | Ma Main: 3 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 47 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [8]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 45 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 47 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 46 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 46 | Ma Main: 5 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 46 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 4 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 3 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 4 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [4]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 3 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 2 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ABILITY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 2 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 42 | Ma Main: 3 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: END

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 44 | Ma Main: 5 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 44 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 37 | Ma Main: 3 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 43 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 43 | Ma Main: 3 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 42 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 41 | Ma Main: 5 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 41 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACK (Attack: Spiky Hopper)

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 41 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 3 | Opp Banc: 4 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 42 | Ma Main: 3 | Mon Banc: 4 | Prizes: 6
 Opp Deck: 41 | Opp Main: 5 | Opp Banc: 0 | Prizes: 5
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [3]: CARD

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 41 | Ma Main: 4 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 41 | Opp Main: 5 | Opp Banc: 0 | Prizes: 5
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: END

==================================================
 [TOUR 5] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 40 | Ma Main: 6 | Mon Banc: 0 | Prizes: 5
 Opp Deck: 41 | Opp Main: 4 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [3]: ATTACK (Attack: Spiky Hopper)

==================================================
 [TOUR 5] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 40 | Ma Main: 6 | Mon Banc: 0 | Prizes: 5
 Opp Deck: 41 | Opp Main: 4 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 5] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 41 | Ma Main: 4 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 40 | Opp Main: 7 | Opp Banc: 0 | Prizes: 4
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 40 | Ma Main: 5 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 40 | Opp Main: 7 | Opp Banc: 0 | Prizes: 4
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 40 | Ma Main: 4 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 40 | Opp Main: 7 | Opp Banc: 0 | Prizes: 4
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 40 | Ma Main: 3 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 40 | Opp Main: 7 | Opp Banc: 0 | Prizes: 4
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 39 | Ma Main: 4 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 40 | Opp Main: 7 | Opp Banc: 0 | Prizes: 4
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: ATTACH

==================================================
 [TOUR 6] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 39 | Ma Main: 3 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 40 | Opp Main: 7 | Opp Banc: 0 | Prizes: 4
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 7] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 39 | Ma Main: 8 | Mon Banc: 0 | Prizes: 4
 Opp Deck: 39 | Opp Main: 3 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [5]: ATTACK (Attack: Spiky Hopper)

==================================================
 [TOUR 7] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 39 | Ma Main: 8 | Mon Banc: 0 | Prizes: 4
 Opp Deck: 39 | Opp Main: 3 | Opp Banc: 3 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 7] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 39 | Ma Main: 3 | Mon Banc: 3 | Prizes: 6
 Opp Deck: 39 | Opp Main: 9 | Opp Banc: 0 | Prizes: 3
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 8] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 38 | Ma Main: 4 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 39 | Opp Main: 9 | Opp Banc: 0 | Prizes: 3
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: END

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 38 | Ma Main: 10 | Mon Banc: 0 | Prizes: 3
 Opp Deck: 38 | Opp Main: 4 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [7]: ATTACK (Attack: Spiky Hopper)

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 38 | Ma Main: 10 | Mon Banc: 0 | Prizes: 3
 Opp Deck: 38 | Opp Main: 4 | Opp Banc: 2 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 9] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 38 | Ma Main: 4 | Mon Banc: 2 | Prizes: 6
 Opp Deck: 38 | Opp Main: 11 | Opp Banc: 0 | Prizes: 2
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 37 | Ma Main: 5 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 38 | Opp Main: 11 | Opp Banc: 0 | Prizes: 2
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 37 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 38 | Opp Main: 11 | Opp Banc: 0 | Prizes: 2
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 36 | Ma Main: 5 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 38 | Opp Main: 11 | Opp Banc: 0 | Prizes: 2
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 35 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 38 | Opp Main: 11 | Opp Banc: 0 | Prizes: 2
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 35 | Ma Main: 5 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 38 | Opp Main: 11 | Opp Banc: 0 | Prizes: 2
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 10] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 31 | Ma Main: 8 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 38 | Opp Main: 11 | Opp Banc: 0 | Prizes: 2
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: END

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 37 | Ma Main: 12 | Mon Banc: 0 | Prizes: 2
 Opp Deck: 31 | Opp Main: 8 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dudunsparce (HP: 140/140)
==================================================
[DECISION] Action choisie -> Index [8]: ATTACK (Attack: Spiky Hopper)

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 37 | Ma Main: 12 | Mon Banc: 0 | Prizes: 2
 Opp Deck: 31 | Opp Main: 8 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 11] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 31 | Ma Main: 8 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 37 | Opp Main: 13 | Opp Banc: 0 | Prizes: 1
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 30 | Ma Main: 9 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 37 | Opp Main: 13 | Opp Banc: 0 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 30 | Ma Main: 8 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 37 | Opp Main: 13 | Opp Banc: 0 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 29 | Ma Main: 9 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 37 | Opp Main: 13 | Opp Banc: 0 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 28 | Ma Main: 10 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 37 | Opp Main: 13 | Opp Banc: 0 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 21 | Ma Main: 9 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 37 | Opp Main: 13 | Opp Banc: 0 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [3]: CARD

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 27 | Ma Main: 10 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 37 | Opp Main: 13 | Opp Banc: 0 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 12] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 27 | Ma Main: 9 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 37 | Opp Main: 13 | Opp Banc: 0 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [2]: END

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 36 | Ma Main: 14 | Mon Banc: 0 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 36 | Ma Main: 13 | Mon Banc: 0 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 36 | Ma Main: 12 | Mon Banc: 1 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 36 | Ma Main: 11 | Mon Banc: 2 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: PLAY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 36 | Ma Main: 10 | Mon Banc: 3 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [6]: RETREAT

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 36 | Ma Main: 10 | Mon Banc: 3 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ENERGY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 36 | Ma Main: 10 | Mon Banc: 3 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 36 | Ma Main: 10 | Mon Banc: 3 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [3]: PLAY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 29 | Ma Main: 9 | Mon Banc: 3 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 35 | Ma Main: 10 | Mon Banc: 3 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: PLAY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 35 | Ma Main: 9 | Mon Banc: 3 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 34 | Ma Main: 10 | Mon Banc: 3 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 34 | Ma Main: 9 | Mon Banc: 3 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 34 | Ma Main: 7 | Mon Banc: 3 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 33 | Ma Main: 8 | Mon Banc: 3 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: PLAY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 33 | Ma Main: 7 | Mon Banc: 4 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 33 | Ma Main: 6 | Mon Banc: 4 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 33 | Ma Main: 5 | Mon Banc: 4 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 32 | Ma Main: 5 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 32 | Ma Main: 4 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 32 | Ma Main: 2 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 13] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 31 | Ma Main: 3 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 27 | Opp Main: 9 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 14] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 26 | Ma Main: 10 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 31 | Opp Main: 3 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 14] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 26 | Ma Main: 9 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 31 | Opp Main: 3 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 14] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 26 | Ma Main: 9 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 31 | Opp Main: 3 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 14] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 26 | Ma Main: 8 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 31 | Opp Main: 3 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 14] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 26 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 31 | Opp Main: 3 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: END

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 30 | Ma Main: 4 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 26 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: EVOLVE

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 30 | Ma Main: 3 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 26 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 30 | Ma Main: 2 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 26 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 29 | Ma Main: 3 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 26 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 28 | Ma Main: 4 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 26 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [5]: ATTACH

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 28 | Ma Main: 3 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 26 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 28 | Ma Main: 2 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 26 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ABILITY

==================================================
 [TOUR 15] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 27 | Ma Main: 5 | Mon Banc: 4 | Prizes: 1
 Opp Deck: 26 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 270/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 25 | Ma Main: 8 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 27 | Opp Main: 5 | Opp Banc: 4 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 25 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 27 | Opp Main: 5 | Opp Banc: 4 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 23 | Ma Main: 8 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 27 | Opp Main: 5 | Opp Banc: 4 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [3]: PLAY

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 23 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 27 | Opp Main: 5 | Opp Banc: 4 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 23 | Ma Main: 5 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 27 | Opp Main: 5 | Opp Banc: 4 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 22 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 27 | Opp Main: 5 | Opp Banc: 4 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 22 | Ma Main: 5 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 27 | Opp Main: 5 | Opp Banc: 4 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 16] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 21 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 27 | Opp Main: 5 | Opp Banc: 4 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 270/270)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACK (Attack: Assault Landing)

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 26 | Ma Main: 6 | Mon Banc: 4 | Prizes: 1
 Opp Deck: 21 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 200/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [3]: ATTACH

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 26 | Ma Main: 5 | Mon Banc: 4 | Prizes: 1
 Opp Deck: 21 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 200/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 24 | Ma Main: 6 | Mon Banc: 4 | Prizes: 1
 Opp Deck: 21 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 200/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 17] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 24 | Ma Main: 5 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 21 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 200/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 18] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 20 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 24 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 200/270)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 18] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 20 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 24 | Opp Main: 5 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 200/270)
==================================================
[DECISION] Action choisie -> Index [2]: ATTACK (Attack: Assault Landing)

==================================================
 [TOUR 19] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 23 | Ma Main: 6 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 20 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 130/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 19 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 23 | Opp Main: 6 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 130/270)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 19 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 23 | Opp Main: 6 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 130/270)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 19 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 23 | Opp Main: 6 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 130/270)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 20] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 18 | Ma Main: 5 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 23 | Opp Main: 6 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 130/270)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACK (Attack: Assault Landing)

==================================================
 [TOUR 21] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 22 | Ma Main: 7 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 18 | Opp Main: 5 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 60/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 22] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 17 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 22 | Opp Main: 7 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 60/270)
==================================================
[DECISION] Action choisie -> Index [1]: END

==================================================
 [TOUR 23] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 21 | Ma Main: 8 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 17 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 60/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 24] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 16 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 21 | Opp Main: 8 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 60/270)
==================================================
[DECISION] Action choisie -> Index [2]: END

==================================================
 [TOUR 25] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 20 | Ma Main: 9 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 16 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 60/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: ATTACH

==================================================
 [TOUR 25] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 20 | Ma Main: 8 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 16 | Opp Main: 7 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 60/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 26] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 15 | Ma Main: 8 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 20 | Opp Main: 8 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 60/270)
==================================================
[DECISION] Action choisie -> Index [3]: END

==================================================
 [TOUR 27] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 19 | Ma Main: 9 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 15 | Opp Main: 8 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce ex (HP: 60/270)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: END

==================================================
 [TOUR 28] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 14 | Ma Main: 9 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 19 | Opp Main: 9 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 60/270)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 28] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 14 | Ma Main: 8 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 19 | Opp Main: 9 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 60/270)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 28] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 13 | Ma Main: 8 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 19 | Opp Main: 9 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 60/270)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 28] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 13 | Ma Main: 7 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 19 | Opp Main: 9 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 60/270)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 28] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 13 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 19 | Opp Main: 9 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Dudunsparce ex (HP: 60/270)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 28] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 13 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 19 | Opp Main: 9 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 28] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 13 | Ma Main: 5 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 19 | Opp Main: 9 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: RETREAT

==================================================
 [TOUR 28] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 13 | Ma Main: 5 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 19 | Opp Main: 9 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Fan Rotom (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 28] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 13 | Ma Main: 5 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 19 | Opp Main: 9 | Opp Banc: 5 | Prizes: 1
 Mon Actif: Abra (HP: 50/50)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 18 | Ma Main: 10 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [5]: ATTACH

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 14 | Ma Main: 13 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [3]: EVOLVE

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 14 | Ma Main: 12 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [5]: RETREAT

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 14 | Ma Main: 12 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [0]: ENERGY

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 14 | Ma Main: 12 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 14 | Ma Main: 12 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [3]: PLAY

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 14 | Ma Main: 11 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 14 | Ma Main: 9 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 13 | Ma Main: 10 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [2]: EVOLVE

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 13 | Ma Main: 9 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [2]: ABILITY

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 13 | Ma Main: 12 | Mon Banc: 4 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [3]: PLAY

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 13 | Ma Main: 11 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 13 | Ma Main: 10 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Abra (HP: 50/50)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 13 | Ma Main: 10 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Fan Rotom (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 29] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 13 | Ma Main: 10 | Mon Banc: 5 | Prizes: 1
 Opp Deck: 13 | Opp Main: 5 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

Partie 3 terminée en 147 étapes. Vainqueur : Joueur 0

```

---

## PARTIE 4

```text
# PARTIE DE DÉMONSTRATION 4

Démarrage du combat Lopunny vs Lopunny...

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 60 | Ma Main: 0 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 60 | Opp Main: 0 | Opp Banc: 0 | Prizes: 0
==================================================
[DECISION] Action choisie -> Index [1]: NO

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 53 | Ma Main: 7 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 53 | Opp Main: 7 | Opp Banc: 0 | Prizes: 0
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 53 | Ma Main: 7 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 53 | Opp Main: 6 | Opp Banc: 0 | Prizes: 0
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 46 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [6]: PLAY

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 46 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [4]: ATTACH

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 46 | Ma Main: 5 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [3]: PLAY

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 46 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 45 | Ma Main: 5 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 45 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 45 | Ma Main: 2 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [6]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 3 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 46 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 44 | Opp Main: 3 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 46 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 44 | Opp Main: 3 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 46 | Ma Main: 5 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 44 | Opp Main: 3 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 46 | Ma Main: 3 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 44 | Opp Main: 3 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 45 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 44 | Opp Main: 3 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 45 | Ma Main: 3 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 44 | Opp Main: 3 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 44 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 44 | Opp Main: 3 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 43 | Ma Main: 5 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 44 | Opp Main: 3 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 36 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 44 | Opp Main: 3 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 42 | Ma Main: 5 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 44 | Opp Main: 3 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 42 | Opp Main: 5 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [3]: EVOLVE

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 3 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 42 | Opp Main: 5 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: EVOLVE

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 2 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 42 | Opp Main: 5 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: ATTACH

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 1 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 42 | Opp Main: 5 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dudunsparce (HP: 140/140)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: ABILITY

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 42 | Opp Main: 5 | Opp Banc: 0 | Prizes: 6
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 5 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [3]: ATTACK (Attack: Gale Thrust)

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 5 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

Partie 4 terminée en 28 étapes. Vainqueur : Joueur 1

```

---

## PARTIE 5

```text
# PARTIE DE DÉMONSTRATION 5

Démarrage du combat Lopunny vs Lopunny...

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 60 | Ma Main: 0 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 60 | Opp Main: 0 | Opp Banc: 0 | Prizes: 0
==================================================
[DECISION] Action choisie -> Index [1]: NO

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 53 | Ma Main: 7 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 53 | Opp Main: 7 | Opp Banc: 0 | Prizes: 0
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 53 | Ma Main: 7 | Mon Banc: 0 | Prizes: 0
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 47 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
==================================================
[DECISION] Action choisie -> Index [1]: NUMBER (Number: 1)

==================================================
 [TOUR 0] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 46 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 47 | Opp Main: 6 | Opp Banc: 0 | Prizes: 6
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 46 | Ma Main: 7 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 46 | Ma Main: 6 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: PLAY

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 46 | Ma Main: 5 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 46 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 46 | Ma Main: 3 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 1] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 45 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 46 | Opp Main: 6 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 45 | Ma Main: 7 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 45 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 45 | Ma Main: 5 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 44 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 43 | Ma Main: 7 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 43 | Ma Main: 6 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 43 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 42 | Ma Main: 5 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 42 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [2]: CARD

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 41 | Ma Main: 5 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACH

==================================================
 [TOUR 2] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 41 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 45 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Dunsparce (HP: 70/70)
 Opp Actif: Buneary (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: END

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 5 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 41 | Opp Main: 4 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Buneary (HP: 70/70)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: EVOLVE

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 41 | Opp Main: 4 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: PLAY

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 44 | Ma Main: 3 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 41 | Opp Main: 4 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: CARD

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 43 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 41 | Opp Main: 4 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 42 | Ma Main: 5 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 41 | Opp Main: 4 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 42 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 41 | Opp Main: 4 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Dunsparce (HP: 70/70)
==================================================
[DECISION] Action choisie -> Index [1]: ATTACK (Attack: Spiky Hopper)

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 42 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 41 | Opp Main: 4 | Opp Banc: 1 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 3] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 41 | Ma Main: 4 | Mon Banc: 1 | Prizes: 6
 Opp Deck: 42 | Opp Main: 5 | Opp Banc: 0 | Prizes: 5
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 40 | Ma Main: 5 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 5 | Opp Banc: 0 | Prizes: 5
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: ATTACH

==================================================
 [TOUR 4] - JOUEUR ACTIF: Joueur 0
 Mon Deck: 40 | Ma Main: 4 | Mon Banc: 0 | Prizes: 6
 Opp Deck: 42 | Opp Main: 5 | Opp Banc: 0 | Prizes: 5
 Mon Actif: Moltres (HP: 120/120)
 Opp Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: END

==================================================
 [TOUR 5] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 41 | Ma Main: 6 | Mon Banc: 0 | Prizes: 5
 Opp Deck: 40 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
 Opp Actif: Moltres (HP: 120/120)
==================================================
[DECISION] Action choisie -> Index [4]: ATTACK (Attack: Spiky Hopper)

==================================================
 [TOUR 5] - JOUEUR ACTIF: Joueur 1
 Mon Deck: 41 | Ma Main: 6 | Mon Banc: 0 | Prizes: 5
 Opp Deck: 40 | Opp Main: 4 | Opp Banc: 0 | Prizes: 6
 Mon Actif: Mega Lopunny ex (HP: 330/330)
==================================================
[DECISION] Action choisie -> Index [0]: CARD

Partie 5 terminée en 34 étapes. Vainqueur : Joueur 1

```

---

