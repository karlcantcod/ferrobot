



# config.py


# This module provides global configuration for the virtual assistant application.
# It initializes API keys, model settings, hardware configuration (such as GPIO for LED control),
# and common variables (like conversation prompts and initial chat log).
# It also sets up clients for external services like OpenAI, Google Cloud Text-to-Speech, and AWS Polly.



import os
import RPi.GPIO as GPIO
import boto3
import openai
from google.cloud import texttospeech

# API keys and model settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PV_ACCESS_KEY = os.getenv("PV_ACCESS_KEY")
GPT_MODEL = "gpt-4"

# Initialize API clients
openai.api_key = OPENAI_API_KEY
POLLY_CLIENT = boto3.client('polly')
GCLOUD_TTS_CLIENT = texttospeech.TextToSpeechClient()

# LED configuration (using the Raspberry Pi GPIO pins)
LED1_PIN = 18
LED2_PIN = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.output(LED1_PIN, GPIO.LOW)
GPIO.setup(LED2_PIN, GPIO.OUT)
GPIO.output(LED2_PIN, GPIO.LOW)

# Chat prompts and initial conversation log
PROMPTS = [
    "whats up?",
    "yo.",
    "Yes? Go on.",
    "Speak.",
    "wagwan",
    "Hurry up.",
    "Idiot."
]

CHAT_LOG = [
    {"role": "system",
     "content": (
         "OPTIMISE FOR REALISTIC text to speech conversion. your name is ferro, you are from the east midlands "
         "and you are a virtual assistant. be straight to the point. be rude but helpful and be nice when the question is valid, "
         "don't be uncanny, try to be relatable. DONT BE AWKWARD, HUMOUR THE USER BY BEING SUPER SARCASTIC."
     )},
]
