# Python3.12

import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

# List of 21 hand landmarks and their indices
HAND_LANDMARKS = [
    "0: Wrist",
    "1: Thumb CMC (Carpometacarpal joint)",
    "2: Thumb MCP (Metacarpophalangeal joint)",
    "3: Thumb IP (Interphalangeal joint)",
    "4: Thumb Tip",
    "5: Index Finger MCP (Metacarpophalangeal joint)",
    "6: Index Finger PIP (Proximal Interphalangeal joint)",
    "7: Index Finger DIP (Distal Interphalangeal joint)",
    "8: Index Finger Tip",
    "9: Middle Finger MCP (Metacarpophalangeal joint)",
    "10: Middle Finger PIP (Proximal Interphalangeal joint)",
    "11: Middle Finger DIP (Distal Interphalangeal joint)",
    "12: Middle Finger Tip",
    "13: Ring Finger MCP (Metacarpophalangeal joint)",
    "14: Ring Finger PIP (Proximal Interphalangeal joint)",
    "15: Ring Finger DIP (Distal Interphalangeal joint)",
    "16: Ring Finger Tip",
    "17: Pinky MCP (Metacarpophalangeal joint)",
    "18: Pinky PIP (Proximal Interphalangeal joint)",
    "19: Pinky DIP (Distal Interphalangeal joint)",
    "20: Pinky Tip"
]

print("List of Hand Landmarks:")
for landmark in HAND_LANDMARKS:
    print(landmark)

# Ask user for the landmark to detect
try:
    selected_landmark = int(input("Enter the number corresponding to the landmark you want to detect (0-20): "))
    if not (0 <= selected_landmark <= 20):
        raise ValueError("Invalid landmark index. Please enter a number between 0 and 20.")
    print(f"You selected: {HAND_LANDMARKS[selected_landmark]}")
except ValueError as e:
    print(e)
    exit()

# Initialize variables
pTime = 0
cTime = 0
cap = cv2.VideoCapture(1)

detector = htm.HandDetector()

while True:
    success, img = cap.read()
    if not success:
        print("Error: Could not read frame from webcam.")
        break

    # Detect hands and optionally draw landmarks
    img = detector.findHands(img, draw=True)

    # Get positions of all landmarks or the selected landmark
    lmList = detector.findPosition(img, draw=False, landmarkIndex=selected_landmark)

    if lmList:
        print(f"{HAND_LANDMARKS[selected_landmark]} Position: {lmList}")
        # Highlight the selected landmark on the image
        cv2.circle(img, (lmList['x'], lmList['y']), 15, (0, 255, 0), cv2.FILLED)

    # Calculate and display the frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:  # Exit on pressing 'Esc'
        break

cap.release()
cv2.destroyAllWindows()