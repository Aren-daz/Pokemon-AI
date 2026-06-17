import sys
from cg.api import all_card_data, all_attack, CardType

def main():
    cards = {c.cardId: c for c in all_card_data()}
    attacks = {a.attackId: a for a in all_attack()}
    
    deck_ids = [1158, 721, 722, 723, 1145, 1205, 1227, 1235, 3]
    
    for cid in deck_ids:
        if cid not in cards:
            print(f"Card ID {cid} not found!")
            continue
        c = cards[cid]
        c_type = CardType(c.cardType).name if hasattr(CardType, "name") else str(c.cardType)
        print(f"=== {c.name} (ID: {cid}) ===")
        print(f"Type: {c_type}")
        if c.hp > 0:
            print(f"HP: {c.hp}")
        if c.retreatCost > 0:
            print(f"Retreat Cost: {c.retreatCost}")
        if c.evolvesFrom:
            print(f"Evolves From: {c.evolvesFrom}")
        
        # Attacks
        if c.attacks:
            print("Attacks:")
            for aid in c.attacks:
                a = attacks[aid]
                from cg.api import EnergyType
                energy_requirements = ", ".join(EnergyType(e).name for e in a.energies) if a.energies else "None"
                print(f"  - {a.name}: {a.damage} damage | Cost: {energy_requirements}")
                if a.text:
                    print(f"    Text: {a.text}")
                    
        # Skills
        if c.skills:
            print("Skills:")
            for s in c.skills:
                print(f"  - {s.name}: {s.text}")
        print()

if __name__ == "__main__":
    main()
