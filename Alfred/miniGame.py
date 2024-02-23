from voice import say
from micFun import listen
import random


def game():
    say("Let's Play Rock,Paper,Scissor")
    say("Say Rock, Paper or Scissor")
    round = 0
    usr_score = 0
    bot_score = 0
    while(round<5):
        choose = ("rock","paper","scissor")
        bot = random.choice(choose)
        query = listen().lower()
        if (query == "rock"):
            if (bot == "rock"):
                say("Rock")
                print(f"Score:-\n[User: {usr_score}]\t[Bot: {bot_score}\n]")
            elif (bot == "paper"):
                say("paper")
                bot_score += 1
                print(f"Score:-\n[User: {usr_score}]\t[Bot: {bot_score}\n]")
            else:
                say("Scissor")
                usr_score += 1
                print(f"Score:-\n[User: {usr_score}]\t[Bot: {bot_score}\n]")
        elif (query == "paper"):
            if (bot == "paper"):
                say("Paper")
                print(f"Score:-\n[User: {usr_score}]\t[Bot: {bot_score}\n]")
            elif (bot == "scissor"):
                say("scissor")
                bot_score += 1
                print(f"Score:-\n[User: {usr_score}]\t[Bot: {bot_score}\n]")
            else:
                say("Rock")
                usr_score += 1
                print(f"Score:-\n[User: {usr_score}]\t[Bot: {bot_score}\n]")
        elif (query == "scissor" or query == "caesar"):
            if (bot == "scissor"):
                say("scissor")
                print(f"Score:-\n[User: {usr_score}]\t[Bot: {bot_score}\n]")
            elif (bot == "rock"):
                say("scissor")
                bot_score += 1
                print(f"Score:-\n[User: {usr_score}]\t[Bot: {bot_score}\n]")
            else:
                say("Paper")
                usr_score += 1
                print(f"Score:-\n[User: {usr_score}]\t[Bot: {bot_score}\n]")
        round += 1
    print(f"Final Score:- User--> {usr_score}\tBot--> {bot_score}")
    if usr_score>bot_score:
        say("You win")
    elif usr_score<bot_score:
        say("I win")
    else:
        say("Game Draw")
    say("Exiting game")
