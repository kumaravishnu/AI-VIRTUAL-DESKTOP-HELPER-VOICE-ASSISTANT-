import requests
from bs4 import BeautifulSoup
from elevenlabstest import speak


def get_temperature(location):
    search = f"temperature in {location}"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    return temp

def handle_query(query):
    if "temperature" in query or "weather" in query:
        # Extract the location from the query
        location = query.split("in")[-1].strip()
        temperature = get_temperature(location)
        speak(f"The current temperature in {location} is {temperature}")

