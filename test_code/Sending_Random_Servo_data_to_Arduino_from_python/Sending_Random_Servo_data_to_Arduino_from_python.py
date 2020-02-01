import sys, time, math, serial
from pynput.keyboard import Key, Listener
from random import randrange

ARDUINO_PORT_NAME='COM9'
FREQ_COMMANDS = 0.05
arduino = serial.Serial(ARDUINO_PORT_NAME ,9600)
timeCommand=0.0

def on_press(key):
    global timeCommand
    if time.clock() - timeCommand > FREQ_COMMANDS:
        stringa= str(randrange(2)) + str(randrange(8)) + str(randrange(10)) + str(randrange(2)) + str(randrange(8)) + str(randrange(10)) + str(randrange(2)) + str(randrange(8)) + str(randrange(10)) + str(randrange(2)) + str(randrange(8)) + str(randrange(10)) + str(randrange(2)) + str(randrange(8)) + str(randrange(10))
        arduino.write(stringa)
        print stringa
        print "Arduino:" + arduino.read()

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

with Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()

