#  I am going to try to put the main combat system in here and call player and enemy into it.
import random


def basic_combat(player, enemy):  # it should  take the player's info automatically and add it with a monster
    defend_turns = 0  # used to allow turn based modifier for defence
    real_ac = player.status["ac"]

    vowels = ["a", "e", "i", "o", "u"]
    if enemy.name[0:1] in vowels:  # grammar is good
        grammar = "an"
    else:
        grammar = "a"
    print(f'You have encountered {grammar} {enemy.name}!')

    while enemy.health or player.status["health"] > 0:  # loops till fight is over
        if defend_turns >= 1:
            player.status["ac"] = real_ac
            defend_turns -= 1

        choice = player.combat_choice()  # lets you choose your next move

        if choice == "attack":  # d20 attack to see if you can deal damage
            enemy.health = player.basic_attack(player.stat_ability["str_ability"], enemy.ac, enemy.health)
            if enemy.health < 1:
                print(f'You defeated the {enemy.name}\n')
                return
            print(f'The {enemy.name} has {enemy.health} health left.\n')

        elif choice == "flee":  # it's basically just a d20 plus mod to see if you escape.
            escape = player.flee(player.stat_ability["dex_ability"], enemy.dex)
            if escape:
                print(f'You escaped the {enemy.name}\n')
                return
            else:
                print("You failed to escape!\n")

        elif choice == "defend":  # I don't know if I need the function, but I have it
            player.defend()
            defend_turns += 1

        if player.status["poison"]:  # it checks for poison in status, does damage, puts poison down by one
            player.status["health"] = player.status["health"] - 1
            print("You took one poison damage!")
            player.status["poison"] -= 1

        if player.status["health"] < 1:  # don't die lol
            print("You have died. Game over!")
            exit()

        #  this is the entire enemy turn lol
        player.status["health"], player.status["poison"] = enemy.combat_choice(player)  # goes into the enemy class
        print(f'You have {player.status["health"]} health left.\n')

        if player.status["health"] < 1:
            print("You have died. Game over!")
            exit()


def combat(player, enemy):

    vowels = ["a", "e", "i", "o", "u"]
    if enemy.name[0:1] in vowels:  # grammar is good
        grammar = "an"
    else:
        grammar = "a"
    print(f'You have encountered {grammar} {enemy.name}!')

