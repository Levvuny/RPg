import cv2
import numpy as np
import random
import time


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

number = input("How many frames per shot?\n")
divide = input("How much do you want to divide it?\n")
list_amount = []
number = int(number)
for n in range(number):
    list_amount.append(n)

def crack_starter():
    for item in range(len(list_amount)):
        ret, frame = cap.read()
        if ret:
            new_frame = frame // int(divide)
            frame = new_frame
            list_amount[item] = frame


def data_changer(key):
    global divide
    if key == 119:
        divide = int(divide) + 1
        return

    if key == 115:
        if int(divide) > 0:
            divide = int(divide) - 1
            int(divide)
            return

        else:
            return

    if key == 43:
        ret, frame = cap.read()
        if ret:
            new_frame = frame // int(divide)
            frame = new_frame
            list_amount.append(frame)
            return

    if key == 45:
        if len(list_amount) == 1:
            return

        else:
            list_amount.pop()
            return



def crack():
    crack_starter()
    global key
    while True:

        for item in range(len(list_amount)):

            ret, frame = cap.read()
            if ret:
                new_frame = frame // int(divide)
                frame = new_frame
                list_amount[item] = frame
            for items in range(len(list_amount)):
                if items != item:

                    list_amount[items] += list_amount[item]

            if (item + 1) in range(len(list_amount)):
                mod = item + 1
            else:
                mod = 0

            all = frame + list_amount[mod]
            cv2.imshow("crackhead", all)
            key = cv2.waitKey(1) & 0xFF


        print(key)
        if key == 119 or key == 115 or key == 43 or key == 45:
            data_changer(key)
        if key == ord('q'):
            break



crack()
