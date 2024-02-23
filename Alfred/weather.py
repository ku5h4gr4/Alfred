import datetime
import requests
from micFun import listen
from voice import say
import re
from fetchapi import key


query = listen().lower


def convert_temperature(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit
def climate(query):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    # todo: add your api key here
    api_key = key("weather")
    match = re.search(r"(temperature in|temperature at|what's the temperature in) (\w+)", query, re.IGNORECASE)
    if match:
        city = match.group(2)
    else:
        say("Sorry, I couldn't understand the city name")
        return

    try:
        url = base_url + "appid=" + api_key + "&q=" + city
        response = requests.get(url).json()

        temp_kelvin = response["main"]["temp"]
        temp_celsius, temp_fahrenheit = convert_temperature(temp_kelvin)

        wind_speed = response["wind"]["speed"]
        humidity = response["main"]["humidity"]
        descript = response["weather"][0]["description"]
        sunrise_time = datetime.datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"]).strftime("%H:%M:%S")
        sunset_time = datetime.datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"]).strftime("%H:%M:%S")

        say(f"Temperature in {city} is {temp_celsius:.2f} celsius; {descript}")
        print(f"Temperature in {city} is {temp_celsius:.2f} celsius; {descript}")
        say(f"Humidity is {humidity} percent")
        print(f"Humidity is {humidity} percent")
        say(f"Wind speed is {wind_speed} meter per second")
        print(f"Wind speed is {wind_speed} meter per second")
        say(f"Sun rises at {sunrise_time}")
        print(f"Sun rises at {sunrise_time}")
        say(f"Sun sets at {sunset_time}")
        print(f"Sun sets at {sunset_time}")

    except Exception as e:
        say(f"Sorry, an error occurred: {str(e)}")
