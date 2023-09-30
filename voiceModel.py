from gtts import gTTS
import pygame
import tempfile
import os

# Text to be converted to speech
text_to_speak = "Hello, this is a text-to-speech example on Raspberry Pi."

# Create a temporary file to store the audio
temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name

try:
    # Create a gTTS (Google Text-to-Speech) object
    tts = gTTS(text=text_to_speak, lang="en")

    # Save the audio to the temporary file
    tts.save(temp_audio_file)

    # Initialize the pygame mixer
    pygame.mixer.init()

    # Load the temporary audio file
    pygame.mixer.music.load(temp_audio_file)

    # Play the audio
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Clean up the temporary audio file
    os.remove(temp_audio_file)
