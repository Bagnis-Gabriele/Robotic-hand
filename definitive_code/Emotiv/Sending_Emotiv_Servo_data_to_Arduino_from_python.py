import sys, time, math, serial
from pynput.keyboard import Key, Listener

ARDUINO_PORT_NAME='COM4'
FREQ_COMMANDS = 0.1
arduino = serial.Serial(ARDUINO_PORT_NAME ,9600)
timeCommand=0.0

def on_press(key):
    print str(key)
    if str(key)=="u'o'":
        open()
    if str(key)=="u'c'":
        close()
    
def close():
    print "CLOSE"
    global timeCommand
    if time.clock() - timeCommand > FREQ_COMMANDS:
        arduino.write("000000000000000")
        print "Arduino:" + arduino.read()
        timeCommand = time.clock()

def open():
    print "OPEN"
    global timeCommand
    if time.clock() - timeCommand > FREQ_COMMANDS:
        arduino.write("180180180180180")
        print "Arduino:" + arduino.read()
        timeCommand = time.clock()

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

with Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()

