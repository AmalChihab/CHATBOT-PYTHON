import speech_recognition as sr
import gtts
from playsound import playsound
import os

r = sr.Recognizer()

def get_audio():
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
    return audio

def audio_to_text(audio):
    text = ""
    try:
        text = r.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        text = "Speech recognition could not understand audio"
        print("Speech recognition could not understand audio")
    except sr.RequestError:
        text = "could not request results from API"
        print("could not request results from API")
    return text

def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        tempfile = "./temp.mp3"
        tts.save(tempfile)
        playsound(tempfile)
        os.remove(tempfile)
    except AssertionError:
        print("could not play sound")


# test
if __name__ == "__main__":
    play_sound("salut")
    print(sr.Microphone.list_microphone_names())
    print(sr.Microphone)
   
    