import cv2
import mediapipe as mp # https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker
import time


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

class HandDetector:
    def __init__(self, mode=False, maxHands=2, minDetectionConfidence=0.5, minTrackingConfidence=0.5):
        """
        Initializes the hand detection module.
        
        Parameters:
        mode (bool): If True, runs in static image mode.
        maxHands (int): Maximum number of hands to detect.
        minDetectionConfidence (float): Minimum confidence value ([0.0, 1.0]) for hand detection to be considered successful.
        minTrackingConfidence (float): Minimum confidence value ([0.0, 1.0]) for the landmark tracking to be considered successful.
        """
        self.mode = mode
        self.maxHands = maxHands
        self.minDetectionConfidence = minDetectionConfidence
        self.minTrackingConfidence = minTrackingConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.minDetectionConfidence,
            min_tracking_confidence=self.minTrackingConfidence
        )

        self.mpDraw = mp.solutions.drawing_utils
        self.results = None

    def findHands(self, img, draw=True):
        """
        Detects hands in the input image and optionally draws the landmarks.

        Parameters:
        img (numpy.ndarray): The input image in BGR format.
        draw (bool): If True, draws the hand landmarks on the image.

        Returns:
        numpy.ndarray: The image with hand landmarks drawn (if draw=True).
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert the image to RGB
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True, landmarkIndex=None):
        """
        Finds the positions of landmarks on a specific hand.

        Parameters:
        img (numpy.ndarray): The input image in BGR format.
        handNo (int): Index of the hand to analyze.
        draw (bool): If True, draws circles on the landmarks.
        landmarkIndex (int): If specified, only returns the position of this landmark.

        Returns:
        list or dict: A list of all landmark positions as [id, x, y], or a dict with the specified landmark position.
        """
        lmList = []
        if self.results and self.results.multi_hand_landmarks:
            if handNo < len(self.results.multi_hand_landmarks):
                myHand = self.results.multi_hand_landmarks[handNo]
                for id, lm in enumerate(myHand.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 15, (255, 25, 255), cv2.FILLED)

                if landmarkIndex is not None:
                    if 0 <= landmarkIndex < len(lmList):
                        return {"id": landmarkIndex, "x": lmList[landmarkIndex][1], "y": lmList[landmarkIndex][2]}
                    else:
                        print(f"Invalid landmark index: {landmarkIndex}")
                        return None
        return lmList

def main():
    """
    Main function to capture video feed and use the HandDetector class for hand landmark detection.
    """
    pTime = 0  # Previous time for FPS calculation
    cTime = 0  # Current time for FPS calculation

    cap = cv2.VideoCapture(0)  # Use webcam (camera index 0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    detector = HandDetector()

    try:
        while True:
            success, img = cap.read()
            if not success:
                print("Error: Could not read frame from webcam.")
                break

            img = detector.findHands(img)
            lmList = detector.findPosition(img, landmarkIndex=4)  # Example: Get position of Thumb Tip
            if lmList:
                print(f"Landmark Position: {lmList}")

            # Calculate and display the frame rate
            cTime = time.time()
            fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
            pTime = cTime

            cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

            cv2.imshow("Hand Tracking", img)

            if cv2.waitKey(1) & 0xFF == 27:  # Exit on pressing 'Esc'
                break

    finally:
        cap.release()  # Release webcam resource
        cv2.destroyAllWindows()  # Close all OpenCV windows

if __name__ == "__main__":
    main()