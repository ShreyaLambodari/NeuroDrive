# src/features/blink_detector.py
import numpy as np

LEFT_EYE = [33,160,158,133,153,144]
RIGHT_EYE = [362,385,387,263,373,380]

def _euclid(a,b):
    return np.linalg.norm(np.array(a)-np.array(b))

def eye_aspect_ratio(landmarks, idxs):
    p = [landmarks[i] for i in idxs]
    A = _euclid(p[1], p[5])
    B = _euclid(p[2], p[4])
    C = _euclid(p[0], p[3])
    if C == 0:
        return 0.0
    return (A + B) / (2.0 * C)

class BlinkDetector:
    def __init__(self, ear_thresh=0.23, consecutive=3):
        self.ear_thresh = ear_thresh
        self.consecutive = consecutive
        self.counter = 0
        self.total_blinks = 0

    def update(self, landmarks):
        le = eye_aspect_ratio(landmarks, LEFT_EYE)
        re = eye_aspect_ratio(landmarks, RIGHT_EYE)
        ear = (le + re) / 2.0
        closed = False
        if ear < self.ear_thresh:
            self.counter += 1
            closed = True
        else:
            if self.counter >= self.consecutive:
                self.total_blinks += 1
            self.counter = 0
            closed = False
        return {"ear": ear, "closed": closed, "blinks": self.total_blinks}