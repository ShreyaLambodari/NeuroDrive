# src/alerts/alert_manager.py
import pygame
import time
import sys

class AlertManager:
    def __init__(self, beep_file=None, serial_port=None):
        try:
            pygame.mixer.init()
            self.sound = pygame.mixer.Sound(beep_file) if beep_file else None
        except Exception as e:
            print("Audio init failed:", e)
            self.sound = None
        # serial for vibration motor can be added later
        self.serial = None

    def play_beep(self):
        if self.sound:
            self.sound.play()
        else:
            try:
                import winsound
                winsound.Beep(1200, 500)
            except:
                print("[ALERT] beep fallback")

    def vibrate(self):
        # placeholder - integrate with ESP32 via serial later
        print("[ALERT] vibrate (stub)")

    def trigger(self, level="medium"):
        self.play_beep()
        self.vibrate()