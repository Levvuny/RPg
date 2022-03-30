import random

poison = ["slime", "giant spider"]
easy = ["goblin", "boar", "cow", "changeling", "shadow", "skeleton"]
medium = ["giant spider"]


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
    else:
        return Monster(name, lvl)


def name_maker(name):
    random.shuffle(modifier)
    names = modifier[1] + " " + name
    return names


class Monster:
    def __init__(self, name, lvl=0):
        self.lvl = lvl  # if player doesn't put a level in, it will automatically set a level based on the name
        if lvl == 0:
            if name in easy:
                self.lvl = random.randint(1, 4)
            if name in medium:
                self.lvl = random.randint(5, 8)

        self.str = (random.randint(5, 22) - 10) // 2 + (self.lvl - 1)
        self.dex = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.con = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.wis = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.int = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.cha = (random.randint(1, 15) - 10) // 2 + (self.lvl - 1)
        self.ac = 8 + random.randint(-1, 1)
        self.health = max(random.randint(1, 5) + random.randint(1, 5) + self.con + 2, 1)
        self.name = name_maker(name)

    def basic_attack(self, player):
        print(f'The {self.name} attacks you!')
        d20roll = d20()
        attack_roll = d20roll + self.str - player.status["ac"]
        damage = max((random.randint(1, 6) + self.str), 1)

        if d20roll == 1:
            return player.status["health"], player.status["poison"]
        elif d20roll == 20:
            player.status["health"] -= damage
            print(f"{damage} damage!")
            return player.status["health"], player.status["poison"]
        elif attack_roll > 0:
            player.status["health"] -= damage
            print(f"{damage} damage!")
            return player.status["health"], player.status["poison"]
        else:
            print("Miss!")
            return player.status["health"], player.status["poison"]

    def poison(self, player):
        print(f'The {self.name} spits poison at you!')
        d20roll = d20()
        attack_roll = d20roll + self.str - player.status["ac"]
        damage = max((random.randint(1, 2) + self.str), 1)
        if d20roll == 1:
            return player.status["health"], player.status["poison"]
        elif d20roll == 20:
            player.status["health"] -= damage
            print(f"{damage} damage!")
            player.status["poison"] += 3
            return player.status["health"], player.status["poison"]
        elif attack_roll > 0:
            player.status["health"] -= damage
            print(f"{damage} damage!")
            player.status["poison"] += 2
            return player.status["health"], player.status["poison"]
        else:
            print("Miss!")
            return player.status["health"], player.status["poison"]

    def combat_choice(self, player):
        choice = random.randint(1, 2)
        if choice == 1:
            return self.basic_attack(player)
        if choice == 2:
            return self.basic_attack(player)


class Poison(Monster):
    def combat_choice(self, player):
        choice = random.randint(1, 2)
        if choice == 1:
            return self.basic_attack(player)
        elif choice == 2:
            return self.poison(player)
