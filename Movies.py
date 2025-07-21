from elevenlabstest import speak
import speech_recognition 
from imdb import IMDb
import datetime



def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("understanding")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "none"
    return query

# Function for searching movie
def search_movie():
    # Gathering information from IMDb
    moviesdb = IMDb()

    # Search for title
    speak("What movie would you like to know about?")
    text = takeCommand()

    if text == "none":
        speak("I didn't catch that. Please try again.")
        return

    # Passing input for searching movie
    movies = moviesdb.search_movie(text)

    speak("Searching for " + text)
    if len(movies) == 0:
        speak("No results found.")
    else:
        speak("I found these:")

        for movie in movies:
            title = movie.get('title', 'Unknown Title')
            year = movie.get('year', 'Unknown Year')
            speak(f'{title} - {year}')

            info = movie.getID()
            movie = moviesdb.get_movie(info)

            title = movie.get('title', 'Unknown Title')
            year = movie.get('year', 'Unknown Year')
            rating = movie.get('rating', 'No Rating Available')
            plot = movie.get('plot outline', 'No Plot Available')

            # Handling past and future releases
            if year != 'Unknown Year' and year < int(datetime.datetime.now().year):
                print(
                    f'{title} was released in {year} with an IMDb rating of {rating}. '
                    f'The plot summary of the movie is: {plot}'
                )
                speak(
                    f'{title} was released in {year} with an IMDb rating of {rating}. '
                    f'The plot summary of the movie is: {plot}'
                )
                break
            else:
                print(
                    f'{title} will release in {year} with an IMDb rating of {rating}. '
                    f'The plot summary of the movie is: {plot}'
                )
                speak(
                    f'{title} will release in {year} with an IMDb rating of {rating}. '
                    f'The plot summary of the movie is: {plot}'
                )
                break


