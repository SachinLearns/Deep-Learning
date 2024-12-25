# Reference: https://youtu.be/NZde8Xt78Iw?si=89x0wqkWhN-9dtlY

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    # Below, all variables are set with default values
    static_image_mode=False, # False: Track or Detect (switch based on the tracking confidence level; If tracking confidence goes down, perform detection again) | True: only Detect (makes it slow)
    max_num_hands=2, # Maximum number of hands to detect
    min_detection_confidence=0.5, # Minimum confidence value ([0, 1]) to consider a hand detected (if below 50%, it will not be considered)
    min_tracking_confidence=0.5 # Minimum confidence value ([0, 1]) to consider a hand tracked (if below 50%, it will perform detection again)
)

mpDraw = mp.solutions.drawing_utils # For drawing on the image


pTime = 0 # Previous time
cTime = 0 # Current time

while True:
    # To run the webcamp
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert the image to RGB; mpHands works with RGB images only
    results = hands.process(imgRGB) # Process the frame
    # print(results.multi_hand_landmarks) # To check if a hand is detected

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark): # index number (relates to the exact number of the finger landmarks, e.g., 4 indicates the tip of the thumb) and landmark ((x, y) coordinates in terms of image ratio)
                # print(id, lm) # Print the index number and the landmark  
                h, w, c = img.shape # Height, Width, and Channels of the image        
                cx, cy = int(lm.x * w), int(lm.y * h) # Convert the landmark coordinates to pixel values
                # print(id, cx, cy) # Print the index number and the pixel values

                # if id == 0: # To identify an individual landmark
                #     cv2.circle(img, (cx, cy), 15, (255, 25, 255), cv2.FILLED) 
                # # In total it has 21 landmarks (4 for the thumb, 4 for the index finger, 4 for the middle finger, 4 for the ring finger, 4 for the pinky finger, one for the palm end)
            
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) # Draw the landmarks on the original image (we aren't interested in the RGB image)

    # Calculate the frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display the frame rate
    cv2.putText(img = img, text = f'FPS: {int(fps)}', org = (10, 70), fontFace = cv2.FONT_HERSHEY_PLAIN, fontScale = 3, color = (255, 0, 255), thickness = 3)


    cv2.imshow("Image", img)
    cv2.waitKey(1) # 1 ms delay