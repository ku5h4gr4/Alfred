from voice import say
import pywhatkit
from micFun import listen
import webbrowser
import wikipedia
import pyautogui as pyg
from time import sleep


query = listen().lower()


def googleSearch(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("Alfred","")
        query = query.replace("google search","")
        query = query.replace("google","")
        say("This is what I found on google")
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,2)
            say(result)
        except:
            say("Didn't find Output to speak")


def youtubeSearch(query):
    if "youtube" in query:
        say("Sure;Sir!")
        query = query.replace("Alfred", "")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        sleep(3)
        pyg.press("k")
        say("Playing your song")

def wikipediaSearch(query):
    if "wikipedia" in query:
        query = query.replace("Alfred","")
        query = query.replace("wikipedia search","")
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query,sentences = 7)
        say("According to wikipedia")
        print(result)
        say(result)
