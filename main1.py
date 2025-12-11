import speech_recognition as sr
import wikipedia
import webbrowser
import asyncio
import edge_tts
import playsound


# ---------- SPEAK FUNCTION USING MICROSOFT EDGE TTS ----------
async def speak_async(text):
    voice = "en-IN-NeerjaNeural"

    output_file = "voice.mp3"
    
    tts = edge_tts.Communicate(text, voice)

    try:
        await tts.save(output_file)
    except:
        # retry with fallback voice
        tts = edge_tts.Communicate(text, "en-IN-NeerjaNeural")
        await tts.save(output_file)

    playsound.playsound(output_file)


def speak(text):
    print("Assistant:", text)
    asyncio.run(speak_async(text))


# ---------- LISTEN FUNCTION ----------
def take_command():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration=0.3)

        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("No voice detected in time.")
            return ""

    try:
        query = r.recognize_google(audio)
        print("You said:", query)
        return query.lower()

    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return ""

    except sr.RequestError:
        print("Speech recognition service failed.")
        return ""


# ---------- MAIN LOOP ----------
speak("Voice assistant activated. How can I help you?")

while True:

    command = take_command()
    if command == "":
        continue

    # EXIT
    if "stop" in command or "exit" in command or "close assistant" in command:
        speak("Closing the assistant. Goodbye.")
        break

    # GOOGLE SEARCH
    if "search" in command and "on google" in command:
        topic = command.replace("search", "").replace("on google", "").strip()
        speak(f"Searching {topic} on Google.")
        webbrowser.open(f"https://www.google.com/search?q={topic}")
        continue

    # YOUTUBE PLAY/SEARCH
    if "on youtube" in command or "play" in command:
        topic = command.replace("play", "").replace("on youtube", "").strip()
        if topic == "":
            speak("Please say what you want me to play.")
            continue

        speak(f"Playing {topic} on YouTube.")
        webbrowser.open(f"https://www.youtube.com/results?search_query={topic}")
        continue

    # WIKIPEDIA SUMMARY
    if "who is" in command or "what is" in command:
        try:
            speak(f"Searching for {command}")
            result = wikipedia.summary(command, sentences=2)
            print(result)
            speak(result)
        except:
            speak("I couldn't find that on Wikipedia.")
        continue

    # DEFAULT REPLY
    speak("Okay, noted. What else can I do?")
