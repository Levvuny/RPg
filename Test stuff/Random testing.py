import pandas as pd
import random
import requests
import json
#
# EnemySheet = requests.get("https://sheets.googleapis.com/v4/spreadsheets/1_Ym0miRRwRvT6j0cTkbwEgiiZ9GImDkJqhR7OAw33R8/values/Sheet1?key=AIzaSyB5DWWVzSER7OpXYIFVuhq0KysBzQocy7U")
#
# EnemySheet = EnemySheet.json()
#
# EnemyInfo = pd.DataFrame(EnemySheet["values"], columns=EnemySheet["values"][0])
# EnemyInfo.drop(index=0, inplace=True)
#
# monsterNames = []
#
# for x in EnemyInfo["Name"]:
#     monsterNames.append(x)
# # monsters = {
# #     "Key": ["Mon1", "Mon2", "Mon3", "Mon4"],
# #     "Name": ["Slime", "Bat", "Fire Wisp", "Crab"],
# #     "Type": ["Poison" " Fire" " Lightning", "Air", "Fire", "Normal"]
# # }
# #
# # MonsterData = pd.DataFrame(monsters)
#
#
#
# print(monsterNames)
#
# # print(df)
#
#
# def level_setter(name, level):
#     if name in EnemyInfo.values:
#         if level != 0:
#             return level
#         row_finder = EnemyInfo.loc[EnemyInfo["Name"] == name, "Difficulty"]
#         if "easy" in row_finder.values:
#             lvl = random.randint(1, 4)
#             return lvl
#         if "medium" in row_finder.values:
#             lvl = random.randint(5, 8)
#             return lvl
#         if "hard" in row_finder.values:
#             lvl = random.randint(9, 14)
#             return lvl
#         if "legendary" in row_finder.values:
#             lvl = random.randint(15, 20)
#             return lvl
#         else:
#             lvl = 0
#             return lvl
#     else:
#         return 0
#
#
# print(level_setter("fire wisp", 0))
# # class Monster:
# #     def __init__(self, name):
# #         self.type = "enemy"
# #         self.lvl = level_setter(name)
# #         self.name = name
# #
# #
# # mon = Monster("fire wisp")
# # print(mon.__dict__)
# #
# # print(df.values)
#
# import json
# import requests
# # from bs4 import BeautifulSoup
#
# spells = requests.get("https://www.dnd5eapi.co/api/spells/")
# spells = spells.json()
# # if spells["attack_type"] == "ranged":
# #     print("Yay")
# # print(spells["desc"])
#
# acid_spells = []
# # print(spells["results"][0])
# # type = input("What type of spell?\n")
# # for value in range(len(spells["results"])):
# #     # print(spells["results"][value]["name"])
# #     if type in (spells["results"][value]["name"]).lower():
# #         acid_spells.append(spells["results"][value]["url"])
# # print(acid_spells)
# # url_base = "https://www.dnd5eapi.co"
# #
# # for spells in acid_spells:
# #     url = url_base + spells
# #     spell = requests.get(url)
# #     spell = spell.json()
# #     print(spell["name"])
# #     print(spell["desc"])
# #     print("")
# #
import cv2
import numpy
import matplotlib


# vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#
# while(True):
#
#     # Capture the video frame
#     # by frame
#     ret, frame = vid.read()
#
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
#
#     # the 'q' button is set as the
#     # quitting button you may use any
#     # desired button of your choice
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # After the loop release the cap object
# vid.release()
# # Destroy all the windows
# cv2.destroyAllWindows()


img = cv2.VideoCapture(0, cv2.CAP_DSHOW)
te, imge = img.read()
cv2.imwrite("test_img.png", imge)
image = cv2.imread("test_img.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
