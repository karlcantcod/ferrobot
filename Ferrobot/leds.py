





# This module handles LED control for the virtual assistant.
# It defines functions to create visual effects, such as fading LEDs in and out,
# which can be used to indicate processing or listening status.
# The module leverages the Raspberry Pi GPIO library.







# leds.py
import time
import threading
import RPi.GPIO as GPIO
from config import LED1_PIN, LED2_PIN

def fade_leds(stop_event):
    """
    Fades two LEDs in and out until the stop_event is set.
    """
    pwm1 = GPIO.PWM(LED1_PIN, 200)
    pwm2 = GPIO.PWM(LED2_PIN, 200)

    stop_event.clear()

    while not stop_event.is_set():
        pwm1.start(0)
        pwm2.start(0)
        for dc in range(0, 101, 5):
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(dc)
            time.sleep(0.05)
        time.sleep(0.75)
        for dc in range(100, -1, -5):
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(dc)
            time.sleep(0.05)
        time.sleep(0.75)
