import requests
import json
from elevenlabstest import speak

def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?category=business&apiKey=***REMOVED***",
        "entertainment": "https://newsapi.org/v2/top-headlines?&category=entertainment&apiKey=***REMOVED***",
        "health": "https://newsapi.org/v2/top-headlines?category=health&apiKey=***REMOVED***",
        "science": "https://newsapi.org/v2/top-headlines?category=science&apiKey=***REMOVED***",
        "sports": "https://newsapi.org/v2/top-headlines?category=sports&apiKey=***REMOVED***",
        "technology": "https://newsapi.org/v2/top-headlines?category=technology&apiKey=***REMOVED***"
    }

    content = None
    url = None
    speak("Which field of news do you want? [business], [health], [technology], [sports], [entertainment], or [science]")
    field = input("Type the field of news that you want: ")

    url = api_dict.get(field.lower())
    
    if url is None:
        speak("Sorry, I couldn't find the news field you requested.")
        return

    try:
        response = requests.get(url)
        if response.status_code != 200:
            speak(f"Error fetching the news. Status code: {response.status_code}")
            return
        news = response.json()

        speak("Here is the first news.")

        arts = news.get("articles", [])
        if not arts:
            speak("Sorry, no news articles were found.")
            return

        for articles in arts:
            article = articles.get("title", "No Title Available")
            summary = articles.get("description", articles.get("content", "Summary not available"))

            print(f"Title: {article}")
            print(f"Summary: {summary}\n")
            speak(f"Title: {article}")
            speak(f"Summary: {summary}")
            
            news_url = articles.get("url", "No URL Available")
            print(f"For more info visit: {news_url}")

            a = input("[Press 1 to continue] and [Press 2 to stop]: ")
            if str(a) == "2":
                break

        speak("That's all for now.")
    except requests.exceptions.RequestException as e:
        speak("Network error occurred while fetching the news. Please try again later.")
        print(f"Network Error: {e}")
    except json.JSONDecodeError as e:
        speak("There was an issue with the news response. Please try again later.")
        print(f"JSON Error: {e}")

# Call the function to get the latest news
latestnews() 