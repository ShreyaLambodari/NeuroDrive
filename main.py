# src/main.py
import time, os
from collections import deque
from camera.camera import Camera
from detection.face_landmarks import FaceDetector
from features.blink_detector import BlinkDetector
from features.yawn_detector import mouth_aspect_ratio
from features.gaze_estimator import gaze_ratio
from recorders.circular_recorder import CircularRecorder
from utils.smoothing import EWMA
from inference.model_inference import DrowsinessModel
from alerts.alert_manager import AlertManager
from logger.telemetry import log_event

import cv2
import yaml

# load config
with open("config/config.yaml", "r") as f:
    cfg = yaml.safe_load(f)

cam = Camera(width=cfg['frame_width'], height=cfg['frame_height'], fps=cfg['fps'])
det = FaceDetector()
blink = BlinkDetector(ear_thresh=cfg['ear_threshold'], consecutive=cfg['ear_consec_frames'])
rec = CircularRecorder(max_frames=cfg['prebuffer_s']*cfg['fps'])
smoother = EWMA(alpha=0.2)
model = DrowsinessModel(tflite_path=None)  # add if you have a tflite model
alerts = AlertManager()
perclos_deque = deque(maxlen=cfg['perclos_window_s']*cfg['fps'])

last_event = 0

try:
    for frame in cam.frames():
        rec.add(frame)
        lms = det.get_landmarks(frame)
        if not lms:
            cv2.imshow("frame", frame); 
            if cv2.waitKey(1)&0xFF==ord('q'): break
            continue

        b = blink.update(lms)
        mar = mouth_aspect_ratio(lms)
        gaze = (gaze_ratio(lms, [33,160,158,133,153,144]) + gaze_ratio(lms,[362,385,387,263,373,380]))/2.0

        is_closed = 1 if b['ear'] < cfg['ear_threshold'] else 0
        perclos_deque.append(is_closed)
        perclos = sum(perclos_deque)/max(1, len(perclos_deque))

        features = {"ear": b['ear'], "mar": mar, "gaze": gaze, "perclos": perclos}
        score = model.predict(features)
        smooth = smoother.update(score)

        # draw
        cv2.putText(frame, f"SCORE:{smooth:.2f} PERC:{perclos:.2f}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0),2)

        now = time.time()
        if smooth > 0.6 and (now - last_event) > cfg['event_cooldown_s']:
            last_event = now
            print("EVENT: Drowsy!")
            alerts.trigger()
            # save clip
            fname = os.path.join("events", f"event_{int(now)}.avi")
            rec.save(fname, fps=cfg['fps'])
            log_event("events", "drowsy", features)
        cv2.imshow("Driver", frame)
        if cv2.waitKey(1)&0xFF == ord('q'):
            break
finally:
    cam.release()
    cv2.destroyAllWindows()