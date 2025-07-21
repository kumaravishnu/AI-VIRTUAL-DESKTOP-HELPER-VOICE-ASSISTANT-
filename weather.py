import requests
from bs4 import BeautifulSoup
from elevenlabstest import speak

def get_weather(location):
    search = f"weather in {location}"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    
    # Parse temperature
    temp = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
    
    # Parse weather description
    description = data.find("div", class_="BNeawe tAd8D AP7Wnd").text
    
    return temp, description

def handle_query(query):
    if "temperature" in query or "weather" in query:
        location = query.split("in")[-1].strip()
        temp, description = get_weather(location)
        
        if "temperature" in query:
            speak(f"The current temperature in {location} is {temp}")
        elif "weather" in query:
            speak(f"The current weather in {location} is {temp} with {description}")