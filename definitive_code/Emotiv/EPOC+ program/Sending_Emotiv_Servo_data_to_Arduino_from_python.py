import sys, time, math, serial, config
from pynput.keyboard import Key, Listener

arduino = serial.Serial(config.ARDUINO_PORT_NAME ,config.ARDUINO_SERIAL)
timeCommand=0.0

def on_press(key):
    print str(key)
    if str(key)==config.K_O:
        open()
    if str(key)==config.K_C:
        close()
    
def close():
    print "CLOSE"
    global timeCommand
    if time.clock() - timeCommand > config.FREQ_COMMANDS:
        arduino.write(config.CLOSE)
        print "Arduino:" + arduino.read()
        timeCommand = time.clock()

def open():
    print "OPEN"
    global timeCommand
    if time.clock() - timeCommand > config.FREQ_COMMANDS:
        arduino.write(config.OPEN)
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

