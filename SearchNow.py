import speech_recognition
from elevenlabstest import speak
import pywhatkit
import wikipedia
import webbrowser

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
 

def searchGoogle(query):
    if "google" in query:
        query = query.replace("milo", "").replace("google search", "").replace("google", "").strip()
        if not query:
            speak("Please provide a valid search query for Google.")
            return
        speak("This is what I found on Google.")
        try:
            pywhatkit.search(query)
            result = wikipedia.summary(query, sentences=1)
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options[:5]
            speak("Your search term has multiple meanings. Here are some options.")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            speak(f"Please refine your query by specifying one of these options: {', '.join(options)}")
        except wikipedia.exceptions.PageError:
            speak("No detailed information found for this query on Wikipedia.")
        except Exception as e:
            speak("No speakable output is available for this query.")
            print("Error:", e)

def searchYoutube(query):
    if "youtube" in query:
        query = query.replace("youtube search", "").replace("youtube", "").replace("milo", "").strip()
        if not query:
            speak("Please provide a valid search query for YouTube.")
            return
        speak("This is what I found for your search.")
        try:
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("Successfully done.")
        except Exception as e:
            speak("I couldn't play the video on YouTube. Please try again.")
            print("Error:", e)

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("milo", "").replace("wikipedia", "").replace("search wikipedia", "").strip()
        if not query:
            speak("Please provide a valid search query.")
            return
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia..")
            print(results)
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options[:5]
            speak("Your search term has multiple meanings. Here are some options.")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            speak(f"Please refine your query by specifying one of these options: {', '.join(options)}")
        except wikipedia.exceptions.PageError:
            speak("No page found for your query. Please try a different search term.")
        except Exception as e:
            speak("An error occurred while searching Wikipedia. Please try again.")
            print("Error:", e)

query = takeCommand().lower()
searchGoogle(query)
searchYoutube(query)
searchWikipedia(query)




