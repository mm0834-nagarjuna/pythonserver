from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from flask_cors import CORS
from text_to_speech import speak_text

app = Flask(__name__)
CORS(app)
load_dotenv()

app.config['DEBUG'] = os.environ.get('FLASK_DEBUG') == 'True'

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/post', methods=['POST'])
def post_example():
    data = request.get_json()
    return jsonify({"received_message": data})

@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    speak_text(text)
    return jsonify({"received_message": text})

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
