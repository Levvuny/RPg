import random
import json
import enemies
import encounters
import combat
import Items


class Player:
    def __init__(self):
        self.type = "player"
        self.stats = {
            "str": 0,
            "dex": 0,
            "con": 0,
            "wis": 0,
            "int": 0,
            "cha": 0,
        }
        self.stat_ability = {
            "str": 0,
            "dex": 0,
            "con": 0,
            "wis": 0,
            "int": 0,
            "cha": 0,
        }
        self.status = {
            "health": 0,
            "max_health": 0,
            "ac": 0,
            "poison": 0,
            "fire": 0,
            "weakness": 0,
            "wet": 0,
            "summonGreg": 0
        }
        self.skills = {
            "attack": 1,
            "flee": 1,
            "defense": 0,
            "fire punch": 0,
        }
        self.buffs = {
            "defense": 0,
            "power": 0,
        }
        self.inv = {
        }
        self.knownMonsters = ["slime"]
        self.knowledge = []
        self.resistance = []
        self.equip = {
            "head": None,
            "body": None,
            "legs": None,
            "boots": None,
            "arms": None,
            "weapon": None
        }

    def stat_reset(self):  # maybe I need a different spot to store it all...
        health = random.randint(1, 8) + self.stat_ability["con"]
        self.status = {
            "health": health,
            "max_health": health,
            "ac": 10 + self.stat_ability["dex"],
            "poison": 0,
            "fire": 0,
            "weakness": 0,
            "wet": 0,
            "summonGreg": 0,
        }
        self.skills = {
            "attack": 1,
            "flee": 1,
            "defend": 0,
            "fire punch": 0,
        }
        self.buffs["defense"] = 0
        self.buffs["power"] = 0

        self.knownMonsters.clear()
        self.knownMonsters.append("slime")
        self.knowledge.clear()
        self.inv = {
            "1": 5
        }
        self.equip = {
            "head": None,
            "body": None,
            "legs": None,
            "boots": None,
            "arms": None,
            "weapon": []
        }

    def ability_modifier_maker(self):  # takes the numbers from stats and transforms them into ability modifiers.
        keys = []
        for key in self.stat_ability.keys():
            keys.append(key)
        values = []
        for value in self.stats.values():
            values.append(value)
        for v in range(len(values)):
            values[v] = (values[v] - 10) // 2
        for r in range(len(self.stat_ability)):
            self.stat_ability[keys[r]] = values[r]

    def fire_punch(self, enemy):  # all the info is in dict for the attack
        info = {
            "roll_mod": self.stat_ability["int"],
            "damage": int(max(random.randint(1, 6) + self.stat_ability["str"], 1)),
            "damage_type": "fire",
            "debuff_turns": 2,
            "success_hit": f'Fire engulfs your hand as you smash it into the {enemy.name}.',
            "weak_hit": f'The {enemy.name} seems to greatly resist the fire.'
        }
        return info

    def defend(self, real_ac):
        print("You defend yourself for the worst.\n")
        self.buffs["defense"] += 3
        self.status["ac"] = real_ac + 4

    def basic_attack(self, enemy):  # all the info is in dict for the attack
        info = {
            "roll_mod": self.stat_ability["str"],
            "damage": int(max(random.randint(1, 6) + self.stat_ability["str"], 1)),
            "damage_type": "basic",
            "debuff_turns": 0,
            "success_hit": f'You swing with all your might as you attack the {enemy.name}.',
            "weak_hit": f'Your attack seems to bounce off the  {enemy.name}.'
        }
        return info

    def combat_choice(self):  # A program to let player decide what move to do
        choices = []

        for keys, values in self.skills.items():  # takes all values in skills that are True and puts in list
            if values:
                choices.append(keys)

        choice = 0
        try:
            if self.equip["weapon"][3]:
                choices.append("special")
        except IndexError:
            pass  # this just makes it so that not having an item doesn't... destroy everything...
        choices.append("inv")

        print(f'What do you want to do?\n')
        for x in choices:  # asks you what skill you want to use, if it isn't in your allowed skills it retries.
            print(x)
        while choice not in choices:
            choice = input().lower()
            if choice not in choices:
                print("Please choose a valid option.")
                for x in choices:
                    print(x)

        return choice  # returns the choice so that other programs can use it


