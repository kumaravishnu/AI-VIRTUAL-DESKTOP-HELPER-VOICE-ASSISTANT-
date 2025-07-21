import requests
from dotenv import load_dotenv 
import os 

load_dotenv()
api_key = os.getenv("ELEVEN_LABS_API_KEY")


def speak(audio):
    import io
    from pygame import mixer



    voice_id = "XrExE9yKIg1WjnnlVkGX"  # Replace with the desired Eleven Labs voice ID

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }
    data = {
        "text": audio,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        # Use a BytesIO stream to handle the audio data in memory
        audio_stream = io.BytesIO(response.content)
        audio_stream.seek(0)

        # Play the audio directly using pygame
        mixer.init()
        mixer.music.load(audio_stream, "mp3")
        mixer.music.play()
        
        # Wait until playback finishes
        while mixer.music.get_busy():
            pass
    else:
        print("Error:", response.status_code, response.text)

