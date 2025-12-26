import pyautogui
import time
import pygetwindow as gw
import webbrowser
import pywhatkit
import subprocess
import os
from youtube_controls import activate_chrome

VOLUME_UP_KEYWORDS = [
    "volume up", "increase volume", "louder", 
    "sound up", "increase sound"
]

VOLUME_DOWN_KEYWORDS = [
    "volume down", "decrease volume", "lower volume", 
    "quiet", "reduce sound"
]

# -------------------------------
#  CHROME TAB CONTROLS
# -------------------------------


def volume_down():
    time.sleep(0.2)
    pyautogui.press("volumedown")

def volume_up():
    time.sleep(0.2)
    pyautogui.press("volumeup")

def activate_chrome_cmd():
    return activate_chrome()


