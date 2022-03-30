import random
import json
import enemies
import encounters


class Player:
    def __init__(self):
        self.stats = {
            "str": 0,
            "dex": 0,
            "con": 0,
            "wis": 0,
            "int": 0,
            "cha": 0,
        }
        self.stat_ability = {
            "str_ability": 0,
            "dex_ability": 0,
            "con_ability": 0,
            "wis_ability": 0,
            "int_ability": 0,
            "cha_ability": 0,
        }
        self.status = {
            "health": 0,
            "max_health": 0,
            "ac": 0,
            "poison": 0,
            "summonGreg": 0
        }
        self.skills = {
            "attack": 1,
            "flee": 1,
            "defend": 0,
        }
        self.knownMonsters = ["slime"]
        self.knowledge = []

    def stat_reset(self):
        health = random.randint(1, 8) + self.stat_ability["con_ability"]
        self.status = {
            "health": health,
            "max_health": health,
            "ac": 10 + self.stat_ability["dex_ability"],
            "poison": 0,
            "summonGreg": 0
        }
        self.skills = {
            "attack": 1,
            "flee": 1,
            "defend": 0,
        }

    def basic_combat(self, enemy):  # it should  take the player's info automatically and add it with a monster
        defend_turns = 0  # used to allow turn based modifier for defence
        real_ac = self.status["ac"]

        vowels = ["a", "e", "i", "o", "u"]
        if enemy.name[0:1] in vowels:  # grammar is good
            grammar = "an"
        else:
            grammar = "a"
        print(f'You have encountered {grammar} {enemy.name}!')

        while enemy.health or self.status["health"] > 0:  # loops till fight is over
            if defend_turns >= 1:
                self.status["ac"] = real_ac
                defend_turns -= 1

            choice = combat_choice()  # lets you choose your next move

            if choice == "attack":  # d20 attack to see if you can deal damage
                enemy.health = basic_attack(self.stat_ability["str_ability"], enemy.ac, enemy.health)
                if enemy.health < 1:
                    print(f'You defeated the {enemy.name}\n')
                    return
                print(f'The {enemy.name} has {enemy.health} health left.\n')

            elif choice == "flee":  # it's basically just a d20 plus mod to see if you escape.
                escape = flee(self.stat_ability["dex_ability"], enemy.dex)
                if escape:
                    print(f'You escaped the {enemy.name}\n')
                    return
                else:
                    print("You failed to escape!\n")

            elif choice == "defend":  # I don't know if I need the function, but I have it
                defend()
                defend_turns += 1

            if self.status["poison"]:  # it checks for poison in status, does damage, puts poison down by one
                self.status["health"] = self.status["health"] - 1
                print("You took one poison damage!")
                self.status["poison"] -= 1

            if self.status["health"] < 1:  # don't die lol
                print("You have died. Game over!")
                exit()

            #  this is the entire enemy turn lol
            self.status["health"], self.status["poison"] = enemy.combat_choice(self)  # goes into the enemy class
            print(f'You have {self.status["health"]} health left.\n')

            if self.status["health"] < 1:
                print("You have died. Game over!")
                exit()


#  Work on Monster class stuff more. A few more attacks to flesh it out a bit including a heavy attack which will
#  add a reason to use the defence skill. add more non-combat encounters because that is something that currently
#  would greatly benefit the game by adding experiences that will change how game goes. finish rest, cooking thing (inv)
#  worn down houses on the road, OH little shrines that how score checks and interactions do with them change stuff
#  like what player will more often find, power of monsters, element powers, etc.

#  Add a way for player to explore the world with a map or some kind of road that the player goes down.

#  After that add a few random characters that player can either fight or help????
#  after that add xp system so fighting also adds experience for people going in that direction.
#  make a reason for player to use multiple skills.
#  Add more story and journey. focus on the road. life is a road. make the journey like that road.
#  sometimes you learn things from just getting through stuff (xp). sometimes you learn from others (encounters).

def ability_modifier_maker():  # takes the numbers from stats and transforms them into ability modifiers.
    keys = []
    for key in player.stat_ability.keys():
        keys.append(key)
    values = []
    for value in player.stats.values():
        values.append(value)
    for v in range(len(values)):
        values[v] = (values[v] - 10) // 2
    for r in range(len(player.stat_ability)):
        player.stat_ability[keys[r]] = values[r]


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


def stat_saver():  # will save the player info to text files
    player_data = open("player-data.txt", "r+")
    player_info = json.dumps(player.__dict__)
    player_data.write(player_info)
    player_data.close()


def stat_roll():   # Rolls all the dice needed for one stat.
    dice1, dice2, dice3, dice4 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
    num = [dice1, dice2, dice3, dice4]
    num.sort()
    num.pop(0)
    total = 0
    for a in num:
        total += a
    return total


