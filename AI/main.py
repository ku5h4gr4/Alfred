import datetime
import os
import pyttsx3
import speech_recognition as sr
import pyautogui as pyg
from time import sleep
from pygame import mixer

mixer.init()


# AUTHENTICATION TO LOAD ASSISTANT

for i in range(2):
    usr = input("Enter password to open Desktop Assistant: ")
    with open("pass.txt","r") as pswd_file:
        pw = pswd_file.read()
    if usr == pw:
        print("OPENING....")
        break
    elif i == 1 and usr != pw:
        exit()
    elif usr != pw:
        print("Try again")
sleep(0.3)

# START ANIMATION

from introAssistant import scrBg
scrBg

print("WELCOME, PLZ SPEAK [WAKE UP ALFRED] TO LOAD ASSISTANT")


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 180)


# MACHINE VOICE
def say(audio):
    engine.say(audio)
    engine.runAndWait()


# MICROPHONE
def listen():
    cmd = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening..")
        cmd.pause_threshold = 0.8  # WAIT AFTER LISTENING
        cmd.energy_threshold = 70  # AMPLITUDE OF USER VOICE
        audio = cmd.listen(source, 0, 4)
    try:
        print("Recognizing...")
        query = cmd.recognize_google(audio, language="en-in")
        print(f"User: {query}\n")
    except Exception as e:
        print("Couldn't fetch Voice\n")
        return "None"
    return query


def alarm(query):
    with open("Alarm.txt", "a") as alarmtime:
        alarmtime.write(query)
        os.startfile("alarmfile.py")


