import pandas as pd
import random

# monsters = {
#     "Key": ["Mon1", "Mon2", "Mon3", "Mon4"],
#     "Name": ["Slime", "Bat", "Fire Wisp", "Crab"],
#     "Type": ["Poison" " Fire" " Lightning", "Air", "Fire", "Normal"]
# }
#
# MonsterData = pd.DataFrame(monsters)
df = pd.read_csv("enemies.csv")
monsterNames = []

for x in df["Name"].values:
    monsterNames.append(x)

print(monsterNames)

print(df["Name"].values)


def level_setter(name, level):
    if name in df.values:
        if level != 0:
            return level
        row_finder = df.loc[df["Name"] == name, "Difficulty"]
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
        return 10000


print(level_setter("fire wisp", 0))
# class Monster:
#     def __init__(self, name):
#         self.type = "enemy"
#         self.lvl = level_setter(name)
#         self.name = name
#
#
# mon = Monster("fire wisp")
# print(mon.__dict__)
#
# print(df.values)

import requests

response = requests.get("https://docs.google.com/spreadsheets/d/1_Ym0miRRwRvT6j0cTkbwEgiiZ9GImDkJqhR7OAw33R8/edit#gid=0&range=A1:C4")
response.json()
# response = pd.read_csv(response)


# response = requests.get("https://docs.python.org/3/c-api/index.html")



print(response.text)