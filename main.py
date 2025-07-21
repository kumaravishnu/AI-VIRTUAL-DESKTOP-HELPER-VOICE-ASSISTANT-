import os
import eel
import subprocess
from features import *
from milo import *
from auth import recoganize

def start():
    # Initialize eel with the "www" folder where your HTML files are located
    eel.init("www")

    # Play the assistant's sound on startup
    playAssistantSound()

    # Expose the init function to be called from the frontend
    @eel.expose
    def init():
        subprocess.call([r'device.bat'])  # Run the batch file (make sure it works properly)
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can I help you?")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Failed")

    # Start the Eel web app (this will automatically open the browser)
    eel.start('index.html', mode=None, host='localhost', block=True)

# If you want to manually start the browser with MS Edge, you can keep this line,
# but it should only be necessary if you need to do so after the server is started.
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

if __name__ == "__main__":
    start()
