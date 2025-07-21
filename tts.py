from gtts import gTTS
import io
import pygame

def speak(text, lang='en'):
    """
    Converts text to speech and plays audio directly from memory.

    Parameters:
        text (str): The text to convert to speech.
        lang (str): The language code for the text (default is 'en').

    Returns:
        None
    """
    try:
        # Generate speech from text
        tts = gTTS(text=text, lang=lang, slow=False)
        
        # Store audio in memory
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)

        # Initialize pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.load(audio_data, 'mp3')  # Load the audio from memory
        pygame.mixer.music.play()

        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
speak(" Once upon a time, a curious little fox named Finn found a shiny golden key in the forest. He searched high and low, wondering what it might unlock, until he stumbled upon a hidden door in an ancient oak tree. Inside, he discovered a magical library filled with books that could transport him to faraway lands. Finn spent his days exploring worlds beyond imagination, making friends with dragons and giants. And so, the little fox who once roamed the woods became the greatest adventurer of them all.", lang='en')
