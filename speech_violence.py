import speech_recognition as sr # Audio Reader 
import winsound  # For Windows beep sound
from transformers import pipeline # Import hugging face transformers

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", framework="pt") #Load NLP for violent speech detection

recognizer = sr.Recognizer() # Initialize recognizer

def beep():
        winsound.Beep(1000, 300)  # Frequency: 1000 Hz, Duration: 300ms

def transcribe_audio():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)  # Reduced delay
        try:
            audio_data = recognizer.listen(source, phrase_time_limit=3, timeout=2)  # Limit to 3 seconds, timeout if no speech
        except sr.WaitTimeoutError:
            return None  # No speech detected, silently continue

        try:
            return recognizer.recognize_google(audio_data).lower()  # Convert speech to text
        except (sr.UnknownValueError, sr.RequestError):
            return None 

def detect_violent_speech():
    text = transcribe_audio() #Hear audio
    if text:
        print(f"{text}")  # Output only the spoken text

        labels = ["violent speech", "normal speech"]
        result = classifier(text, candidate_labels=labels)  # Classify text

        if result["labels"][0] == "violent speech" and result["scores"][0] > 0.7: #If hears violent phrases with 70% confidence
            print("Violent Language Detected!")
            beep() 

# Run continuously
if __name__ == "__main__":
    print("\nMedSafe (Press Ctrl+C to stop)")
    try:
        while True:
            detect_violent_speech()
    except KeyboardInterrupt:
        print("\nStopped listening.")