#  Work on Monster class stuff more. A few more attacks to flesh it out a bit including a heavy attack which will
#  add a reason to use the defence skill. add more non-combat encounters because that is something that currently
#  would greatly benefit the game by adding experiences that will change how game goes. finish rest, cooking thing (inv)
#  worn down houses on the road, OH little shrines that how score checks and interactions do with them change stuff
#  like what player will more often find, power of monsters, element powers, etc.
# get a staff, can cast concussion (hits with staff)

#  Add a way for player to explore the world with a map or some kind of road that the player goes down.
# figure out a small bit of api, so I can use Google sheets, if possible. if not, figure out another way to implement
# apis so that I can learn how to use them. get the basic loop of fighting and encounters down.

#  After that add a few random characters that player can either fight or help????
#  after that add xp system so fighting also adds experience for people going in that direction.
#  make a reason for player to use multiple skills.
#  Add more story and journey. focus on the road. life is a road. make the journey like that road.
#  sometimes you learn things from just getting through stuff (xp). sometimes you learn from others (encounters).


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
    player_data = open("player-data.json", "w")
    player_info = json.dumps(player.__dict__, indent=4)
    player_data.write(player_info)
    player_data.close()

    game_data = open("game-data.json", "w")
    game_info = json.dumps(game.knowledge)
    game_data.write(game_info)
    game_data.close()


def stat_roll():  # Rolls all the dice needed for one stat.
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

    player.ability_modifier_maker()  # creates rest of player stats
    player.stat_reset()


def loading_system():
    player_data = open("player-data.json", "r+")
    file_test = player_data.read()

    game_data = open("game-data.json", "r+")
    game_file = game_data.read()
    if game_data:
        game.knowledge = json.loads(game_file)
        game_data.close()

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
            game.knowledge = {
                "knowledge": [],
                "merchant": {
                    "7": 7,
                    "8": 20,
                    "9": 40
                }
            }
            stat_maker()  # new load out!
    else:
        game.knowledge = {
            "knowledge": [],
            "merchant": {
                "7": 7,
                "8": 20,
                "9": 40
            }
        }
        stat_maker()  # new load out!


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

        elif answer == "fire punch":
            print("\nA spell that enchants your fist, so that when punched into your enemy it explodes in fire.")
            print("Please enter another skill you want to know or type 'exit'")
            answer = input().lower()

        else:
            print("Please put a valid option.")
            answer = input().lower()


