# src/logger/telemetry.py
import json, os, time

def log_event(outdir, event_type, details):
    os.makedirs(outdir, exist_ok=True)
    fname = os.path.join(outdir, f"event_{int(time.time())}.json")
    payload = {"time": time.time(), "type": event_type, "details": details}
    with open(fname, "w") as f:
        json.dump(payload, f, indent=2)