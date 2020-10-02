import RPi.GPIO as GPIO
import time
import sys
import datetime

import pygame.mixer

Sw_pin = 14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def playMusic(): 
    pygame.mixer.init()
    pygame.mixer.music.load("Familymart_music.mp3")
    pygame.mixer.music.play(1)
    time.sleep(9)
    pygame.mixer.music.stop()





while True:
    try:
        detects_current = GPIO.input(Sw_pin)
        print(detects_current)
        
        # Door Open
        if detects_current == 0:
            print(detects_current)
            playMusic()
        
        # Door Not Open
        elif detects_current == 1:
            print(detects_current)
        
            #print('Now Time: {0}, {1}'.format(datetime.datetime.now(), detects_current))
        time.sleep(1)
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()