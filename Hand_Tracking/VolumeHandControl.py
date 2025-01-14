# Reference: https://www.youtube.com/watch?v=9iEPzbG-xLE&list=PLMoSUbG1Q_r8jFS04rot-3NzidnV54Z2q&ab_channel=Murtaza%27sWorkshop-RoboticsandAI

import cv2
import time
import numpy as np
from scipy.spatial.distance import euclidean
import HandTrackingModule as htm #Custom Hand Tracking Module


###### Pycaw (Python Core Audio Windows) ###### #https://github.com/AndreMiras/pycaw
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None) # Accesses Windows Core Audio API for volume control
volume = interface.QueryInterface(IAudioEndpointVolume)
volRange = volume.GetVolumeRange()
print(volRange) #(-65.25, 0.0, 0.03125) - min, max, step size (decibels)
# Note: 0dB is often the reference volume for the loudest possible sound level and anything below that is quieter. Hence the negative values.
minVol = volRange[0]
maxVol = volRange[1]
##############################
vol = 0
volBar = 400
volPercent = 100
wCam, hCam = 1280, 960 # camera width, height

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.HandDetector(minDetectionConfidence = 0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img) # Drawing hand detection
    lmList = detector.findPosition(img, draw=False) # Finding hand landmarks
    # print(lmList) # Printing coordinates for each hand landmark
    
    # We want to control the volume with the thumb and index finger
    # so we need to check if the thumb and index finger landmarks are detected
    if lmList: # If list is empty, no hand landmarks are detected

        print(lmList[4], lmList[8])


        # Thumb and Index finger landmarks
        x1, y1 = lmList[4][1], lmList[4][2] # Thumb tip (x & y coordinates)
        x2, y2 = lmList[8][1], lmList[8][2] # Index finger tip (x & y coordinates)
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2 # Center of the line between thumb and index finger tips

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED) # Thumb tip
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED) # Index finger tip
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3) # Line between thumb and index finger tips
        cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED) # Center of the line between thumb and index finger tips

        length = euclidean((x1, y1), (x2, y2)) # Euclidean distance between thumb and index finger tips
        # print(length)

        # Hand range: 60 - 290 (Checked empirically by printing the length between the points in real time)
        # Volume range: -65.25 - 0.0
        vol = np.interp(length, [60, 290], [minVol, maxVol]) # Interpolates the length to the volume range, i.e., changing the volume range based on the hand range
        volBar = np.interp(length, [60, 290], [400, 150]) # Interpolates the length to the volume bar range
        volPercent = np.interp(length, [60, 290], [0, 100]) # Interpolates the length to the volume percentage range

        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None) # Used to set the master volume level - parameters(level, event context)
        # Event context is an optional parameter that can be used to identify the context of the call. If 'None', the change is applied globally.
            
    

    if not success:
        print("Error: Could not read frame from webcam.")
        break
    
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3) # Volume bar
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 255, 0), cv2.FILLED) # Volume bar filled with yellow color
    cv2.putText(img, f'{int(volPercent)}%', (40, 450), cv2.FONT_HERSHEY_COMPLEX , 1, (255, 0, 0), 3) # Volume percentage

    cTime = time.time() # Current time  
    fps = 1/(cTime - pTime) # Frames per second
    pTime = cTime # Previous time

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_COMPLEX , 1.5, (255, 0, 0), 3) 
    # over image, text to display, position (coordinates), font, scale, color (RGB), thickness

    cv2.imshow("Image", img)
    cv2.waitKey(1)