#  I am going to try to put the main combat system in here and call player and enemy into it.
import random


def d20():  # a basic d20 that also tells for critical fails/successes.
    d20_roll = random.randint(1, 20)
    if d20_roll == 1:
        print("Critical fail!\n")
        return d20_roll
    elif d20_roll == 20:
        print("Critical success!\n")
        return d20_roll
    else:
        return d20_roll


def roll_check(attacker_mod, defender_mod):  # this one is simple. simply just works :)
    d20r = d20()
    if d20r == 1:
        return False
    elif d20r == 20:
        return True
    elif d20r + attacker_mod > defender_mod:
        return True
    else:
        print("Miss!\n")
        return False


def player_death_check(player):
    if player.status["health"] < 1:
        print("You have died. Game over!")
        exit()


def player_debuff_check(player):

    if player.status["poison"]:  # activates if player has been poisoned, will do damage and tick down the poison
        player.status["health"] -= 1
        player.status["poison"] -= 1
        print("You have taken 1 poison damage!")

        if player.status["poison"] <= 0:
            print("You are no longer poisoned.")

    if player.status["fire"]:
        player.status["health"] -= player.status["fire"]
        print(f'You have taken {player.status["fire"]} fire damage!')
        player.status["fire"] -= 1

        if player.status["fire"] <= 0:
            print("You are no longer on fire.")

    player_death_check(player)


def player_buff_check(player, ac):

    if player.buffs:  # checks to see if player has any buffs

        if player.buffs["defense"]:  # checks to see if defense is up and if it does it go down by one. if at zero
            player.buffs["defense"] -= 1  # resets ac
            if player.buffs["defense"] <= 0:
                player.status["ac"] = ac


def damage_dealer(enemy, info):  # takes a dict from enemies attacks to see what attack will do when hit with resistance

    if enemy.type == "enemy":  # does the attack to the enemy
        if info["damage_type"] in enemy.resistance:
            info["damage"] //= 3  # if enemy has resistance it does far less damage
            enemy.health -= info["damage"]
            print(info["weak_hit"] + f' You delt {int(info["damage"])} {info["damage_type"]} damage.\n')
        else:
            enemy.health -= info["damage"]
            if info["debuff_turns"]:
                enemy.__dict__[info["damage_type"]] += info["debuff_turns"]
            print(info["success_hit"] + f' You delt {int(info["damage"])} {info["damage_type"]} damage!\n')

    elif enemy.type == "player":  # this is what monsters will do to fight le player
        if info["damage_type"] in enemy.resistance:  # attack it does if resistance. lower damage no effect
            info["damage"] //= 3
            enemy.status["health"] -= info["damage"]
            print(info["weak_hit"] + f' {info["damage"]} damage!')

        else:  # the attack it does if there is no resistance
            enemy.status["health"] -= info["damage"]
            if info["debuff_turns"]:
                enemy.status[info["damage_type"]] += info["debuff_turns"]
            print(info["success_hit"] + f' {info["damage"]} damage!')


def enemy_debuff_check(enemy):

    if enemy.fire:
        enemy.health -= enemy.fire  # does more damage than poison, but is harder to stack
        print(f'The {enemy.name} has taken {enemy.fire} fire damage\n')
        enemy.fire -= 1

    if enemy.poison:
        enemy.health -= 1  # poison
        print(f'The {enemy.name} has taken 1 poison damage\n')  # yeah, I comment
        enemy.poison -= 1


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
                damage_dealer(enemy, player.basic_attack(enemy))

        if turn_move == "flee":  # a simply check to see if player can escape. add later for un-escapable monsters.
            # make an "if monster escapable" statement before this once monsters updated.
            if roll_check(player.stat_ability["dex"], enemy.dex):
                print(f'You made it out safely from the {enemy.name}\n')
                return

            else:
                print("You failed to escape. The battle rages on. \n")

        if turn_move == "defend":
            player.defend()

        if turn_move == "fire punch":
            if roll_check(player.stat_ability["int"], enemy.ac):  # checks to see if players int roll is better than ac
                damage_dealer(enemy, player.fire_punch(enemy))

        if enemy.health < 1:  # checks to see if player has defeated enemy yet
            print(f'You defeated the {enemy.name}\n')
            return
        print(f'The {enemy.name} has {enemy.health} health left.\n')

        # ENEMY TURN START HERE

        player_debuff_check(player)
        # enemy_buff_check(enemy)

        print(f'The {enemy.name} prepares to attack you.')
        enemy_turn = enemy.combat_choice()  # turns the entire enemy turn into a dictionary that can be used in file
        if roll_check(enemy_turn["roll_mod"], player.status["ac"]):  # checks if the attack will work
            damage_dealer(player, enemy_turn)
        player_death_check(player)
        print(f'\nYou have {player.status["health"]} health left.\n')

        enemy_debuff_check(enemy)
        if enemy.health < 1:  # checks to see if player has defeated enemy yet
            print(f'You defeated the {enemy.name}\n')
            return

