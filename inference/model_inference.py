# src/inference/model_inference.py
import math

class DrowsinessModel:
    def __init__(self, tflite_path=None):
        # Simplified constructor - no TensorFlow dependency
        pass

    def predict(self, features):
        # features = dict with ear, mar, gaze, blink_rate, perclos
        # simple heuristic score: bigger = more drowsy (0..1)
        ear = features.get("ear", 0.3)
        mar = features.get("mar", 0.0)
        perclos = features.get("perclos", 0.0)
        gaze_dev = abs(features.get("gaze", 0.5) - 0.5)  # 0 = center
        score = min(1.0, max(0.0, (0.6*(1-ear) + 0.2*mar + 0.4*perclos + 0.4*gaze_dev)/1.6))
        return score