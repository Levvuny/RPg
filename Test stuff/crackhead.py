import cv2
import numpy as np
import random
import time


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

ret, frame = cap.read()
A = frame
one = frame

ret, frame = cap.read()

one += frame
two = frame

ret, frame = cap.read()

one += frame
two += frame
three = frame

ret, frame = cap.read()

one += frame
two += frame
three += frame
four = frame

ret, frame = cap.read()

one += frame
two += frame
three += frame
four += frame
five = frame

ret, frame = cap.read()

one += frame
two += frame
three += frame
four += frame
five += frame
six = frame

ret, frame = cap.read()

one += frame
two += frame
three += frame
four += frame
five += frame
six += frame
seven = frame

ret, frame = cap.read()

one += frame
two += frame
three += frame
four += frame
five += frame
six += frame
seven += frame
eight = frame

ret, frame = cap.read()

one += frame
two += frame
three += frame
four += frame
five += frame
six += frame
seven += frame
eight += frame
nine = frame

ret, frame = cap.read()

one += frame
two += frame
three += frame
four += frame
five += frame
six += frame
seven += frame
eight += frame
nine += frame
ten = frame

while True:
    ret, frame = cap.read()
    A = frame + two
    two += frame
    three += frame
    four += frame
    five += frame
    six += frame
    seven += frame
    eight += frame
    nine += frame
    ten += frame
    one = frame
    cv2.imshow("f", A)
    cv2.waitKey(1)

    ret, frame = cap.read()
    A = frame + three
    one += frame
    three += frame
    four += frame
    five += frame
    six += frame
    seven += frame
    eight += frame
    nine += frame
    ten += frame
    two = frame
    cv2.imshow("f", A)
    cv2.waitKey(1)

    ret, frame = cap.read()
    A = frame + four
    one += frame
    two += frame
    four += frame
    five += frame
    six += frame
    seven += frame
    eight += frame
    nine += frame
    ten += frame
    three = frame
    cv2.imshow("f", A)
    cv2.waitKey(1)

    ret, frame = cap.read()
    A = frame + five
    one += frame
    two += frame
    three += frame
    five += frame
    six += frame
    seven += frame
    eight += frame
    nine += frame
    ten += frame
    four = frame
    cv2.imshow("f", A)
    cv2.waitKey(1)

    ret, frame = cap.read()
    A = frame + six
    one += frame
    two += frame
    three += frame
    four += frame
    six += frame
    seven += frame
    eight += frame
    nine += frame
    ten += frame
    five = frame
    cv2.imshow("f", A)
    cv2.waitKey(1)

    ret, frame = cap.read()
    A = frame + seven
    one += frame
    two += frame
    three += frame
    four += frame
    five += frame
    seven += frame
    eight += frame
    nine += frame
    ten += frame
    six = frame
    cv2.imshow("f", A)
    cv2.waitKey(1)

    ret, frame = cap.read()
    A = frame + eight
    one += frame
    two += frame
    three += frame
    four += frame
    five += frame
    six += frame
    eight += frame
    nine += frame
    ten += frame
    seven = frame
    cv2.imshow("f", A)
    cv2.waitKey(1)

    ret, frame = cap.read()
    A = frame + nine
    one += frame
    two += frame
    three += frame
    four += frame
    five += frame
    six += frame
    seven += frame
    eight = frame
    nine += frame
    ten += frame
    cv2.imshow("f", A)
    cv2.waitKey(1)

    ret, frame = cap.read()
    A = frame + ten
    one += frame
    two += frame
    three += frame
    four += frame
    five += frame
    six += frame
    seven += frame
    eight += frame
    nine = frame
    cv2.imshow("f", A)
    cv2.waitKey(1)

    ret, frame = cap.read()
    A = frame + one
    one += frame
    two += frame
    three += frame
    four += frame
    five += frame
    six += frame
    seven += frame
    eight += frame
    nine += frame
    ten = frame
    cv2.imshow("f", A)
    cv2.waitKey(1)

# while True:
#     ret, frame = cap.read()
#     ree = frame
#
#     for x in range(2):
#         ret, frame = cap.read()
#         ree += frame
#     cv2.imshow("test", ree)
#     cv2.waitKey(1)
