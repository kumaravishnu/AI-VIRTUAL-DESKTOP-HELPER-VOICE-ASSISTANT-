import google.generativeai as genai
import speech_recognition as sr
from elevenlabstest import speak
from dotenv import load_dotenv 
import os 

load_dotenv()
# Configure Gemini API with your actual key
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

# Initialize the Generative Model
model = genai.GenerativeModel("gemini-1.5-flash")

# Variable to store conversation history
conversation_history = []

# Function to generate conversational content from Gemini
def get_gemini_response(user_input):
    # Add the current user input to conversation history
    conversation_history.append(f"User: {user_input}")
    
    # Create the full conversation context by joining all previous interactions
    context = "\n".join(conversation_history)
    
    # Generate content based on the full context (including history)
    response = model.generate_content(context)
    clean_text = response.text.replace("*", "")  # Remove asterisks if any
    
    # Add the response to conversation history
    conversation_history.append(f"Chatbot: {clean_text}")
    
    return clean_text

# Voice interaction using Speech Recognition
def listen_and_respond():
    recognizer = sr.Recognizer()
    
    # Enable microphone input
    with sr.Microphone() as source:
        speak("Listening for a question... Please speak now.")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            print("Processing your speech...")
            user_query = recognizer.recognize_google(audio)
            speak(f"You said: {user_query}")
            
            # Get Gemini chatbot response based on conversation history
            chatbot_reply = get_gemini_response(user_query)
            
            # Split response into sentences and give a summary
            sentences = chatbot_reply.split(". ")
            summary = ". ".join(sentences[:4])  # Get the first 4 sentences
            
            # Speak the summary and print the full text
            speak(summary)
            speak("For more details, please check the printed text.")
            print(f"Response from Gemini:\n{chatbot_reply}")
            
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please speak clearly.")
        except sr.RequestError as e:
            speak(f"Error with the speech recognition service: {e}")

# Start Chat Mode
listen_and_respond()
