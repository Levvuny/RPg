import random

hotdog = ["greg", "smurgus"]
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
    if name in hotdog:
        return SmurgusTheHotdogMan(name, lvl)
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
    if name in hotdog:
        return name
    else:
        random.shuffle(modifier)
        names = modifier[1] + " " + name
        return names


class Monster:
    def __init__(self, name, lvl):
        self.type = "enemy"
        self.lvl = level_setter(lvl, name)
        self.name = name_maker(name)
        self.str = (random.randint(5, 20) - 10) // 2 + (self.lvl - 1)  # something needs to happen here
        self.dex = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.con = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.wis = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.int = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.cha = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.ac = 8 + random.randint(-1, 1)  # turn this into a function that is defined by name like lvl?
        self.health = max(random.randint(1, (5 + self.lvl)) + random.randint(1, (5 + self.lvl)) + self.con + 2, 1)
        self.fire = 0
        self.poison = 0
        self.defense = 0
        self.resistance = []
        self.attacks = [self.basic_attack]
        self.charging = []

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
                "damage": int(max(random.randint(1, 10) + self.str, 1)),
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
        if self.charging:
            return self.charging[0]()
        else:
            random.shuffle(self.attacks)
            return self.attacks[0]()


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
            "debuff_turns": 0,
            "success_hit": f'Hork hork hork, my hotdogs are great for your health!!!!',
            "weak_hit": f'This message should never happen.'
        }
        return info
