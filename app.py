from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
load_dotenv()

app.config['DEBUG'] = os.environ.get('FLASK_DEBUG') == 'True'


# import pyttsx3

# def speak_text(command):
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)
#     engine.say(command)
#     engine.runAndWait()



import speech_recognition as sr


def capture_and_process_command():
    r = sr.Recognizer()
    text = ''
    with sr.Microphone(0) as source2:
        print("please wait......")
        r.adjust_for_ambient_noise(source2, duration=0.2)
        print("Listening for your command. Please speak clearly.")

        try:
            audio = r.listen(source2, timeout=None, phrase_time_limit=20)  
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()

            text = MyText
        except sr.WaitTimeoutError:
            return("Listening timed out while waiting for phrase to start")
            return None
        except sr.UnknownValueError:
            return("Google Speech Recognition could not understand the audio")
            return None
        except sr.RequestError as e:
            return(f"Could not request results from Google Speech Recognition service; {e}")
            return None
    return text






@app.route('/')
def home():
    return "Hello, World!"

@app.route('/post', methods=['POST'])
def post_example():
    data = request.get_json()
    return jsonify({"received_message": data})

@app.route('/speect_to_text', methods=['POST'])
def text_to_speech():
    
    text = capture_and_process_command()
    if not text:
        return jsonify({"error": "No text provided"}), 400

    return jsonify({"received_message": text})

# if __name__ == '__main__':
#     app.run(debug=app.config['DEBUG'])
