"""
calculation of finger-palm distance
"""
import Leap, sys, time, math, serial, config
from threading import Thread
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

arduino = serial.Serial(config.ARDUINO_PORT_NAME ,9600)
timeCommand=0.0

"""
Lettura di dati dal Lead
"""
class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    nScan=0
    Mtemp = {"Thumb":0,"Index":0,"Middle":0,"Ring":0,"Pinky":0}
    Fmin = {"Thumb":0,"Index":0,"Middle":0,"Ring":0,"Pinky":0}
    Fmax = {"Thumb":0,"Index":0,"Middle":0,"Ring":0,"Pinky":0}
    

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        position={"Thumb":0,"Index":0,"Middle":0,"Ring":0,"Pinky":0}
        ardu={"Thumb":0,"Index":0,"Middle":0,"Ring":0,"Pinky":0}
        ardustr={"Thumb":0,"Index":0,"Middle":0,"Ring":0,"Pinky":0}
        
        #training request for open hand        
        if self.nScan == 0:
            print "------------------------------------\nTRAINING\n------------------------------------"
            print "\nKeep your hand OPEN over the sensor"
            print "scan in 3 seconds"
            time.sleep(1)
            print "scan in 2 seconds"
            time.sleep(1)
            print "scan in 1 seconds"
            time.sleep(1)

        #training request for close hand
        if self.nScan == 5: 
                print "------------------------------------\nTRAINING\n------------------------------------"
                print "\nKeep your hand CLOSE over the sensor"
                print "scan in 3 seconds"
                time.sleep(1)
                print "scan in 2 seconds"
                time.sleep(1)
                print "scan in 1 seconds"
                time.sleep(1)

        # Get hand
        for hand in frame.hands:
            # Get center hand
            Center= hand.palm_position

            # Get fingers
            for finger in hand.fingers:
                bone = finger.bone(3)
                position[self.finger_names[finger.type]]=int(math.sqrt(pow((bone.next_joint[0]-Center[0]),2)+pow((bone.next_joint[1]-Center[1]),2)+pow((bone.next_joint[2]-Center[2]),2)))

        #data storage for calculating the open hand
        if self.nScan < 6:
            if position["Thumb"]!=0:
                for name,_ in self.Mtemp.items():
                    self.Mtemp[name]=self.Mtemp[name]+position[name]
            else:
                self.nScan=self.nScan-1
        if self.nScan == 5:
            for name,_ in self.Mtemp.items():
                self.Fmax[name]=self.Mtemp[name]/6
            for name,_ in self.Mtemp.items():
                self.Mtemp[name]=0

        #data storage for calculating the close hand
        if self.nScan < 11: 
            if self.nScan > 5:
                if position["Thumb"]!=0:
                    for name,_ in self.Mtemp.items():
                        self.Mtemp[name]=self.Mtemp[name]+position[name]
                else:
                    self.nScan=self.nScan-1
        if self.nScan == 10:
            for name,_ in self.Mtemp.items():
                self.Fmin[name]=self.Mtemp[name]/5     

        #communication with Arduino
        if self.nScan > 10:
            for name,_ in position.items():
                ardu[name]=int(((position[name]-self.Fmin[name])*180)/(self.Fmax[name]-self.Fmin[name]))
                if ardu[name] > 180:
                    ardu[name]= 180
                if ardu[name] < 0:
                    ardu[name]= 0
                if ardu[name] < 100:
                    if ardu[name] < 10:
                        ardustr[name]="00"+str(ardu[name])
                    else:
                        ardustr[name]="0"+str(ardu[name])
                else:
                    ardustr[name]=ardu[name]
            global timeCommand
            if time.clock() - timeCommand > config.FREQ_COMMANDS:
                arduString = str(ardustr["Thumb"])+str(ardustr["Index"])+str(ardustr["Middle"])+str(ardustr["Ring"])+str(ardustr["Pinky"])
                arduino.write(arduString)
                print arduString
                print "numero 1:" + arduino.read() + arduino.read() + arduino.read()
                print "numero 2:" + arduino.read() + arduino.read() + arduino.read()
                print "numero 3:" + arduino.read() + arduino.read() + arduino.read()
                print "numero 4:" + arduino.read() + arduino.read() + arduino.read()
                print "numero 5:" + arduino.read() + arduino.read() + arduino.read()
                timeCommand = time.clock()
        else:
            print 'T'+str(position["Thumb"])+'I'+str(position["Index"])+'M'+str(position["Middle"])+'R'+str(position["Ring"])+'P'+str(position["Pinky"])
        
        self.nScan=self.nScan+1
        time.sleep(1)

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
