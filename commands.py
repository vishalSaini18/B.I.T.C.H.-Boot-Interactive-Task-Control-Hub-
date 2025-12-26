import webbrowser
import pywhatkit
import sys
from datetime import datetime
import re
from speech_engine import speak
from ai_fallback import ai_reply
import time
import os
import pyautogui


from basic_controls import (
    TIME_KEYWORDS, OPEN_GOOGLE_KEYWORDS, OPEN_YOUTUBE_KEYWORDS,
    IN_APP_SEARCH_PREFIX, GOOGLE_SEARCH_PREFIX, SHUTDOWN_KEYWORDS,
    restore_window_keywords,maximize_window_keywords,CLOSE_TAB_KEYWORDS,

    go_back, tell_time, open_google, open_youtube, in_app_search, google_search, shutdown_pc,
    maximize_window, restore_window, next_tab, previous_tab, close_tab
)

from youtube_controls import (
    PAUSE_KEYWORDS, PLAY_KEYWORDS, REWIND_KEYWORDS, FORWARD_KEYWORDS, NEXT_VIDEO_KEYWORDS,
    PREVIOUS_VIDEO_KEYWORDS, PLAY_SONG_PREFIX,
    
    play_song_command,
    pause_video, play_video, rewind_video, forward_video,
    next_video, previous_video,
    play_song_in_same_tab, activate_chrome
)

from chrome_controls import (
    VOLUME_UP_KEYWORDS, VOLUME_DOWN_KEYWORDS,

    volume_up, volume_down,
    activate_chrome_cmd,
)


from whatsapp_desktop_controls import (
    Opening_WHATSAPP_KEYWORDS,
    GO_BACK_TO_CHATS_KEYWORDS,
    UNREAD_MESSAGE_KEYWORDS,
    send_message_to_contact,
    Close_WHATSAPP_KEYWORDS,

    activate_whatsapp_desktop,
    search_contact,
    send_message,
    go_back_to_chats,
    type_message_whatsapp,
    clear_message_whatsapp,
    go_to_unread_messages,
    next_chat,
    close_whatsapp
)


def respond(command):

    # ============================
    #    BASIC COMMANDS
    # ============================

    # Time
    if command in TIME_KEYWORDS:
        tell_time(speak)

    # Open Google
    elif command in OPEN_GOOGLE_KEYWORDS:
        open_google(speak)

    # Open YouTube
    elif command in OPEN_YOUTUBE_KEYWORDS:
        open_youtube(speak)

    # uses Ctrl+F (works in WhatsApp Desktop, browsers, VS Code, etc.)
    elif any(command.startswith(p) for p in IN_APP_SEARCH_PREFIX):
        in_app_search(command, speak)

    # Google Search
    elif any(command.startswith(p) for p in GOOGLE_SEARCH_PREFIX):
        google_search(command, speak)
    
    # Go back
    elif command in ["go back", "previous page"]:
        speak("Going back")
        go_back()

    # Fullscreen
    elif command in maximize_window_keywords :
        speak("Going fullscreen")
        maximize_window()

    # Exit fullscreen
    elif command in restore_window_keywords :
        speak("Exiting fullscreen")
        restore_window()

    # Shutdown PC
    elif command in SHUTDOWN_KEYWORDS:
        shutdown_pc(speak)

    # ============================
    #    YOUTUBE CONTROLS
    # ============================

    # Play song (on YouTube)
    elif command.startswith(f"{PLAY_SONG_PREFIX} "):
        play_song_command(command, speak, play_song_in_same_tab)
    
    # Pause / Stop
    elif command in PAUSE_KEYWORDS:
        speak("Pausing the video")
        pause_video()

    # Resume / Play
    elif command in PLAY_KEYWORDS:
        speak("Playing the video")
        play_video()

    # Rewind 10 seconds
    elif command in REWIND_KEYWORDS :
        speak("Rewinding")
        rewind_video()

    # Forward 10 seconds
    elif command in FORWARD_KEYWORDS :
        speak("Skipping ahead")
        forward_video()

    # Next Video
    elif command in NEXT_VIDEO_KEYWORDS :
        speak("Playing next video")
        next_video()

    # Previous Video
    elif command in PREVIOUS_VIDEO_KEYWORDS :
        speak("Going back to previous video")
        previous_video()
    
    # Exit assistant
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        sys.exit()

        
    # ============================
    #    CHROME COMMANDS
    # ============================

    # Volume Up
    elif command in VOLUME_UP_KEYWORDS :
        speak("Turning volume up")
        volume_up()

    # Volume Down
    elif command in VOLUME_DOWN_KEYWORDS :
        speak("Turning volume down")
        volume_down()

    # Close current tab
    elif command in CLOSE_TAB_KEYWORDS:
        speak("Closing the tab")
        close_tab()
    
    # Move to next Chrome tab
    elif any(phrase in command for phrase in [
        "next tab",
        "move to next tab",
        "switch to next tab",
        "go to next tab"
    ]):
        if next_tab():
            speak("Next tab")
        else:
            speak("Chrome is not active")

    # Move to previous Chrome tab
    elif any(phrase in command for phrase in [
        "previous tab",
        "move to previous tab",
        "switch to previous tab",
        "go to previous tab",
        "last tab"
    ]):
        if previous_tab():
            speak("Previous tab")
        else:
            speak("Chrome is not active")

    # Activate Chrome
    elif any(phrase in command for phrase in [
        "activate chrome",
        "open chrome",
        "bring chrome",
        "switch to chrome",
        "focus chrome"
    ]):
        if activate_chrome():
            speak("Chrome activated")
        else:
            speak("Chrome is not running")

    # ============================
    #    WHATSAPP DESKTOP COMMANDS
    # ============================

    elif any(word in command for word in Opening_WHATSAPP_KEYWORDS):
        speak("Opening WhatsApp")
        activate_whatsapp_desktop()

    elif command.startswith("search whatsapp"):
        # example: search whatsapp rahul
        name = command.replace("search whatsapp", "").strip()
        speak(f"Searching {name} on WhatsApp")
        search_contact(name)

    # search for already in basic commands
    elif command == "go down" or command == "scroll down" or command == "godown" or command == "neeche ja" or command == "neecheja":
        pyautogui.press("down")

    elif command == "go up" or command == "uparja" or command == "upar ja" or command == "up":
        pyautogui.press("up")

    elif command == "select contact" or command == "open chat" or command == "go to chat" or command == "open":
        pyautogui.press("enter")

    elif command.startswith("send message to"):
        name = command.replace("send message to", "").strip()
        speak(f"Sending message to {name}")
        send_message_to_contact(name)

    elif command.startswith("type message"):
        message = command.replace("type message", "").strip()

        if message:
            speak("Typing")
            type_message_whatsapp(message)

    elif command in ["clear message", "delete message", "remove message"]:
        speak("Clearing message")
        clear_message_whatsapp()

    elif command in GO_BACK_TO_CHATS_KEYWORDS:
        go_back_to_chats()

    elif command == "next chat" or command == "next message":
        next_chat()

    elif command in UNREAD_MESSAGE_KEYWORDS:
        go_to_unread_messages()

    elif command == "send message":
        pyautogui.press("enter")

    elif command in Close_WHATSAPP_KEYWORDS:
        speak("Closing WhatsApp")
        if close_whatsapp():
            speak("WhatsApp closed")
        else:
            speak("WhatsApp is not running")


    # ============================
    #    AI FALLBACK
    # ============================

    else:
        reply = ai_reply(command)

        if reply:
            print("AI:", reply)
            speak(reply)
        else:
            print("AI: No response")
            speak("I don't have an answer for that.")


