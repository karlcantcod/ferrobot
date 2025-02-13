# This is the main entry point of the virtual assistant application.
# It ties together all the modules including configuration, chat logic, text-to-speech,
# LED control, wake-word detection, recording, and speech-to-text conversion.
# The main loop waits for a wake word, processes the user's speech, obtains a response
# from ChatGPT, and then both prints and speaks the response.
# It also provides visual feedback using LEDs during processing.


# main.py
import threading
import time
import random
import RPi.GPIO as GPIO

from config import PROMPTS, LED1_PIN, LED2_PIN
from chat import chat_gpt, append_clear_countdown
from tts import voice
from utils import response_printer
from leds import fade_leds
from wake_word import wake_word
from recorder import Recorder, listen, detect_silence
from leopard import init_leopard
from Server.api.flaskApp import assistant_state, app

def main():
    # Start Flask API in a separate thread
    api_thread = threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000), daemon=True)
    api_thread.start()

    count = 0
    clear_thread = None
    leopard_instance = init_leopard()

    while True:
        try:
            if count == 0:
                # Start the conversation-clear countdown on the first loop iteration.
                clear_thread = threading.Thread(target=append_clear_countdown, daemon=True)
                clear_thread.start()
            count += 1

            # Update state for wake word detection
            assistant_state['is_listening'] = False
            assistant_state['is_processing'] = False
            
            # Wait for the wake word
            wake_word()
            assistant_state['is_listening'] = True

            # Respond to wake word with a random prompt
            voice(random.choice(PROMPTS))

            # Start recording and detect when a query is finished
            recorder = Recorder()
            recorder.start()
            listen()
            detect_silence()

            # Process the recorded audio to get a transcript (and words, if needed)
            transcript, words = leopard_instance.process(recorder.stop())
            assistant_state['last_transcript'] = transcript
            assistant_state['is_processing'] = True

            # Start LED fade effect during processing
            fade_event = threading.Event()
            fade_thread = threading.Thread(target=fade_leds, args=(fade_event,))
            fade_thread.start()

            print(transcript)
            # Get ChatGPT’s response
            response_text = chat_gpt(transcript)
            assistant_state['last_response'] = response_text
            print("\nChatGPT's response is:\n")

            # Use threads to speak and print the response concurrently
            voice_thread = threading.Thread(target=voice, args=(response_text,))
            printer_thread = threading.Thread(target=response_printer, args=(response_text,))
            voice_thread.start()
            printer_thread.start()
            voice_thread.join()
            printer_thread.join()

            # Reset processing state
            assistant_state['is_processing'] = False

            # Stop the LED fade effect and turn off LEDs
            fade_event.set()
            GPIO.output(LED1_PIN, GPIO.LOW)
            GPIO.output(LED2_PIN, GPIO.LOW)

        except KeyboardInterrupt:
            print("\nExiting ChatGPT Virtual Assistant")
            leopard_instance.delete()
            break
            
        except Exception as e:
            print(f"An error occurred: {e}")
            assistant_state['is_processing'] = False
            assistant_state['is_listening'] = False
            leopard_instance.delete()
            break

if __name__ == '__main__':
    main()
