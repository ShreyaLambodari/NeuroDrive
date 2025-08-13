# src/features/yawn_detector.py
import numpy as np

UPPER_LIP = 13
LOWER_LIP = 14
MOUTH_LEFT = 61
MOUTH_RIGHT = 291

def _euclid(a,b):
    return np.linalg.norm(np.array(a)-np.array(b))

def mouth_aspect_ratio(landmarks):
    top = landmarks[UPPER_LIP]
    bottom = landmarks[LOWER_LIP]
    left = landmarks[MOUTH_LEFT]
    right = landmarks[MOUTH_RIGHT]
    vertical = _euclid(top, bottom)
    horizontal = _euclid(left, right)
    if horizontal == 0:
        return 0.0
    return vertical / horizontal