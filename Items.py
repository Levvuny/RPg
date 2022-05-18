import json

class Items:

    def __init__(self, info, number):
        self.id = info["id"]
        self.name = info["name"]
        self.description = info["description"]
        self.value = info["value"]
        self.number = number

    def examine(self):
        print(self.description)

    def use(self, player, item):
        print("You aren't sure what you want to do with this.")


"""
types:

1 = usable
2 = food
3 = craftable
4 = armor
5 = weapon
"""


class Armor(Items):
    def __init__(self, info, number):
        super().__init__(info, number)


class Weapon(Items):
    def __init__(self, info, number):
        super().__init__(info, number)
        self.bonus = info["bonus"]
        self.weapon_type = info["weapon_type"]
        self.weapon_bonus = info["weapon_bonus"]
        self.equip_able = info["equip"]


    def equip(self, player):

        if player.equip[self.weapon_type]:
            pass
        player.stat_ability[self.weapon_bonus] += self.bonus
        player.equip[self.weapon_type] = self.bonus
        player.equip["weapon_type"] = self.weapon_bonus



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
