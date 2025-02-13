





# This module handles audio recording and voice activity detection.
# It provides functions to listen for speech and detect when a user has stopped speaking.
# It also includes a threaded Recorder class that continuously collects PCM audio data
# until instructed to stop.





# recorder.py
import struct
import time
import threading
import pyaudio
import pvcobra
from pvrecorder import PvRecorder
import RPi.GPIO as GPIO
from config import PV_ACCESS_KEY, LED1_PIN, LED2_PIN

def listen():
    """
    Listens for a voice signal using Cobra.
    """
    cobra = pvcobra.create(access_key=PV_ACCESS_KEY)
    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=cobra.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=cobra.frame_length
    )

    print("Listening...")
    while True:
        pcm = stream.read(cobra.frame_length)
        pcm = struct.unpack_from("h" * cobra.frame_length, pcm)
        if cobra.process(pcm) > 0.3:
            print("Voice detected")
            stream.stop_stream()
            stream.close()
            cobra.delete()
            break

def detect_silence():
    """
    Monitors for silence (using Cobra) to signal the end of a query.
    """
    cobra = pvcobra.create(access_key=PV_ACCESS_KEY)
    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=cobra.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=cobra.frame_length
    )

    last_voice_time = time.time()
    while True:
        pcm = stream.read(cobra.frame_length)
        pcm = struct.unpack_from("h" * cobra.frame_length, pcm)
        if cobra.process(pcm) > 0.2:
            last_voice_time = time.time()
        else:
            if time.time() - last_voice_time > 1.3:
                print("End of query detected\n")
                GPIO.output(LED1_PIN, GPIO.LOW)
                GPIO.output(LED2_PIN, GPIO.LOW)
                stream.stop_stream()
                stream.close()
                cobra.delete()
                break

class Recorder(threading.Thread):
    """
    A threaded recorder that accumulates PCM audio data.
    """
    def __init__(self):
        super().__init__()
        self._pcm = []
        self._is_recording = False
        self._stop_flag = False

    def run(self):
        self._is_recording = True
        recorder = PvRecorder(device_index=-1, frame_length=512)
        recorder.start()
        while not self._stop_flag:
            self._pcm.extend(recorder.read())
        recorder.stop()
        self._is_recording = False

    def stop(self):
        self._stop_flag = True
        while self._is_recording:
            time.sleep(0.01)
        return self._pcm
