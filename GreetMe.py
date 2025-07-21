import datetime
from elevenlabstest import speak

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
   
    elif hour >12 and hour<18:
        speak("good afternoon sir")
    
    else:
        speak("good evening,sir")

    speak("please tell me,how can i help you?")
