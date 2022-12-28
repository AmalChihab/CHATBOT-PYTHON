from flask import Flask,render_template,request,jsonify

from chat import get_response
from werkzeug.wrappers import response

from audio_recognition import get_audio, audio_to_text, play_sound
import speech_recognition as sr
import gtts
from playsound import playsound
import os

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

@app.post("/audio")
def predictAudio():
    audio = get_audio()
    text = audio_to_text(audio)
    response = get_response(text)
    print(text)
    print(response)
    play_sound(response.encode("windows-1252").decode("utf-8"))
    return jsonify({"question": text, "answer": response})
    

if __name__ == "__main__":
    app.run(port=5502, debug=True)
    print("Hello dev")