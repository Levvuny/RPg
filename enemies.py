import random

fire = ["fire wisp"]
poison = ["slime", "giant spider"]
easy = ["goblin", "boar", "cow", "changeling", "shadow", "skeleton",]
medium = ["giant spider", "fire wisp"]


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


modifier = ["lazy", "fabulous", "cringe", "random", "wild", "sad", "all-knowing", "playboy", "fishy", "green",
            "light green", "ugly", "eccentric"]


def enemy_definers(name, lvl=0):
    if name in poison:
        return Poison(name, lvl)
    elif name in fire:
        return Fire(name, lvl)
    else:
        return Monster(name, lvl)


def level_setter(lvl, name):  # will set the monster level if not already set by specific number
    if lvl != 0:
        return lvl
    else:
        if name in easy:
            lvl = random.randint(1, 4)
            return lvl
        if name in medium:
            lvl = random.randint(5, 8)
            return lvl
        else:
            lvl = 0
            return lvl


def name_maker(name):
    random.shuffle(modifier)
    names = modifier[1] + " " + name
    return names


class Monster:
    def __init__(self, name, lvl):
        self.type = "enemy"
        self.lvl = level_setter(lvl, name)
        self.str = (random.randint(5, 22) - 10) // 2 + (self.lvl - 1)
        self.dex = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.con = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.wis = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.int = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.cha = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.ac = 8 + random.randint(-1, 1)
        self.health = max(random.randint(1, (5 + self.lvl)) + random.randint(1, (5 + self.lvl)) + self.con + 2, 1)
        self.name = name_maker(name)
        self.fire = 0
        self.poison = 0
        self.defense = 0
        self.resistance = []

    def basic_attack(self):

        info = {
            "roll_mod": self.str,
            "damage": int(max(random.randint(1, 2) + self.str, 1)),
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

    def combat_choice(self,):
        choice = random.randint(1, 2)
        if choice == 1:
            return self.basic_attack()
        if choice == 2:
            return self.basic_attack()


class Poison(Monster):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)
        self.resistance.append("poison")

    def combat_choice(self):
        choice = random.randint(1, 2)
        if choice == 1:
            return self.basic_attack()
        elif choice == 2:
            return self.poison_attack()


class Fire(Monster):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)
        self.resistance.append("fire")
