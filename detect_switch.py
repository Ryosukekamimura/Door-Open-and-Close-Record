import RPi.GPIO as GPIO
import time
import sys
import datetime
import random
import requests

import pygame.mixer

Sw_pin = 14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def random_number():
    random_num = random.randrange(1, 9)
    return random_num

def playMusic(number):
    pygame.mixer.init()
    filename = "/home/pi/Desktop/MusicVideo/EDM" + str(number) + ".mp3"
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(1)
    time.sleep(11)
    pygame.mixer.music.stop()


def callback():
    response = requests.get("http://192.168.0.236:8000/stop")

prev = 0
two_times_before = 1



while True:
    try:
        detects_current = GPIO.input(Sw_pin)
        # Close Door == 0
        # Open Door == 1
        print(detects_current)
        if prev != detects_current:
            try:
                callback()
            except:
                print("Can't send to MacBookPro")
            playMusic(random_number())
        prev = detects_current
        time.sleep(1)
        
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
