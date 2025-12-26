# basic_controls.py

import time
import webbrowser
import pyautogui
from datetime import datetime
import os
import sys
import pygetwindow as gw

# =========================
# KEYWORDS
# =========================

TIME_KEYWORDS = [
    "time",
    "current time",
    "what time is it",
    "what's the time",
    "what is the time",
    "tell me the time"
]

OPEN_GOOGLE_KEYWORDS = [
    "open google",
]

OPEN_YOUTUBE_KEYWORDS = [
    "open youtube",
    "launch youtube",
    "start youtube"
]

IN_APP_SEARCH_PREFIX = ["search for"]
GOOGLE_SEARCH_PREFIX = ["search google for", "search on google for", "google search for", "google for" , "search google"]

SHUTDOWN_KEYWORDS = [
    "close all apps and shutdown",
    "close everything and shutdown",
    "shutdown pc completely",
    "force shutdown pc",
    "shutdown my pc",
    "shut down my pc",
    "shut down pc",
    "shutdown pc",
]

maximize_window_keywords = [
    "fullscreen", "full screen", "maximize video", "maximize", "big screen"
]

restore_window_keywords = [
    "exit full screen", "minimize video", "small screen","restore"
]

CLOSE_TAB_KEYWORDS = [
    "close tab", "close this", "close it", 
    "exit tab", "close youtube", "stop youtube", "close the song"
]

# =========================
# FUNCTIONS
# =========================

def tell_time(speak):
    now = datetime.now().strftime("%I:%M %p")
    print(f"Current time: {now}")
    speak(f"The current time is {now}")

def open_google(speak):
    speak("Opening Google")
    webbrowser.open("https://www.google.com")

def open_youtube(speak):
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def in_app_search(command, speak):
    prefix = next(
        (p for p in IN_APP_SEARCH_PREFIX if command.startswith(p)),
        None
    )

    if not prefix:
        return

    query = command.replace(prefix, "").strip()
    if not query:
        return

    speak(f"Searching for {query}")

    pyautogui.hotkey("ctrl", "f")
    time.sleep(0.2)

    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    time.sleep(0.1)

    pyautogui.typewrite(query, interval=0.02)


def google_search(command, speak):
    prefix = next(
        (p for p in GOOGLE_SEARCH_PREFIX if command.startswith(p)),
        None
    )

    if not prefix:
        return

    query = command.replace(prefix, "").strip()
    if not query:
        return

    speak(f"Searching Google for {query}")
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)

def shutdown_pc(speak):
    speak("Closing all applications and shutting down the computer")
    os.system("shutdown /s /f /t 3")
    sys.exit()

def maximize_window():
    time.sleep(0.2)
    win = gw.getActiveWindow()
    if win and not win.isMaximized:
        win.maximize()

def restore_window():
    time.sleep(0.2)
    win = gw.getActiveWindow()
    if win and win.isMaximized:
        win.restore()

def go_back():
    time.sleep(0.2)
    pyautogui.hotkey("alt", "left")

def next_tab():
    pyautogui.hotkey("ctrl", "tab")

def previous_tab():
    pyautogui.hotkey("ctrl", "shift", "tab")

def close_tab():
    pyautogui.hotkey("ctrl", "w")