#SingleInstance Force
SetTitleMatchMode, 2

IfWinNotExist, Chrome
{
    ExitApp, 1
}

WinActivate, Chrome
WinWaitActive, Chrome, , 3
Sleep, 300

Send, ^+a
Sleep, 400
Send, youtube
Sleep, 400
Send, {Enter}
Sleep, 600

IfWinActive, YouTube
    ExitApp, 0
Else
    ExitApp, 1
