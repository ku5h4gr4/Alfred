import wolframalpha
from voice import say
from fetchapi import key


def wolfapi(query):
    # todo: Add your api key
    api = key("wolfram")
    requester = wolframalpha.Client(api)
    requested = requester.query(query)
    try:
        solution = next(requested.results).text
        return solution
    except:
        say("Not Answerable")
def calc(query):
    term = str(query)
    term = term.replace("divide","/")
    term = term.replace("plus","+")
    term = term.replace("minus","-")
    term = term.replace("into","*")
    term = term.replace("by","/")
    final = str(term)
    try:
        result = wolfapi(final)
        print(f"Solution--> {result}")
        say(result)
    except:
        say("Not Answerable")