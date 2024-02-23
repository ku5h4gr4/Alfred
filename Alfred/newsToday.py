import requests
import json
from voice import say
from fetchapi import key

# todo: add your api key
api = key("news")

news_dict = [["business",f"https://newsapi.org/v2/top-headlines?country=in&category={api}"],
             ["entertainment",f"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey={api}"],
             ["health",f"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={api}"],
             ["science",f"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey={api}"],
             ["sports",f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={api}"],
             ["technology",f"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={api}"]]


def latestNews():
    count = 0
    url = None
    say("Offcourse,Sir")
    say("Which field news do you want:-\nBusiness , Health, Science, Entertainment, Sports, Technology")
    print("Which field news do you want:-\nBusiness , Health, Science, Entertainment, Sports, Technology")
    field = input("Enter here: ")
    for topic in news_dict:
        if topic[0].lower() in field.lower():
            url = topic[1]
            say("News found")
            break
        else:
            url = True
    if url is True:
        say("Url not found")

    news = requests.get(url).text
    news = json.loads(news)
    say("News of the day")

    arts = news["articles"]
    for article in arts:
        news_text = article["title"]
        print(news_text)
        say(news_text)
        news_url = article["url"]
        print(f"More info--> {news_url}\n")
        count += 1
        if count/5==1 or count/5==2 or count/5==3 or count/5==4:     # you can use a interval of 5- count/5== 1 or 2 or 3
            say("Do you wish to continue?")
            cont = input("Enter here[y/n]: ")
            if str(cont) == "y":
                pass
            else:
                break
        say("Moving on to the next news")
