from flaskApp import app

@app.route('/')
def home():
    return "Hello, Flask!"
