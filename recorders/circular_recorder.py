# src/recorder/circular_recorder.py
from collections import deque
import cv2
import os

class CircularRecorder:
    def __init__(self, max_frames=20*8):  # default 8s at 20fps
        self.buf = deque(maxlen=max_frames)

    def add(self, frame):
        self.buf.append(frame.copy())

    def save(self, path, fps=20):
        if len(self.buf) == 0:
            return
        h,w = self.buf[0].shape[:2]
        os.makedirs(os.path.dirname(path), exist_ok=True)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(path, fourcc, fps, (w,h))
        for f in self.buf:
            out.write(f)
        out.release()