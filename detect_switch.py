import RPi.GPIO as GPIO
import time
import sys
import datetime
import random
import pygame.mixer
import sqlite3

def setup_database():
    con = sqlite3.connect('labo.db')
    with con:
        con.execute("""
            CREATE TABLE LABO (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                date TEXT
            );
        """)


def addDoorOpenData(cnt, date):
    sql = 'INSERT INTO USER (id, date) values(?,?)'
    data = [
        (cnt, date)
    ]
    with con:
        con.executemany(sql, data)
    # OUTPUT SQL DATA
    with con:
        data = con.execute("SELECT * FROM LABO")
        for row in data:
            print(row)

def setup_raspberry():
    SW_PIN = 14
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Continue Closing Door for 30 min
def playMusic():
    pygame.mixer.init()
    filename = "/home/pi/Desktop/MusicVideo/EDM/1.mp3"
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(1)
    time.sleep(11)
    pygame.mixer.music.stop()

def detect_door():
    close_count = 0
    open_count = 0

    while True:
        try:
            detects_current = GPIO.input(Sw_pin)
            # Close Door == 0
            # Open Door == 1
            CLOSE_DOOR = 0
            OPEN_DOOR = 1

            # CATCH OPEN DOOR
            if detects_current == OPEN_DOOR:
                open_count += 1
                date = str(datetime.datetime.now())
                addDoorOpenData(open_count, date)

            # CATCH CLOSE DOOR
            else:
                close_count += 1

            if close_count == 60*30:
                playMusic()

            time.sleep(1)


        except KeyboardInterrupt:
            GPIO.cleanup()
            sys.exit()



# main メソッド
def main():
    setup_raspberry()
    setup_database()
    detect_door()

if __name__ == "__main__":
    main()