import json
import random


class Items:

    def __init__(self, info, number):
        self.id = info["id"]
        self.name = info["name"]
        self.description = info["description"]
        self.value = info["value"]
        self.number = number
        self.equip_able = info["equip"]

    def examine(self):
        print(self.description)

    def use(self, player, item):
        print("You aren't sure what you want to do with this.")


"""
types:

1 = usable
2 = food
3 = craft-able
4 = armor
5 = weapon
"""


class Equipable(Items):
    def __init__(self, info, number):
        super().__init__(info, number)
        self.bonus = info["bonus"]
        self.weapon_type = info["weapon_type"]
        self.weapon_bonus = info["weapon_bonus"]

    def equip(self, player):

        if player.equip[self.weapon_type]:
            self.dequip(player)
        player.stat_ability[self.weapon_bonus] += self.bonus
        player.equip[self.weapon_type] = list((self.bonus, self.weapon_bonus, self.name))

    def dequip(self, player):
        player.stat_ability[player.equip[self.weapon_type][1]] -= player.equip[self.weapon_type][0]


class Armor(Equipable):
    def __init__(self, info, number):
        super().__init__(info, number)


class Weapon(Equipable):
    def __init__(self, info, number):
        super().__init__(info, number)
        self.special = info["special"]

    def equip(self, player):

        special_placeholder = None
        if self.special:
            special_placeholder = self.special_move()

        if player.equip[self.weapon_type]:
            self.dequip(player)
        player.stat_ability[self.weapon_bonus] += self.bonus
        player.equip[self.weapon_type] = list((self.bonus, self.weapon_bonus, self.name, special_placeholder))

    def special_move(self):
        mod = random.randint(1, int(self.special["roll_mod"]))  # calculates the actual roll mod
        self.special["roll_mod"] = mod
        return self.special  # returns a dictionary like most attacks. might change more later?


class UseAbles(Items):
    def __init__(self, info, number):
        super().__init__(info, number)


class Food(UseAbles):

    def __init__(self, info, number):
        super().__init__(info, number)
        self.heal = info["heal"]
        self.message = "You eat the " + self.name

    def use(self, player, item):
        print(self.message)
        player.status["health"] += self.heal
        if player.status["health"] > player.status["max_health"]:
            player.status["health"] = player.status["max_health"]
        player.inv[str(item)] -= 1


class CraftAbles(UseAbles):
    def __init__(self, info, number):
        super().__init__(info, number)


read = open("item-data.json", "r")
read = json.loads(read.read())


def item_definer(info, number):
    if info["type"] == 1:
        return UseAbles(info, number)
    if info["type"] == 2:
        return Food(info, number)
    if info["type"] == 3:
        return CraftAbles(info, number)
    if info["type"] == 4:
        return Armor(info, number)
    if info["type"] == 5:
        return Weapon(info, number)
