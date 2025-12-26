import pyttsx3
import threading
import queue

def speak(text, speed=160):
    engine = pyttsx3.init()

    for v in engine.getProperty("voices"):
        if "zira" in v.id.lower() or "female" in v.id.lower():
            engine.setProperty("voice", v.id)
            break

    engine.setProperty("rate", speed)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
