import pywhatkit
from elevenlabstest import speak
import datetime
import speech_recognition as sr
from datetime import timedelta, datetime
import pyautogui  # Import pyautogui for mouse click simulation
import time


contacts = {
    "arjun": "+917598488063",
    "she": "+919952984706",
    "jefferson":"+917358223130"
}

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again, please.")
        return "None"
    return query.lower()

def sendMessage():
    speak("Who do you want to message?")
    contact_name = takeCommand()

    if contact_name == "None":
        speak("I didn't catch that. Please try again.")
        return

    contact_name = contact_name.lower()

    phone_number = contacts.get(contact_name)

    if not phone_number:
        speak(f"I don't have a contact named {contact_name}.")
        return

    speak("What's the message?")
    message = takeCommand()

    if message == "None":
        speak("I didn't catch the message. Please try again.")
        return

    strTime = int(datetime.now().strftime("%H"))
    update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))

    try:
        pywhatkit.sendwhatmsg(phone_number, message, time_hour=strTime, time_min=update)

        # Wait for WhatsApp Web to open and the message to be typed
        time.sleep(15)

        # Click the send button using pyautogui
        pyautogui.click(x=1300, y=950)  # Coordinates of the send button

        speak("Message sent successfully.")
    except Exception as e:
        speak("Sorry, I couldn't send the message. Please try again.")

if __name__ == "__main__":
    sendMessage()

