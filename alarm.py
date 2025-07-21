from elevenlabstest import speak
import datetime
import os
import time as t


# Read and process the alarm time
try:
    with open("alarmtext.txt", "rt") as extractedtime:
        time_content = extractedtime.read().strip()
    # Clear the content of the file after reading
    with open("alarmtext.txt", "r+") as deletetime:
        deletetime.truncate(0)
except FileNotFoundError:
    speak("The alarm file is missing.")
    time_content = None

def ring(time_content):
    if not time_content:
        speak("No valid time found to set the alarm.")
        return

    # Processing the time string
    timenow = time_content.lower().replace("milo", "").replace("set an alarm", "").replace(" and ", ":").strip()
    try:
        datetime.datetime.strptime(timenow, "%H:%M:%S")  # Validate time format
        Alarmtime = timenow
        print("Alarm set for:", Alarmtime)
        speak(f"Alarm set for {Alarmtime}")
    except ValueError:
        speak("The alarm time format is invalid. Please use HH:MM:SS format.")
        return

    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing, sir.")
            if os.path.exists("morning_glory.mp3"):
                os.startfile("morning_glory.mp3")
            else:
                speak("The alarm sound file is missing.")
            break  # Stops the loop after the alarm starts
        t.sleep(1)  # Prevent CPU overload

if time_content:
    ring(time_content)
