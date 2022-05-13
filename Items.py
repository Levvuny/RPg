

class Items:

    def __init__(self, info):
        self.id = info["id"]
        self.name = info["name"]
        self.description = info["description"]
        self.value = info["value"]

    def examine(self):
        print(self.description)


"""
types:

1 = usable
2 = food
3 = craftable
4 = armor
5 = weapon
"""


class UseAbles(Items):
    def __init__(self, info):
        super().__init__(info)


class Food(UseAbles):

    def __init__(self, info):
        super().__init__(info)
        self.heal = info["heal"]
        self.message = "You eat the " + self.name

    def use(self, player):
        print(self.message)
        player.health += self.heal
        if player.health > player.max_health:
            player.health = player.max_health


class CraftAbles(UseAbles):
    def __init__(self, info):
        super().__init__(info)


import json
read = open("item-data.json", "r")
read = json.loads(read.read())

for x in read["items"]:
    if x["type"] == 3:
        y = CraftAbles(x)
        print(y.name)


