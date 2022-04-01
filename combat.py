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


def d20():  # a basic d20 that also tells for critical fails/successes.
    d20_roll = random.randint(1, 20)
    if d20_roll == 1:
        print("Critical fail!")
        return d20_roll
    elif d20_roll == 20:
        print("Critical success!")
        return d20_roll
    else:
        return d20_roll


def roll_check(attacker_mod, defender_ac):  # this one is simple. simply just works :)
    d20r = d20()
    if d20r == 1:
        return False
    elif d20r == 20:
        return True
    elif d20r + attacker_mod > defender_ac:
        return True
    else:
        print("Miss!")
        return False


def player_buff_check(player, ac):

    if player.buffs:  # checks to see if player has any buffs

        if player.buffs["defense"]:  # checks to see if defense is up and if it does it go down by one. if at zero
            player.buffs["defense"] -= 1  # resets ac
            if player.buffs["defense"] <= 0:
                player.status["ac"] = ac


def combat(player, enemy):
    real_ac = player.status["ac"]

    vowels = ["a", "e", "i", "o", "u"]
    if enemy.name[0:1] in vowels:  # grammar is good
        grammar = "an"
    else:
        grammar = "a"
    print(f'You have encountered {grammar} {enemy.name}!')

    while player.status["health"] or enemy.status["health"] > 0:

        player_buff_check(player, real_ac)  # should be able to build this up to work with turn based resets for buffs
        turn_move = player.combat_choice()  # asks for the player's input of what to do.

        if turn_move == "attack":  # starts attack move

            if roll_check(player.stat_ability["str"], enemy.ac):  # but only if player succeeds roll
                enemy.health -= player.damage_roll("str")

                if enemy.health < 1:
                    print(f'You defeated the {enemy.name}\n')
                    return
                print(f'The {enemy.name} has {enemy.health} health left.\n')

        if turn_move == "flee":  # a simply check to see if player can escape. add later for un-escapable monsters.
            # make an "if monster escapable" statement before this once monsters updated.
            if roll_check(player.stat_ability["dex"], enemy.dex):
                print(f'You made it out safely from the {enemy.name}\n')
                return

            else:
                print("You failed to escape. The battle rages on. \n")

        if turn_move == "defend":
            player.defend()

        # ENEMY TURN START HERE

        player_debuff_check()




