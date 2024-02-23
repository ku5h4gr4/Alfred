import os
import pyautogui as pyg
import webbrowser
from time import sleep
from voice import say


apps = {"wordpad":"wordpad","chrome":"chrome","brave":"brave","notepad":"notepad"}

def openApp(query):
    say("Launching;Sir")
    if ".com" in query or ".in" in query or ".org" in query or ".co.in" in query:
        query = query.replace("open","")
        query = query.replace("alfred","")
        query = query.replace("search","")
        query = query.replace(" ","")
        webbrowser.open(f"https://{query}")
    else:
        keys = list(apps.keys())
        for app in keys:
            if app in query:
                os.system(f"start {apps[app]}")


def closeApp(query):
    say("Closing;Sir")
    if "close one tab" in query or "1 tab" in query or "close this tab" in query:
        pyg.hotkey("ctrl","w")
        sleep(0.3)
    elif "close two tab" in query or "close 2 tab" in query:
        pyg.hotkey("ctrl","w")
        sleep(0.4)
        pyg.hotkey("ctrl","w")
        sleep(0.4)
    else:
        keys = list(apps.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {apps[app]}.exe")
