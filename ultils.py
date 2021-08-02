import cv2
import pyautogui
import autopy
import HandTrackingModule as htm
from VolumnControl import *


wCam, hCam = 640, 480
cap = cv2.VideoCapture('your_video.avi')
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]



def countFinger(img):
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)


        # print(fingers)
        # totalFingers = fingers.count(1)
        return  fingers


def SoNgonTay(fingers, wScr, hScr):
    wImg = 1920
    hImg = 1080
    if fingers != None:
        i = fingers.count(1)
        print(i)

        if i == 2 and fingers[1] == 1 and fingers[2] == 1:
            TaTQQDuoi(wScr, hScr, wImg, hImg)
        elif i == 4 and fingers[0] == 0:
            TatQQHDuoi(wScr, hScr, wImg, hImg)
        elif i == 3 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1:
            TangVolume(wScr, hScr, wImg, hImg)
        elif i == 5:
            GiamVoLume(wScr, hScr, wImg, hImg)




def TaTQQDuoi(wScr, hScr, wImg, hImg):
    print('TaTQQDuoi')
    scaleX = wImg / wScr
    scaleY = hImg / hScr
    x3 = 1783 / scaleX
    y3 = 931 / scaleY
    # print(f'tao do bam {x3}/{y3}')
    autopy.mouse.move(x3, y3)
    autopy.mouse.click()
    time.sleep(5)


def TatQQHDuoi(wScr, hScr, wImg, hImg):
    print('TatQQHDuoi')
    scaleX = wImg / wScr
    scaleY = hImg / hScr
    x3 = 1399 / scaleX
    y3 = 890 / scaleY
    # print(f'tao do bam {x3}/{y3}')
    autopy.mouse.move(x3, y3)
    autopy.mouse.click()
    time.sleep(5)


def TangVolume(wScr, hScr, wImg, hImg):
    TangVolumnTo()


def GiamVoLume(wScr, hScr, wImg, hImg):
    GiamVolumnNho()