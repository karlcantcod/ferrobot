






# This module is responsible for converting text to speech using Google Cloud Text-to-Speech.
# It synthesizes the provided text into an MP3 file and then plays the audio using pygame.
# This allows the virtual assistant to "speak" its responses.







# tts.py
import os
import time
import pygame
from google.cloud import texttospeech
from config import GCLOUD_TTS_CLIENT

def voice(text):
    """
    Synthesizes the given text to an MP3 file using Google Cloud TTS,
    then plays it using pygame.
    """
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice_params = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Journey-D",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
    )
    response = GCLOUD_TTS_CLIENT.synthesize_speech(
        input=synthesis_input,
        voice=voice_params,
        audio_config=audio_config
    )

    output_file = "speech.mp3"
    with open(output_file, "wb") as out:
        out.write(response.audio_content)
    print(f"Audio content written to file '{output_file}'")

    pygame.mixer.init()
    try:
        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
    except Exception as e:
        print(f"Error playing audio: {e}")
    time.sleep(0.2)
