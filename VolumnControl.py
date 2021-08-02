import time
from ctypes import cast, POINTER

import cv2
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0

def TangVolumnTo():
    curVolum = volume.GetMasterVolumeLevel()
    curVolum = curVolum + 1
    print(curVolum)
    if curVolum <= maxVol:
        volume.SetMasterVolumeLevel(curVolum, None)
        time.sleep(0.5)

def GiamVolumnNho():
    curVolum = volume.GetMasterVolumeLevel()
    curVolum = curVolum - 1
    print(curVolum)
    if curVolum >= minVol:
        volume.SetMasterVolumeLevel(curVolum, None)
        time.sleep(0.5)

if __name__=="__main__":
    while True:

        cv2.waitKey(1)