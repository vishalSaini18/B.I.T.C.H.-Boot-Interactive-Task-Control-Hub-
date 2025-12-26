from speech_engine import speak
from listener import listen
from commands import respond
import time

speak("Bitch activated.")

WAKE_WORDS = [
    "bitch activate", "hey bitch", "bitch", "fucking bitch",
    "jarvis", "hey jarvis", "jorvis", "hey jorvis", "siri","hey siri", "kutte", "uth ja kutte"
]

ACTIVE_TIMEOUT = 600  # seconds

active = True                    # active initially
last_active_time = time.time()   # start timer

while True:
    command = listen()

    # 🔥 FIX: silently ignore empty polls
    if command is None:
        # auto-deactivate on timeout
        if active and time.time() - last_active_time > ACTIVE_TIMEOUT:
            active = False
            speak("Deactivated.")
        time.sleep(0.05)   # prevent fast looping
        continue

    command = command.lower()
    print(f"Command received: {command}")

    if command == "exit":
        speak("Goodbye.")
        break

    # Wake word detection (when inactive)
    if not active:
        if any(w in command for w in WAKE_WORDS):
            active = True
            last_active_time = time.time()
            speak("Bitch Activated.")
        continue

    # Reset timer on any valid command while active
    last_active_time = time.time()

    # Manual sleep
    if command in ["sleep", "deactivate", "stop listening", "chup", "chup kar kutte", "chup kar be kutte", "chup karbe kutte"]:
        active = False
        speak("Deactivated.")
        continue

    # Execute command
    respond(command)