if __name__ == "__main__":

    while True:
        mixer.music.load("Z:/Stuffs/Project/AI/Sounds/ai_listen.mp3")
        mixer.music.play()
        query = listen().lower()
        if "wake up alfred" in query or "wake up at" in query or "wake up and" in query or "wake up alphabet" in query:
            from greeting import greet
            greet()

            while True:
                mixer.music.load("Z:/Stuffs/Project/AI/Sounds/ai_listen.mp3")
                mixer.music.play()

                # ALL COMMANDS
                query = listen().lower()
                if "alfred log of" in query:
                    say("Logging Off")
                    print("Speak [WAKE UP ALFRED] to wake me up")
                    break

                elif "power down alfred" in query:
                    say("Shutting Down")
                    exit()

                elif "how are you" in query or "how r u" in query:
                    say("I am Perfect;Sir")
                elif "thank you" in query:
                    say("It's a pleasure for me;Sir")

                elif "pause video" in query or "play video" in query:
                    pyg.press("k")
                    say("Done;Sir")

                elif "full screen mode" in query:
                    pyg.press("f")
                    say("Done,Sir")

                elif "silent" in query or "silent off" in query:
                    pyg.press("m")
                    say("Done;Sir")

                elif "show caption" in query:
                    pyg.press("c")

                elif "switch tab" in query:
                    from keyboard import tabSwitch
                    tabSwitch()
                    say("Tab Switched")

                elif "show all window" in query:
                    from keyboard import deskWindow
                    deskWindow()

                elif "show my working window" in query or "hide window" in query:
                    from keyboard import deskScreen
                    deskScreen()

                elif "increase volume" in query:
                    from keyboard import volUp
                    say("volume increased")
                    volUp()

                elif "volume down" in query:
                    from keyboard import volDown
                    volDown()
                    say("volume decreased")

                elif "full volume" in query:
                    from keyboard import fullVolume
                    fullVolume()
                    say("Maximum Volume")

                elif "alfred open" in query:
                    query = query.replace("alfred","")
                    query = query.replace("open","")
                    query = query.replace("  ","")
                    say("Launching Sir")
                    pyg.press("super")
                    sleep(0.5)
                    pyg.typewrite(query)
                    pyg.press("enter")

                elif query == "close window" or query == "exit":
                    from keyboard import closeWindow
                    closeWindow()
                    say("Done,Sir")

                elif "open" in query:
                    from dictApp import openApp
                    openApp(query)

                elif "close" in query:
                    from dictApp import closeApp
                    closeApp(query)

                elif "google" in query:
                    from searchWeb import googleSearch
                    googleSearch(query)

                elif "wikipedia" in query:
                    from searchWeb import wikipediaSearch
                    wikipediaSearch(query)

                elif "youtube" in query:
                    from searchWeb import youtubeSearch
                    youtubeSearch(query)

                elif "temperature" in query:
                    from weather import climate
                    climate(query)

                elif "the time" in query:
                    currentTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(currentTime)
                    say(currentTime)

                elif "set an alarm" in query:
                    print("Input time example:- 10:10:10")
                    say("Set the alarm")
                    alrm = input()
                    alarm(alrm)
                    say("Done;Sir")

                elif "store this alfred" in query:
                    query = query.replace("store this alfred","")
                    message = query.replace("alfred","")
                    message = query.replace(" ","")
                    print(message)
                    with open("AlfredMemory.txt","w") as rememberText:
                        rememberText.write(message)
                        say("Saved it in my database")

                elif "tell me alfred what do you remember" in query:
                    say("Sure,Sir;here's what i found in my database")
                    with open("AlfredMemory.txt","r") as rememberText:
                        say(rememberText.read())

                elif "alfred i am tired play something" in query:
                    from songPlaylist import playlist
                    playlist()

                elif "read some news" in query:
                    from newsToday import latestNews
                    try:
                        latestNews()
                    except Exception as e:
                        pass

                elif "calculate" in query:
                    from calculate import calc
                    query = query.replace("calculate","")
                    query = query.replace("alfred","")
                    calc(query)

                elif "change password" in query:
                    say("Type new password: ")
                    new_pw = input("Enter here: ")
                    with open("pass.txt","w") as new_pass:
                        new_pass.write(new_pw)
                    say("Password changed successfully")

                elif "shut down my system" in query:
                    say("Are you sure? ")
                    shutdown = input("Enter-[y][n]: ")
                    if shutdown == "y" or shutdown == "Y":
                        say("System will shutdown in 10 seconds")
                        print("System will shutdown in 10 seconds")
                        os.system("shutdown /s /t 10")
                    elif shutdown == "n" or shutdown == "N":
                        say("Okay")
                        break

                elif "schedule my task" in query:
                    tasks = []
                    say("Do you want to clear previous tasks (Say clear or NO")
                    query = listen().lower()
                    if "clear" in query:
                        with open("tasks.txt","w") as task_file:
                            task_file.write(f"")
                    elif "no" in query:
                        pass
                    else:
                        say("No command received, proceeding for default")
                    say("Enter the number of tasks")
                    total_tasks = int(input("Enter the number of task: "))
                    with open("tasks.txt", "a") as task_file:
                        for i in range(total_tasks):
                            task = input(f"Enter task {i + 1}: ")
                            tasks.append(task)
                            task_file.write(f"{i+1}: {task}\n")
                    say("Tasks are scheduled")

                elif "show my schedule" in query:
                    from pygame import mixer
                    from plyer import notification
                    with open("tasks.txt", "r") as task_file:
                        content = task_file.read()
                        mixer.init()
                        mixer.music.load("Z:/Stuffs/Project/AI/Sounds/notific.wav")
                        mixer.music.play()
                        notification.notify(
                            title = "My Schedule:- ",
                            message = content,
                            timeout = 5
                        )     

                elif "show my internet speed" in query:
                    say("Fetching, Sir Please wait")
                    from speedtest import Speedtest
                    wifi = Speedtest()
                    upload_net = wifi.upload()/1048576             #1Mb = (1024*1024) bytes
                    download_net = wifi.download()/1048576
                    print(f"Upload speed: {upload_net:.2f} Mb/s")
                    print(f"Download speed: {download_net:.2f} Mb/s")
                    say(f"Upload speed is {upload_net:.2f} MegaBye per second")
                    say(f"Download speed is {download_net:.2f} MegaBye per second")

                elif "let's play a game" in query:
                    from miniGame import game
                    game()

                elif "capture screen" in query:
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("Z:/Stuffs/Project/AI/Sounds/ss_capture.mp3")
                    mixer.music.play()
                    capt = pyg.screenshot()
                    path = "Z:/Stuffs/Project/AI/Captures/"
                    file_name = "ss" + datetime.datetime.now().strftime("-%Y-%m-%d-%H-%M-%S") + ".png"
                    file_path = path + file_name
                    capt.save(file_path)
                    sleep(0.3)

                elif "click photo" in query:
                    pyg.press("super")
                    sleep(0.2)
                    pyg.typewrite("camera")
                    sleep(0.5)
                    pyg.press("enter")
                    say("Say Cheese")
                    sleep(2)
                    pyg.press("enter")

                elif "click again" in query:
                    pyg.press("enter")

