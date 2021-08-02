import autopy as autopy

from ultils import *




wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
cap.set(3, wCam)
cap.set(4, hCam)


wScr, hScr = autopy.screen.size()

while True:
    success, imgCam = cap.read()
    fingers = countFinger(imgCam)
    print(f'{fingers} ')
    SoNgonTay(fingers,wScr, hScr)
    cv2.imshow('cam', imgCam)
    cv2.waitKey(1)
cap.release()
cv.destroyAllWindows()