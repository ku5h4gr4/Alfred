import datetime
from voice import say


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        say("Good Morning;Sir")
    elif hour > 12 and hour <= 17:
        say("Good AfterNoon;Sir")
    else:
        say("good Evening;Sir")
    say("How Can I help You? ")
