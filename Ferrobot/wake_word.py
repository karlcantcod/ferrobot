



# This module handles wake-word detection using the Porcupine library.
# It listens for one of the predefined wake words (e.g., "computer", "hey google", "alexa")
# and activates the virtual assistant when detected.
# It also provides visual feedback using LEDs.





# wake_word.py
import os
import sys
import struct
import pyaudio
import time
from colorama import Fore
import pvporcupine
import RPi.GPIO as GPIO
from config import PV_ACCESS_KEY, LED1_PIN, LED2_PIN

def wake_word():
    """
    Listens for a wake word and turns on LEDs when detected.
    """
    keywords = ["computer", "hey google", "alexa"]
    porcupine = pvporcupine.create(
        keywords=keywords,
        access_key=PV_ACCESS_KEY,
        sensitivities=[0.1, 0.1, 0.1]
    )

    # Suppress stderr from Porcupine
    devnull = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(2)
    sys.stderr.flush()
    os.dup2(devnull, 2)
    os.close(devnull)

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    detected = False
    while not detected:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            GPIO.output(LED1_PIN, GPIO.HIGH)
            GPIO.output(LED2_PIN, GPIO.HIGH)
            keyword = keywords[keyword_index]
            print(Fore.GREEN + f"\n{keyword} detected\n")
            audio_stream.stop_stream()
            audio_stream.close()
            porcupine.delete()
            # Restore stderr
            os.dup2(old_stderr, 2)
            os.close(old_stderr)
            detected = True
