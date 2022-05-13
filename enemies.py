import pandas as pd
import random
import requests

EnemySheet = requests.get("https://sheets.googleapis.com/v4/spreadsheets/1_Ym0miRRwRvT6j0cTkbwEgiiZ9GImDkJqhR7OAw33R8"
                          "/values/Sheet1?key=AIzaSyB5DWWVzSER7OpXYIFVuhq0KysBzQocy7U")

EnemySheet = EnemySheet.json()

LootSheet = requests.get(
    "https://sheets.googleapis.com/v4/spreadsheets/1_Ym0miRRwRvT6j0cTkbwEgiiZ9GImDkJqhR7OAw33R8"
    "/values/Sheet2?key=AIzaSyB5DWWVzSER7OpXYIFVuhq0KysBzQocy7U")
LootSheet = LootSheet.json()  # the data for loot information

EnemyInfo = pd.DataFrame(EnemySheet["values"], columns=EnemySheet["values"][0])
EnemyInfo.drop(index=0, inplace=True)

type_dict = {

}

modifier = ["lazy", "fabulous", "cringe", "random", "wild", "sad", "all-knowing", "playboy", "fishy", "green",
            "light green", "ugly", "eccentric"]


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


def type_definers():
    types = []  # this list is uses to get all available monster types
    for section in EnemyInfo["Type"]:  # searches each monster for their type
        if section not in types:  # if the list doesn't have the type, it adds it
            types.append(section)

    for item in types:  # for each monster type, it adds a list to the type dictionary.
        type_dict[item] = []

    for dicts in type_dict:  # cycles through the type dictionaries in the dictionary of them
        for name in EnemyInfo["Name"]:  # also cycles through enemy list by name
            row_finder = EnemyInfo.loc[EnemyInfo["Name"] == name, "Type"]  # finds the row by the name and gets the type
            if row_finder.values == dicts:  # if the monster has the right type adds it to the dictionary
                type_dict[dicts].append(name)  # adds it so that it can be used in other programs to know its type


type_definers()


def enemy_definers(name, lvl=0):  # returns type of monster based on their type data
    if name in type_dict["poison"]:
        return Poison(name, lvl)

    elif name in type_dict["fire"]:
        return Fire(name, lvl)

    if name in type_dict["hotdog"]:
        return SmurgusTheHotdogMan(name, lvl)

    else:
        return Monster(name, lvl)


def loot_info(name):  # is used to get the loot for when monster slain

    if name in EnemyInfo["Name"].values:  # is getting the info so that it can call the specific loot item
        info = EnemyInfo.loc[EnemyInfo["Name"] == name, "Loot"]
        info = list(info)
        info = info[0].split(",")  # getting numbers seperated so that it can be used as a range
        randomLoot = random.randint(int(info[0]), int(info[1]))  # takes loot number from monster info and randomizes

        loot = LootSheet["values"][randomLoot]
        amount = loot[1]
        amount = list(amount.split(", "))  # splits it by getting rid of space and comma and only leaves number values
        amount = random.randint(int(amount[0]), int(amount[1]))  # uses numbers to generate amount of loot

        LootList = [int(loot[0]), amount]

        return LootList

    else:  # no name no loot XD
        return


def level_setter(name, level):  # will set the monster level if not already set by specific number
    if name in EnemyInfo["Name"].values:
        if level != 0:
            return level
        row_finder = EnemyInfo.loc[EnemyInfo["Name"] == name, "Difficulty"]  # finds the difficulty of mon using name

        if "easy" in row_finder.values:
            lvl = random.randint(1, 4)
            return lvl
        if "medium" in row_finder.values:
            lvl = random.randint(5, 8)
            return lvl
        if "hard" in row_finder.values:
            lvl = random.randint(9, 14)
            return lvl
        if "legendary" in row_finder.values:
            lvl = random.randint(15, 20)
            return lvl
        else:
            lvl = 0
            return lvl

    else:
        return 0


def name_maker(name):
    if name in type_dict["hotdog"]:
        return name
    else:
        random.shuffle(modifier)
        names = modifier[1] + " " + name
        return names