def stat_maker():
    st, d, c, w, i, ch = stat_roll(), stat_roll(), stat_roll(), stat_roll(), stat_roll(), stat_roll()
    raw_nums = [st, d, c, w, i, ch]
    empty = []
    print(f'{st}, {d}, {c}, {w}, {i}, and {ch} are your stats')

    for s in player.stats:
        a = "a"
        while a not in raw_nums:
            x_temp = input(f"What do you want to assign to {s}?\n")
            try:
                x_temp = int(x_temp)
                if x_temp not in raw_nums:
                    print("That's not an option!")
                else:
                    a = x_temp
                    player.stats[s] = a
            except ValueError:
                print("That's not an option!")
        raw_nums.remove(player.stats[s])
        if raw_nums != empty:
            print(raw_nums)

    ability_modifier_maker()  # creates rest of player stats
    player.knownMonsters.clear()
    player.knownMonsters.append("slime")
    player.stat_reset()
    player.knowledge.clear()


def loading_system():
    player_data = open("player-data.txt", "r+")
    file_test = player_data.read()

    if file_test:
        player.__dict__ = json.loads(file_test)
        player_data.close()

        answer_options = ["yes", "no"]  # gives you the option to either load your stats or start from scratch.
        file_answer = 0
        print(f'Do you want to load your old save with stats:\n{player.stats} \nYes/No')
        while file_answer not in answer_options:
            x = input()
            if str.lower(x) in answer_options:
                file_answer = str.lower(x)
            else:
                print("please enter \'yes\' or \'no\'")

        if file_answer != "yes":
            stat_maker()  # new load out!
    else:
        stat_maker()  # new load out!


def combat_choice():  # A program to let player decide what move to do
    choices = []
    for keys, values in player.skills.items():  # takes all values in skills that are True and puts in list
        if values:
            choices.append(keys)
    choice = 0

    print(f'What do you want to do?\n')
    for x in choices:  # asks you what skill you want to use, if it isn't in your allowed skills it retries.
        print(x)
    while choice not in choices:
        choice = input()
        choice = choice.lower()
        if choice not in choices:
            print("Please choose a valid option.")
            for x in choices:
                print(x)

    return choice  # returns the choice so that other programs can use it


def basic_attack(mod, mod2, hp):  # calculates the damage and gives info to the player.
    d20roll = d20()
    attack_roll = d20roll + mod - mod2
    damage = max((random.randint(1, 6) + mod), 1)
    if d20roll == 1:
        return hp
    elif d20roll == 20:
        hp -= damage
        print(f"{damage} damage!")
        return hp
    elif attack_roll > 0:
        hp -= damage
        print(f"{damage} damage!")
        return hp
    else:
        print("Miss!")
        return hp


def flee(mod1, mod2):  # like basic attack, but with fleeing.
    d20roll = d20()
    escape_roll = (d20roll + mod1) - mod2

    if d20roll == 1:
        return False
    elif d20roll == 20:
        return True
    elif escape_roll > 0:
        return True


def defend():
    print("You defend yourself for the worst.")
    player.status["ac"] += 5


def skill_definitions():  # A program to let player read what their skills do
    skills = []
    for keys, values in player.skills.items():  # takes all values in skills that are True and puts in list
        if values:
            skills.append(keys)

    print("Your skills are:")
    for x in skills:  # easy loop to show all skills
        print(x)
    answer = input("\nWhat skill do you want to look up?\n")

    while answer != "exit":  # until user says, will continue to let player look at skills.

        if answer == "attack":
            print("\nA move to attack your enemy with great force.")
            print("Please enter another skill you want to know or type 'exit'")
            answer = input().lower()

        elif answer == "flee":
            print("\nFor times of dire need when the best option is to run away.")
            print("Please enter another skill you want to know or type 'exit'")
            answer = input().lower()

        elif answer == "defend":
            print("\nA tactic that allows you to focus on survivability, making you much harder to hit.")
            print("Please enter another skill you want to know or type 'exit'")
            answer = input().lower()

        else:
            print("Please put a valid option.")
            answer = input().lower()


player = Player()
loading_system()

command = 0
print("what do you want to do?")
while command != "quit":
    command = input()
    if command == "fight":
        random.shuffle(player.knownMonsters)
        player.basic_combat(enemies.enemy_definers(player.knownMonsters[0]))
        command = "egg"

    if command == "encounter":
        randMon = enemies.Monster(player.knownMonsters[0])
        encounters.old_man(player, randMon)
        command = "egg"

    if command == "skills":
        skill_definitions()
        command = "egg"

    if command == "stats":
        print(player.__dict__)
        command = "egg"


stat_saver()
