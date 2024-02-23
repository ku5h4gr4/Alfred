import datetime
from pygame import mixer
from voice import say
from time import sleep

mixer.init()

with open("Alarm.txt","rt") as extractedtime:
    time = extractedtime.read()
    Time = str(time)

with open("Alarm.txt","r+") as deletetime:
    deletetime.truncate(0)


def ringAlarm(time):
    timeset = str(time)
    timenow = timeset.replace("alfred","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace("for","")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            say("Alarm Ringing")
            mixer.music.load("Z:/Stuffs/Project/AI/Sounds/Morning_Drift_[NCS_Release].mp3")
            mixer.music.play()
            # os.startfile("Z:/Stuffs/Project/AI/Sounds/Morning_Drift_[NCS_Release].mp3")
            # sleep(25)
            # exit()
        elif currenttime + "00:00:10" == Alarmtime:
            exit()

ringAlarm(time)