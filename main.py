import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is down.")
        return ""

def respond(command):
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you today?")
    elif "time" in command:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "search for" in command:
        query = command.split("search for")[-1].strip()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm not sure how to help with that.")

# Main loop
speak("speak assistant activated.")
# Modify your main loop to look like this

speak("Voice assistant activated.")
while True:
    command = listen()

    # --- ADD THIS FOR DEBUGGING ---
    print(f"DEBUG: The command received from listen() is: '{command}'")

    if command:
        print("DEBUG: Command is valid. Calling respond().")
        respond(command)
    else:
        # This will now show you when it fails
        print("DEBUG: Command is empty. Skipping respond() and listening again.")