class Monster:
    def __init__(self, name, lvl):
        self.type = "enemy"
        self.lvl = level_setter(name, lvl)
        self.name = name_maker(name)
        self.str = (random.randint(1, 20) - 10) // 2 + (self.lvl - 1)  # something needs to happen here
        self.dex = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.con = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.wis = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.int = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.cha = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.ac = 8 + random.randint(-1, 1)  # turn this into a function that is defined by name like lvl?
        self.health = self.health_def(name)
        self.max_health = self.health
        self.fire = 0
        self.poison = 0
        self.defense = 0
        self.resistance = []
        self.attacks = [self.basic_attack]
        self.charging = []
        self.loot = loot_info(name)

    def health_def(self, name):
        if name in EnemyInfo["Name"].values:
            row_finder = EnemyInfo.loc[EnemyInfo["Name"] == name, "Difficulty"]  # finds the dif of mon using name
            if "easy" in row_finder.values:
                health = random.randint(1, 6) + random.randint(1, 6) + self.lvl
                return health
            if "medium" in row_finder.values:
                health = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + self.lvl
                return health
            if "hard" in row_finder.values:
                health = random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8)\
                         + random.randint(1, 8) + self.lvl
                return health
            if "legendary" in row_finder.values:
                health = random.randint(1, 12) + random.randint(1, 12) + random.randint(1, 12) + random.randint(1, 12) \
                         + random.randint(1, 12) + random.randint(1, 12) + self.lvl
                return health
        else:
            health = random.randint(1, 6) + random.randint(1, 6) + self.lvl
            return health

    def basic_attack(self):

        info = {
            "roll_mod": self.str,
            "damage": int(max(random.randint(1, 4) + self.str, 1)),
            "damage_type": "basic",
            "debuff_turns": 0,
            "success_hit": f'The {self.name} rams into you!',
            "weak_hit": f'The {self.name} bounces off of you, barely hurting you.'
            }
        return info

    def poison_attack(self):

        info = {
            "roll_mod": self.str,
            "damage": int(max(random.randint(1, 2) + self.str, 1)),
            "damage_type": "poison",
            "debuff_turns": 6,
            "success_hit": f'The {self.name} spits poison at you!',
            "weak_hit": f'The {self.name} spits poison at you, but you dodge most of it.'
        }
        return info

    def fire_blast(self):
        if self.fire_blast in self.charging:
            info = {
                "roll_mod": self.str + 5,
                "damage": int(max(random.randint(4, 10) + self.str, 1)),
                "damage_type": "fire",
                "debuff_turns": 3,
                "success_hit": f'The {self.name} slams into you, burning you to the core.',
                "weak_hit": f'The {self.name} slams a blast of fire into you, but you resist the onslaught.'
            }
            self.charging.remove(self.fire_blast)
            return info
        else:
            info = {
                "roll_mod": self.str + 500,
                "damage": 0,
                "damage_type": "charging",
                "debuff_turns": 0,
                "success_hit": f'The {self.name} charges a great attack.',
                "weak_hit": f'The {self.name} charges a great attack.'
            }
            self.charging.append(self.fire_blast)
            return info

    def combat_choice(self):
        if self.charging:  # if the enemy is charging an attack, it will do that attack.
            return self.charging[0]()
        else:
            random.shuffle(self.attacks)
            return self.attacks[0]()

    def healing_flames(self):  # healing spell for mon
        info = {
            "roll_mod": 9999999,
            "damage": 0,
            "damage_type": "charging",
            "debuff_turns": 0,
            "success_hit": f'The {self.name} sets itself on fire, healing itself!',
            "weak_hit": f'Do not see this message.'
            }
        self.health += self.int + random.randint(1, 4)
        if self.health > self.max_health:
            self.health = self.max_health
        return info


class Poison(Monster):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)
        self.resistance.append("poison")
        self.attacks.append(self.poison_attack)


class Fire(Monster):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)
        self.resistance.append("fire")
        self.attacks.append(self.fire_blast)
        self.attacks.append(self.healing_flames)


class Water(Monster):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)
        self.resistance.append("water")


class Air(Monster):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)
        self.resistance.append("air")


class Earth(Monster):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)
        self.resistance.append("earth")
        self.resistance.append("basic")


class SmurgusTheHotdogMan(Monster):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)
        self.resistance.append("hotdog")
        self.resistance.append("shmeat")
        self.attacks.remove(self.basic_attack)
        self.attacks.append(self.hotdogs)

    def hotdogs(self):
        info = {
            "roll_mod": self.str + 500,
            "damage": -2,
            "damage_type": "HOTDOG",
            "attack_type": False,
            "debuff_turns": 0,
            "success_hit": f'Hork hork hork, my hotdogs are great for your health!!!!',
            "weak_hit": f'This message should never happen.'
        }
        return info
