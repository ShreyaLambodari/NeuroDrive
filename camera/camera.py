# src/camera/camera.py
import cv2

class Camera:
    def __init__(self, device=0, width=640, height=480, fps=20):
        self.cap = cv2.VideoCapture(device, cv2.CAP_DSHOW)  # use DirectShow on Windows
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FPS, fps)
        self.width = width; self.height = height; self.fps = fps

    def frames(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            yield frame

    def read(self):
        return self.cap.read()

    def release(self):
        if self.cap:
            self.cap.release()