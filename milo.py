import random
import sys
import webbrowser
from elevenlabstest import speak
import requests
import speech_recognition as sr
import datetime
import os
import pyautogui
from plyer import notification
from pygame import mixer
import speedtest
import time
import subprocess
from Email import send_email
from imageGeneration import generate_image, speak_text

from dotenv import load_dotenv 
import os 

load_dotenv()

HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")
apiKey = os.getenv("apiKey")
contacts = {
    "arjun": os.getenv("arjun"),
    "she": os.getenv("she"),
    "jefferson": os.getenv("jefferson")
}
weather_api_key = os.getenv("weather_api_key")
news_api_key = os.getenv("news_api_key")
wolfram_alpha_app_id = os.getenv("wolfram_alpha_app_id")
api_key = os.getenv("api_key") 
api__key = os.getenv("api__key")
api___key = os.getenv("api___key")


for i in range(3):
    a = input("Enter Password to open milo :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
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


def alarm(query):
    with open("alarmtext.txt", "a") as timehere:
        timehere.write(query)
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, you can call me anytime.")
                    break

                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")
                
                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                
                elif "show my schedule" in query:
                   file = open("tasks.txt","r")
                   content = file.read()
                   file.close()
                   mixer.init()
                   mixer.music.load("mixkit-digital-quick-tone-2866.wav")
                   mixer.music.play()
                   notification.notify(
                     title = "My schedule :-",
                     message = content,
                     timeout = 15
                    )

                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO ]"))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\Admin\\OneDrive\\Desktop\\Ai desktop assistant\\focusmode.py")
                        exit()

                    
                    else:
                        pass
                
                elif "show my focus" in query:
                    from FocusGraph import generate_graph
                    generate_graph()

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("milo","")
                    query = query.replace("translate","")
                    translategl(query)
                
                elif "movie" in query:
                    from Movies import search_movie
                    search_movie()
                

                   
                   
                elif "send an email" in query:
                    speak("On what email address do you want to send, sir? Please enter in the terminal.")
                    receiver_add = input("Email address: ")
                    speak("What should be the subject, sir?")
                    subject = takeCommand().capitalize()
                    speak("What is the message?")
                    message = takeCommand().capitalize()
            
                    if send_email(receiver_add, subject, message):
                     speak("I have sent the email, sir.")
                     print("I have sent the email, sir.")
                    else:
                     speak("Something went wrong. Please check the error log.")

                elif " ip address" in query:
                    speak("Checking")
                    try:
                      ipAdd = requests.get('https://api.ipify.org').text
                      print(ipAdd)
                      speak("your ip adress is")
                      speak(ipAdd)
                    except Exception as e:
                      speak("network is weak, please try again some time later" ) 
                
                elif "refresh" in query:
                    pyautogui.moveTo(1472,406, duration=2)
                    pyautogui.click(button='right')
                    time.sleep(1)  # Give time for the context menu to open
                    pyautogui.moveTo(1546,514, duration=1)  
                    pyautogui.click()
                 
                
                elif "scroll down" in query:
                    pyautogui.scroll(1000)

                elif "rectangular spiral" in query:
                    
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.write('paint')
                    time.sleep(1)
                    pyautogui.press('enter')
                    time.sleep(5)
                    screen_width, screen_height = pyautogui.size()
                    center_x = screen_width // 2
                    center_y = screen_height // 2
                    pyautogui.moveTo(center_x, center_y)
                    pyautogui.click()
                    distance = 300
                    while distance > 0:
                      pyautogui.dragRel(distance, 0, duration=0.5, button='left')   # Right
                      distance -= 10
                      pyautogui.dragRel(0, distance, duration=0.5, button='left')   # Down
                      pyautogui.dragRel(-distance, 0, duration=0.5, button='left')  # Left
                      distance -= 10
                      pyautogui.dragRel(0, -distance, duration=0.5, button='left')  # Up
 
                elif "fetch score" in query:
                    from FetchScore import get_cricket_scores
                    get_cricket_scores()
                    
                elif "open" in query:   
                    query = query.replace("open","")
                    query = query.replace("milo","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 
                
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

                elif "play a game" in query:
                    from game import game_play
                    game_play()

                elif "screenshot" in query:
                     speak("Taking screenshot, sir.")
                     im = pyautogui.screenshot()
                     im.save("my.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")  # Opens the start menu
                    pyautogui.typewrite("camera")  # Types 'camera' to search for the Camera app
                    pyautogui.press("enter")  # Opens the Camera app
                    time.sleep(5)  # Waits for the camera to launch
                    speak("SMILE")  # Prompts the user to smile
                    time.sleep(2)  # Gives a little pause
                    pyautogui.press("enter")  # Takes the photo
                    time.sleep(2)  # Waits to ensure the photo is taken
                    subprocess.run(["taskkill", "/IM", "WindowsCamera.exe", "/F"])  # Closes the Camera app


                 
                
                elif "hello" in query:
                    speak("Hello sir, how are you?")
                elif "i am fine" in query:
                    speak("That's great, sir.")
                elif "how are you" in query:
                    speak("Perfect, sir.")
                elif "thank you" in query:
                    speak("You are welcome, sir.")
                
                # Media controls
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused.")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played.")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted.")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up, sir.")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir.")
                    volumedown()

                # Opening and closing applications
                elif "open" in query:
                    from dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from dictapp import closeappweb
                    closeappweb(query)

                # Play random song
                elif "tired" in query:
                    speak("Playing your favourite songs, sir.")
                    a = (1, 2, 3)  # Choose any number of songs
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=anUz77ElBK4")

                # Searching
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                 
                
                # Temperature and weather
                elif "temperature" in query:
                    from temperature import handle_query
                    handle_query(query)
                elif "weather" in query:
                    from weather import handle_query
                    handle_query(query)

                # Alarm
                elif "set an alarm" in query:
                   print("Input time example: 10 and 10 and 10")
                   speak("Set the time.")
                   a = input("Please tell the time: ")
                   alarm(a)
                   speak("Done, sir.")
     
                #News Function
                elif "news" in query:
                  from NewsRead import latestnews
                  latestnews()
                
                #whatsapp function
                elif "whatsapp" in query:
                  from Whatsapp import sendMessage
                  sendMessage()

                #calculate
                elif "calculate" in query:
                 from Calculatenumbers import WolfRamAlpha
                 from Calculatenumbers import Calc
                 query = query.replace("calculate","")
                 query = query.replace("jarvis","")
                 Calc(query)
                
               
                
                # Time check
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                
                # Memory functions
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "").replace("milo", "")
                    speak("You told me to remember that " + rememberMessage)
                    with open("Remember.txt", "a") as remember:
                        remember.write(rememberMessage + "\n")
               
                elif "what do you remember" in query:
                    with open("Remember.txt", "r") as remember:
                        remember_contents = remember.read().strip()
                    if remember_contents:
                        speak("You told me to remember that " + remember_contents)
                    else:
                        speak("I don't have anything to remember.")

                if "shutdown the system" in query:
                   speak("Are you sure you want to shut down?")
                   shutdown = input("Do you wish to shut down your computer? (yes/no): ").lower()
                   if shutdown == "yes":
                     os.system("shutdown /s /t 1")
                   elif shutdown == "no":
                    speak("Shutdown canceled.")

                if "restart the system" in query:
                    speak("Are you sure you want to restart?")
                    restart = input("Do you wish to restart your computer? (yes/no): ").lower()
                    if restart == "yes":
                      os.system("shutdown /r /t 1")
                    elif restart == "no":
                      speak("Restart canceled.")
                
                if "lock the system" in query:
                    speak("Are you sure you want to lock the system?")
                    lock = input("Do you wish to lock your computer? (yes/no): ").lower()
                    if lock == "yes":
                     os.system("rundll32.exe user32.dll,LockWorkStation")
                    elif lock == "no":
                     speak("Lock canceled.")

                if "sleep the system" in query:
                  speak("Are you sure you want to put the system to sleep?")
                  sleep = input("Do you wish to sleep your computer? (yes/no): ").lower()
                  if sleep == "yes":
                   os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                  elif sleep == "no":
                   speak("Sleep canceled.")

                elif "finally sleep" in query:
                   speak("Going to sleep.")
                   exit()
