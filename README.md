## 🧠 NeuroDrive - "Your Co-Pilot for Safety"
*Driver Fatigue Detection & Safety Alert System*

Real-time drowsiness detection and alerting using OpenCV & Pygame.

## 🚀 Overview

NeuroDrive is an AI-assisted driver monitoring system that uses computer vision to track eye blinks, yawns, and gaze direction to detect signs of fatigue.
When drowsiness is detected, the system triggers alerts to keep the driver awake and focused.

## ✨ Features
*Blink detection* — track eye closure frequency.

*Yawn detection* — detect mouth openings associated with fatigue.

*Gaze estimation* — monitor if the driver’s attention drifts away from the road.

*Real-time alerts* — sound notifications and visual warnings using Pygame.

*Customizable thresholds* — tweak sensitivity via the config file.

## 🛠 Tech Stack
**Languages: Python**

**Libraries Used:**

**opencv-python — image capture & processing**

**pygame — sound alerts**

**numpy — numerical processing**

**math — geometric calculations**

**json — reading/writing structured config**

**os, time — system utilities & timing**

**collections.deque — frame buffering for smooth detection**

## 📂 Project Structure

NeuroDrive/
│
├── alerts/                # Alert management logic
│   └── alert_manager.py
│
├── camera/                 # Camera handling & video capture
│   └── camera.py
│
├── config/
│   └── config.yaml         # Configurable parameters
│
├── detection/              # Face and landmark detection
│   └── face_landmarks.py
│
├── features/               # Blink, yawn, gaze modules
│   ├── blink_detector.py
│   ├── gaze_estimator.py
│   └── yawn_detector.py
│
├── inference/              # (Optional) model inference logic
│   └── model_inference.py
│
├── logger/                 # Logging/telemetry
│   └── telemetry.py
│
├── recorders/              # Video/audio recording
│   └── circular_recorder.py
│
├── utils/                  # Helper functions
│   └── smoothing.py
│
├── main.py                  # Main application entry point
└── .gitignore


## ⚙️ Installation & Usage
Clone the repository


git clone https://github.com/your-username/NeuroDrive.git
cd NeuroDrive
Install dependencies


pip install opencv-python pygame numpy
Run the main application


python main.py
📊 How It Works
mermaid
Copy
Edit
flowchart LR
    Camera --> FaceDetection
    FaceDetection --> Blink
    FaceDetection --> Yawn
    FaceDetection --> Gaze
    Blink --> AlertSystem
    Yawn --> AlertSystem
    Gaze --> AlertSystem
    AlertSystem --> Pygame[Sound Alert]

    
## 🌟 Future Plans
**GUI for adjusting detection thresholds.**

**Logging fatigue events with timestamps.**

**Support for multiple camera angles.**

**Integration with external hardware (buzzers, vibration motors).**

