from flask import Flask
import speech_recognition
import os

app = Flask(__name__)

recognizer = speech_recognition.Recognizer()
audio_file = os.path.join(os.path.dirname(__file__), '..', 'app', 'audio.wav')

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/getText', methods=['GET'])
def Text():
    with speech_recognition.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:

        recognized_text = recognizer.recognize_google(audio)
        return(f"Recognized text:{recognized_text}" )
    except speech_recognition.UnknownValueError:
        return("Sorry, I couldn't understand what you said.")
    except speech_recognition.RequestError as e:
        return("Error:", e)
