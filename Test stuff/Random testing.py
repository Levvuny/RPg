
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
import numpy as np
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


# img = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# te, imge = img.read()
# cv2.imwrite("test_img.png", imge)
# image = cv2.imread("test_img.png", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# # fourcc = cv2.VideoWriter_fourcc(*'XVID')
# # out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
# pts = np.array(([20, 20], [50, 50], [100, 199]), np.int32)
# # pts = pts.reshape((-1, 1, 2))
# font = cv2.FONT_HERSHEY_SIMPLEX
# hi, mom = cap.read()
# pic = mom
#
# while True:
#     ret, frame = cap.read()
#     pic += frame
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # out.write(frame)
#     # cv2.circle(gray, (350, 200), 50, (255, 0, 0))
#
#     # cv2.putText(frame, "Hello, mother", (300, 40), font, 1, (200, 100, 200))
#     # cv2.polylines(gray, [pts], True, (255, 0, 0))
#     cv2.imshow("gray", gray)
#
#     cv2.imshow("color", frame)
#     rec = frame[250:400, 150:300]
#     frame[0:150, 0:150] = rec
#     cv2.rectangle(frame, (250, 150), (400, 300), (0, 0, 255), 5)
#     cv2.imshow("line", frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# # # out.release()
# cv2.destroyAllWindows()
# cv2.imshow("o", pic)

img1 = cv2.imread("test_img.png", cv2.IMREAD_COLOR)
img2 = cv2.imread("test_img2.png", cv2.IMREAD_COLOR)


cv2.waitKey(0)
img3 = cv2.imread("politefroggo_2_112x1122.png", cv2.IMREAD_COLOR)

rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]  # roi = range of interest

gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
cv2.imshow("s", gray)
ret, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

cv2.imshow("mask", mask)

mask_inv = cv2.bitwise_not(mask)
cv2.imshow("e",mask_inv)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow("d", img1_bg)
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)
cv2.imshow("dd", img3_fg)

dst = cv2.add(img1_bg, img3_fg)
cv2.imshow(":D", dst)
img1[0:rows, 0:cols] = dst

cv2.imshow("img", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()