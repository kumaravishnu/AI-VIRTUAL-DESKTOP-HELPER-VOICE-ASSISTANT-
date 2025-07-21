import requests
import speech_recognition as sr
from elevenlabstest import speak
from PIL import Image
from io import BytesIO

# Replace with your Hugging Face API Key
HUGGING_FACE_API_KEY = "***REMOVED***"

def speak_text():
    """
    Captures voice input from the user and converts it to text.
    Returns:
        str: Recognized text prompt.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for your query. Please speak now.")
        print("Listening for your query...")
        
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        
        try:
            audio = recognizer.listen(source, timeout=5)  # Set a timeout for listening
            print("Processing your speech...")
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that. Please try again.")
            print("Sorry, I didn't understand that. Please try again.")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
        except sr.WaitTimeoutError:
            speak("No speech detected. Please try again.")
            print("No speech detected. Please try again.")
    return None

def generate_image(prompt):
    """
    Generates an image from a given text prompt using the Hugging Face API.
    Args:
        prompt (str): Text description for the image.
    """
    try:
        print(f"Generating image for prompt: {prompt}")

        # Hugging Face API endpoint
        api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

        # API headers
        headers = {
            "Authorization": f"Bearer {HUGGING_FACE_API_KEY}",
            "Content-Type": "application/json",
        }

        # API payload
        payload = {"inputs": prompt}

        # Sending the request
        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code == 200:
            # Load and display the image
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            speak("Your image is ready. Displaying it now.")
            print("Displaying the generated image...")
            image.show()
        else:
            print(f"Error generating image: {response.status_code} {response.text}")

    except Exception as e:
        print(f"Error generating image: {e}")

if __name__ == "__main__":
    speak("Voice-activated image generation is starting now.")
    print("Voice-activated image generation started!")
    prompt = speak_text()
    if prompt:
        speak(f"You said: {prompt}")
        print(f"received: {prompt}")
        generate_image(prompt)
    else:
        print("No prompt provided. Exiting.")