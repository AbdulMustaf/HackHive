import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import time
import threading
import winsound

# Load the trained model
print("Loading model")
model = load_model('violence_detection_model.h5')
print("Model loaded successfully!")

# Open webcam
print("Opening webcam")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam. Trying again")
    cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Critical Error: No webcam found. Exiting.")
    exit()

print("Webcam opened successfully!")

# Define violence detection threshold
SEVERE_VIOLENCE_THRESHOLD = 0.80  # Severe violence threshold

# Function to play alarm sound (only once per detection)
def play_alarm():
    print("Playing alarm sound")
    winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500ms

# Initialize detection variables
severe_violence_detected = False

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: No frame captured. Exiting loop.")
        break

    resized_frame = cv2.resize(frame, (224, 224))
    normalized_frame = resized_frame / 255.0
    input_frame = np.expand_dims(normalized_frame, axis=0)

    prediction = model.predict(input_frame)
    print(f"Prediction score: {prediction[0][0]}")  # Debugging print

    # Severe Violence Detection Logic
    if prediction[0][0] > SEVERE_VIOLENCE_THRESHOLD:
        color = (0, 0, 255)  # Red alert color
        text = "VIOLENCE DETECTED!"
        
        # Play alarm sound only once per detection
        if not severe_violence_detected:
            severe_violence_detected = True
            threading.Thread(target=play_alarm, daemon=True).start()
    
    else:
        color = (0, 255, 0)  # Green (Safe)
        text = "No Violence Detected"
        
        # Reset detection flag
        severe_violence_detected = False

    # Draw text and bounding box
    cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), color, 10)
    cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow('Violence Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting")
        break

cap.release()
cv2.destroyAllWindows()
print("Webcam released. Script ended.")
