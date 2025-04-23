# Ashley Mitchell
# 4/21/2025
# P5HW
# Create a game using functions


import random

# Function that returns the player character as a dictionary
def create_player():
    name = input("Enter your name: ")
    gender = input("Choose your gender (male/female): ").lower()
    element = input("Choose your element (fire, water, earth, air, lightning): ").lower()
    
    return {
        "name": name,
        "gender": gender,
        "element": element,
        "health": 100,
        "items": ["sword", "potion"]
    }

# Function to randomly select one enemy from 3 options
def select_enemy():
    enemies = {
        "Zayzar": {
            "type": "Lizard Man Hybrid",
            "attacks": ["acid saliva", "poisonous nails"],
            "health": 80
        },
        "Amaris": {
            "type": "Raven Man Hybrid",
            "attacks": ["black mist", "shadow warriors"],
            "health": 90
        },
        "Cheveyo": {
            "type": "Wolf Man Hybrid",
            "attacks": ["super strength", "paralyzing howl"],
            "health": 100
        }
    }
    enemy_name = random.choice(list(enemies.keys()))
    return enemy_name, enemies[enemy_name]

# Updated battle function with multiple attack options
def battle(player, enemy_name, enemy):
    print(f"\nYou are now battling {enemy_name}, the {enemy['type']}!")
    tries = 3
    combo_used = False
    defending = False

    while tries > 0 and player["health"] > 0 and enemy["health"] > 0:
        print(f"\n{tries} tries left. Your health: {player['health']}, {enemy_name}'s health: {enemy['health']}")
        action = input("Choose your action: 'sword', 'element', 'combo', 'defend', or 'potion': ").lower()

        if action == "sword":
            damage = random.randint(15, 25)
            enemy["health"] -= damage
            print(f"You slash with your sword and deal {damage} damage to {enemy_name}!")

        elif action == "element":
            element = player["element"]
            if element == "fire":
                damage = random.randint(20, 30)
                burn = random.randint(5, 10)
                enemy["health"] -= (damage + burn)
                print(f"You hurl a fireball! {damage} damage + {burn} burn damage!")
            elif element == "water":
                damage = random.randint(18, 28)
                heal = random.randint(5, 10)
                enemy["health"] -= damage
                player["health"] += heal
                print(f"You summon a water wave! {damage} damage and you heal {heal} HP.")
            elif element == "earth":
                damage = random.randint(22, 32)
                print(f"You launch an earth spike! It deals {damage} damage.")
                enemy["health"] -= damage
            elif element == "air":
                damage = random.randint(15, 25)
                print(f"You slice with sharp air! It deals {damage} damage.")
                enemy["health"] -= damage
            elif element == "lightning":
                damage = random.randint(20, 30)
                stun = random.choice([True, False])
                enemy["health"] -= damage
                print(f"You blast lightning! {damage} damage" + (" and the enemy is stunned!" if stun else "!"))
                if stun:
                    defending = "stunned"
            else:
                print("Unknown element. No effect.")

        elif action == "combo":
            if not combo_used:
                combo_damage = random.randint(35, 50)
                enemy["health"] -= combo_damage
                combo_used = True
                print(f"You perform a devastating combo and deal {combo_damage} damage!")
            else:
                print("You’ve already used your combo move!")

        elif action == "defend":
            defending = True
            print("You brace yourself to reduce incoming damage.")

        elif action == "potion":
            if "potion" in player["items"]:
                heal = random.randint(20, 40)
                player["health"] += heal
                player["items"].remove("potion")
                print(f"You used a potion and restored {heal} health.")
            else:
                print("You have no potion left!")

        else:
            print("Invalid action! You lose a turn.")

        # Enemy attacks if still alive and not stunned
        if enemy["health"] > 0 and defending != "stunned":
            enemy_attack = random.choice(enemy["attacks"])
            base_damage = random.randint(15, 30)

            if defending:
                reduced_damage = base_damage // 2
                player["health"] -= reduced_damage
                print(f"{enemy_name} attacks with {enemy_attack} but you defend and take only {reduced_damage} damage!")
                defending = False
            else:
                player["health"] -= base_damage
                print(f"{enemy_name} attacks with {enemy_attack} and deals {base_damage} damage!")

        defending = False  # Reset unless stunned skipped it
        tries -= 1

    # End of battle outcomes
    if enemy["health"] <= 0:
        print(f"\n🎉 Congratulations {player['name']}! You have defeated {enemy_name} and escaped the enemy's lair!")
    elif player["health"] <= 0:
        print(f"\n💀 You have been defeated by {enemy_name}.")
    else:
        print(f"\n💀 You failed to defeat {enemy_name} in 3 tries. You remain imprisoned.")

# Main function as central hub
def main():
    print("⚔️ Welcome to EREBUS ⚔️")
    player = create_player()
    enemy_name, enemy = select_enemy()
    battle(player, enemy_name, enemy)

# Start the game
if __name__ == "__main__":
    main()
