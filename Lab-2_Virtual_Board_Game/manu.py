import os
from collections import Counter
import cv2
import statistics

DATASET_PATH = "/Users/manubaba/Documents/CREMA-D"

EMOTION_CODES = {
    "ANG": "Anger",
    "DIS": "Disgust",
    "FEA": "Fear",
    "HAP": "Happy",
    "SAD": "Sad",
    "NEU": "Neutral"
}

emotion_counter = Counter()
fps_values = []
total_videos = 0
failed_videos = []

for root, _, files in os.walk(DATASET_PATH):
    for file in files:
        if file.lower().endswith(".flv"):
            file_path = os.path.join(root, file)
            parts = file.split("_")

            # Emotion parsing
            if len(parts) >= 3 and parts[2] in EMOTION_CODES:
                emotion_counter[EMOTION_CODES[parts[2]]] += 1

            # FPS extraction
            cap = cv2.VideoCapture(file_path)
            fps = cap.get(cv2.CAP_PROP_FPS)

            if not cap.isOpened() or fps <= 0:
                failed_videos.append(file)
            else:
                fps_values.append(fps)

            cap.release()
            total_videos += 1

# ---- Results ----
print("\nEmotion Distribution:")
for emotion, count in emotion_counter.items():
    print(f"{emotion}: {count}")

print(f"\nTotal videos counted: {total_videos}")

if fps_values:
    print("\nFPS Statistics:")
    print(f"Average FPS: {statistics.mean(fps_values):.2f}")
    print(f"Min FPS: {min(fps_values):.2f}")
    print(f"Max FPS: {max(fps_values):.2f}")
    print(f"Unique FPS values: {sorted(set(round(fps, 2) for fps in fps_values))}")

if failed_videos:
    print(f"\nWarning: {len(failed_videos)} videos could not be read properly.")
