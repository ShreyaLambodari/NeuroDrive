# src/features/gaze_estimator.py
def gaze_ratio(landmarks, eye_idxs):
    xs = [landmarks[i][0] for i in eye_idxs]
    left_x = min(xs); right_x = max(xs)
    mean_x = sum(xs)/len(xs)
    if right_x - left_x == 0:
        return 0.5
    return (mean_x - left_x) / (right_x - left_x)  # 0..1, 0.5 center