class Game:  # trying to make the game run as a class
    def __init__(self):
        self.commands = ["options", "continue", "save", "quit", "skills", "stats", "?", "inv", "inventory"]
        self.knowledge = {
            "knowledge": [],
            "merchant": {
                "7": 7,
                "8": 20,
                "9": 40
            }
        }
        self.inv = []

    def options(self):
        options = self.commands
        if self.knowledge["knowledge"]:
            if "travel" not in options:
                options.append("travel")
        for commands in options:
            print(commands)

    def inventory_call(self):  # everytime this is used it will update the usable inventory.
        self.inv.clear()  # resets game active inv

        read = open("item-data.json", "r")
        read = json.loads(read.read())
        for inv_item in player.inv:  # cycles through the players items and adds them into a list
            copy_item = int(inv_item)  # copies it for further use
            for items in read["items"]:  # cycles through item data
                if items["id"] == copy_item:  # now is checking if each inventory item id has item data
                    self.inv.append(Items.item_definer(items, player.inv[inv_item]))
                    # gives inv_item_new all the data from that item

    def inventory_items(self):
        self.inventory_call()

        examine_options = {}
        for x in self.inv:  # this is used so players can choose the names of items
            name = x.name
            print(f'{x.name} : {x.number}')
            examine_options[name] = x  # makes a dictionary. each name = the entire item data

        item_name = []  # this is used to let the answer see
        for x in examine_options.keys():
            item_name.append(x)

        return examine_options, item_name

    def inventory(self):
        self.inventory_call()

        print("You can either examine an item, use an item, equip an item, delete an item, or exit.")  # add delete?
        option = input().lower()
        while option != "exit":  # will let players mess with inventory.

            examine_options, item_name = self.inventory_items()

            if option == "examine":
                print("Enter the item you want to examine or type 'self' to examine yourself")
                answer = input().lower()

                while answer not in item_name:  # select thy poison
                    if answer == "exit":
                        break

                    if answer == "self":
                        empty = 0

                        for item in player.equip:
                            if player.equip[item]:
                                empty = 1
                                print(f'+{player.equip[item][0]} {player.equip[item][1]}: {player.equip[item][2]}')

                        if empty == 0:
                            print("Nothing to show here.")
                        break
                    answer = input("Please pick a valid option\n").lower()

                if answer in item_name:
                    examine_options[answer].examine()

            if option == "use":
                print("What do you want to use?")
                answer = input().lower()

                while answer not in item_name:  # select thy poison
                    if answer == "exit":
                        break
                    answer = input("Please pick a valid option\n").lower()

                if answer in item_name:
                    examine_options[answer].use(player, examine_options[answer].id)

            if option == "delete":
                print("What do you want to delete?")
                answer = input().lower()

                while answer not in item_name:  # select thy poison
                    if answer == "exit":
                        break
                    answer = input("Please pick a valid option\n").lower()

                if answer in item_name:
                    player.inv.pop(str(examine_options[answer].id))
                    print("Deleted!")

            if option == "equip":
                print("What do you want to equip?")
                answer = input().lower()

                while answer not in item_name:  # select thy poison
                    if answer == "exit":
                        break
                    answer = input("Please pick a valid option\n").lower()

                if answer == "exit":
                    break
                if examine_options[answer].equip_able:
                    examine_options[answer].equip(player)
                else:
                    print("You can't equip that!")

            if option == "strip":

                strip_list = ["head", "body", "legs", "boots", "weapon"]
                for item in strip_list:
                    if player.equip[item]:
                        player.stat_ability[player.equip[item][1]] -= player.equip[item][0]
                        player.equip[item] = []

            option = input("Type 'exit' to leave or select another option\n").lower()

    def turn_choice(self):
        random.shuffle(player.knownMonsters)
        randMon = enemies.enemy_definers(player.knownMonsters[0])

        response = input("What do you want to do?\n").lower()
        options = self.commands
        if self.knowledge["knowledge"]:
            if "travel" not in options:
                options.append("travel")

        while response not in options:
            print("Type 'options' to see commands")
            response = input().lower()

        if response == "?" or response == "options":
            self.options()

        if response == "save":
            stat_saver()

        if response == "quit":
            stat_saver()
            exit()

        if response == "skills":
            skill_definitions()

        if response == "stats":
            print(json.dumps(player.__dict__, indent=4))

        if response == "inv" or response == "inventory":
            self.inventory()  # this was so much more work than expected...

        if response == "travel":  # knowledge areas

            print("Where do you want to go?")
            for item in self.knowledge["knowledge"]:
                print(item)

            choice = input().lower()
            while choice not in self.knowledge["knowledge"]:
                choice = input("Please pick a valid option\n").lower()

            if choice == "bridge":
                encounters.damaged_bridge(player, randMon, game)

            if choice == "meadow":
                encounters.meadow(player, randMon, game)

        if response == "continue":  # this is like most of the program lol
            encounters.basic_dialogue(player, randMon, self)
            fate = random.randint(1, 2)

            if fate == 1:
                combat.combat(player, randMon, game)
            if fate == 2:
                encounters.encounter_decider(player, randMon, game)

game = Game()
player = Player()
loading_system()



while player.status["health"] > 0:
    game.turn_choice()

stat_saver()
