

class Items:

    def __init__(self, info):
        self.id = info["id"]
        self.name = info["name"]
        self.description = info["description"]
        self.value = info["value"]

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
    def __init__(self, info):
        super().__init__(info)

class Weapon(Items):
    def __init__(self, info):
        super().__init__(info)
        if
class UseAbles(Items):
    def __init__(self, info):
        super().__init__(info)


class Food(UseAbles):

    def __init__(self, info):
        super().__init__(info)
        self.heal = info["heal"]
        self.message = "You eat the " + self.name

    def use(self, player, item):
        print(self.message)
        player.status["health"] += self.heal
        if player.status["health"] > player.status["max_health"]:
            player.status["health"] = player.status["max_health"]
        player.inv[str(item)] -= 1


class CraftAbles(UseAbles):
    def __init__(self, info):
        super().__init__(info)


import json
read = open("item-data.json", "r")
read = json.loads(read.read())

def item_definer(info):
    if info["type"] == 1:
        return UseAbles(info)
    if info["type"] == 2:
        return Food(info)
    if info["type"] == 3:
        return CraftAbles(info)