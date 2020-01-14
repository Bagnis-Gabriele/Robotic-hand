"""
Leap
"""
import Leap, sys, time, math, serial, config
from threading import Thread
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

arduino = serial.Serial(config.ARDUINO_PORT_NAME , config.ARDUINO_SERIAL)
timeCommand=0.0

"""
Lettura di dati dal Lead
"""
class SampleListener(Leap.Listener):
    finger_names = config.FINGER_NAME
    nScan=0
    Fmin={}
    Fmax={}
    for finger in finger_names:
        Fmin[finger]=0
        Fmax[finger]=0

    def init_training(self):
        if self.nScan < (config.N_SCANSIONI_TRAINING*2):

            if self.nScan == 0:
                #start training
                print "------------------------------------\nSTART TRAINING\n------------------------------------"
                #training request for open hand 
                print "\nKeep your hand OPEN over the sensor"
                self.countdown()

            if self.nScan == config.N_SCANSIONI_TRAINING: 
                #training request for close hand
                print "\nKeep your hand CLOSE over the sensor"
                self.countdown()

        if self.nScan == (config.N_SCANSIONI_TRAINING*2):
            #end training
            print "-------------------------------------\nEND TRAINING\n-------------------------------------"
                        
    def countdown(self):
        #waiting
        print "scan in 3 seconds"
        time.sleep(1)
        print "scan in 2 seconds"
        time.sleep(1)
        print "scan in 1 seconds"
        time.sleep(1)

    def end_training(self, position):
        #I check for data
        if position["Thumb"]!=0:

            #data storage for calculating the open hand
            if self.nScan < config.N_SCANSIONI_TRAINING:
                for name in self.finger_names:
                    self.Fmax[name]=self.Fmax[name]+position[name]
            if self.nScan == config.N_SCANSIONI_TRAINING:
                for name in self.finger_names:
                    self.Fmax[name]=self.Fmax[name]/config.N_SCANSIONI_TRAINING

            #data storage for calculating the close hand
            if self.nScan < (config.N_SCANSIONI_TRAINING*2): 
                if self.nScan > config.N_SCANSIONI_TRAINING:
                    for name in self.finger_names:
                        self.Fmin[name]=self.Fmin[name]+position[name]
            if self.nScan == (config.N_SCANSIONI_TRAINING*2):
                for name in self.finger_names:
                    self.Fmin[name]=self.Fmin[name]/config.N_SCANSIONI_TRAINING-1

        else:
            self.nScan=self.nScan-1

    def control_frame(self, frame, position):
        #I check for one hand
        if frame.hands==0:
            print "put your hand"
        else:
            # Get hand
            for hand in frame.hands:
                # Get center hand
                Center= hand.palm_position
                # Get fingers
                for finger in hand.fingers:
                    bone = finger.bone(config.FINGER_TIP)
                    position[self.finger_names[finger.type]]=int(math.sqrt(pow((bone.next_joint[0]-Center[0]),2)+pow((bone.next_joint[1]-Center[1]),2)+pow((bone.next_joint[2]-Center[2]),2)))
        return position
    
    def arduino(self, position):
        ardu={}
        ardustr={}
        for finger in self.finger_names:
            ardu[finger]=0
            ardustr[finger]=0
        
        for name in self.finger_names:
            #Servo motor position calculation
            ardu[name]=int(((position[name]-self.Fmin[name])*config.SERVO_MAX)/(self.Fmax[name]-self.Fmin[name]))
            #data control
            if ardu[name] > config.SERVO_MAX:
                ardu[name]= config.SERVO_MAX
            if ardu[name] < config.SERVO_MIN:
                ardu[name]= config.SERVO_MIN
            #string conversion
            ardustr[name]=str(ardu[name]).zfill(3)
        #import timecommand
        global timeCommand
        #if Arduino is available I send you the data
        if time.clock() - timeCommand > config.FREQ_COMMANDS:
            #I concatenate the various data to obtain a single string
            arduString = str(ardustr["Thumb"])+str(ardustr["Index"])+str(ardustr["Middle"])+str(ardustr["Ring"])+str(ardustr["Pinky"])
            #send data to Arduino
            arduino.write(arduString)
            #wait data from Arduino
            print "arduino:" + arduino.read()
            #I set the sending time on the Arduino clock
            timeCommand = time.clock()
    
    def on_frame(self, controller):
        
        position={}
        for finger in self.finger_names:
            position[finger]=0
        
        if self.nScan <= (config.N_SCANSIONI_TRAINING*2):
            #start training
            self.init_training()

        # Get the most recent frame and report some basic information
        frame = controller.frame()
        position = self.control_frame(frame, position)

        if self.nScan <= (config.N_SCANSIONI_TRAINING*2):
            #end training
            self.end_training(position)

        if self.nScan > (config.N_SCANSIONI_TRAINING*2):
            #send data to arduino
            self.arduino(position)
        
        #print scanned data
        print 'T'+str(position["Thumb"])+'I'+str(position["Index"])+'M'+str(position["Middle"])+'R'+str(position["Ring"])+'P'+str(position["Pinky"])
        
        #increase the number of scans
        self.nScan=self.nScan+1
    

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


#this function is used to convert the program into a library in case you want to use it in that way
if __name__ == "__main__":
    main()
