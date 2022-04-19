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

import json
import requests
from bs4 import BeautifulSoup

spells = requests.get("https://www.dnd5eapi.co/api/spells/")
spells = spells.json()
# if spells["attack_type"] == "ranged":
#     print("Yay")
# print(spells["desc"])

# acid_spells = []
# print(spells["results"][0])
# type = input("What type of spell?\n")
# for value in range(len(spells["results"])):
#     # print(spells["results"][value]["name"])
#     if type in (spells["results"][value]["name"]).lower():
#         acid_spells.append(spells["results"][value]["url"])
# print(acid_spells)
# url_base = "https://www.dnd5eapi.co"
#
# for spells in acid_spells:
#     url = url_base + spells
#     spell = requests.get(url)
#     spell = spell.json()
#     print(spell["name"])
#     print(spell["desc"])
#     print("")
#
t = requests.get("https://script.google.com/macros/library/d/1Kc4CqAH_0yhtqX6-WyxEDEFflJbrmdyLAn3tmkPPiRp3WTEfjgNTXIhS/1")

print(t.text)