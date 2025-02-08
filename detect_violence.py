import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model, load_model
from flask import Flask, render_template, Response

import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
print("⏳ Loading model...")
model = load_model('violence_detection_model.h5')
print("✅ Model loaded successfully!")

# Open webcam
print("🎥 Opening webcam...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Cannot access webcam. Trying index 1...")
    cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("❌ Critical Error: No webcam found. Exiting.")
    exit()

print("✅ Webcam opened successfully!")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("❌ Error: No frame captured. Exiting loop.")
        break

    print("📸 Frame captured!")  # Debugging print
    
    resized_frame = cv2.resize(frame, (224, 224))
    normalized_frame = resized_frame / 255.0
    input_frame = np.expand_dims(normalized_frame, axis=0)

    prediction = model.predict(input_frame)
    print(f"🧠 Prediction score: {prediction[0][0]}")  # Debugging print

    color = (0, 255, 0)
    text = "No Violence Detected"
    if prediction[0][0] > 0.5:
        color = (0, 0, 255)
        text = "Violence Detected!"

    cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), color, 10)
    cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow('Violence Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🔴 Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Webcam released. Script ended.")
