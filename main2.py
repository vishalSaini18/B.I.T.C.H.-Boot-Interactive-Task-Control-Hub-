import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for index, voice in enumerate(voices):
    print(index, voice.id)


def say(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    say("Hello, I am Bitch, tell me what I can do for you")
