# Hand Tracking (CPU only)

This repository contains Python scripts for hand tracking and landmark detection using the Mediapipe library. The project demonstrates how to use Mediapipe's pre-trained models to detect hands in real-time video and extract specific landmarks for various applications such as gesture recognition and hand movement analysis.

## Project Structure

- **HandTrackingModule.py**: Contains the core `HandDetector` class, encapsulating the functionality for detecting hands and extracting hand landmarks.
- **example_use.py**: A demonstration script showing how to use the `HandTrackingModule` for real-time hand tracking with specific landmark detection.
- **hand_tracking.py**: Another script showcasing the hand tracking functionality and the visualization of hand landmarks.
- **requirements.txt**: Lists the dependencies required to run this project.

## Features

- Real-time hand detection and tracking using a webcam.
- Extracts 21 key landmarks for each detected hand.
- Customizable detection of specific landmarks (e.g., thumb tip, index finger tip).
- Easy-to-use modular code for integration into other projects.

## Requirements

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

Dependencies:
- `opencv-python`: For video capture and image processing.
- `mediapipe`: For hand detection and landmark estimation.

## Usage

### Example Use
To run the demonstration script:
```bash
python example_use.py
```

### Custom Landmark Detection
The `HandDetector` class allows users to detect specific landmarks. For example, you can detect the position of the thumb tip or any other landmark by specifying its index (0-20).

### Hand Landmark Indices
Below are the indices for the 21 hand landmarks:

| Index | Description                          |
|-------|--------------------------------------|
| 0     | Wrist                                |
| 1     | Thumb CMC (Carpometacarpal joint)    |
| 2     | Thumb MCP (Metacarpophalangeal joint)|
| 3     | Thumb IP (Interphalangeal joint)     |
| 4     | Thumb Tip                            |
| 5     | Index Finger MCP                     |
| 6     | Index Finger PIP                     |
| 7     | Index Finger DIP                     |
| 8     | Index Finger Tip                     |
| 9     | Middle Finger MCP                    |
| 10    | Middle Finger PIP                    |
| 11    | Middle Finger DIP                    |
| 12    | Middle Finger Tip                    |
| 13    | Ring Finger MCP                      |
| 14    | Ring Finger PIP                      |
| 15    | Ring Finger DIP                      |
| 16    | Ring Finger Tip                      |
| 17    | Pinky MCP                            |
| 18    | Pinky PIP                            |
| 19    | Pinky DIP                            |
| 20    | Pinky Tip                            |

## Contributions

Contributions are welcome! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
