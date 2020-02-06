from pyemotiv import Epoc
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time, config
import numpy as np
import csv

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

nScan=0

epoc = Epoc()

t=[]
sensor={}
for name in config.SENSORNAME:
    sensor[name]=[]

start_time=time.time()

def countdown(self):
    #waiting
    print "scan in 3 seconds"
    time.sleep(1)
    print "scan in 2 seconds"
    time.sleep(1)
    print "scan in 1 seconds"
    time.sleep(1)

def animate(i,t,sensor,data):

    data = epoc.get_raw()

    # Add x and y to lists
    num=0
    for name in config.SENSORNAME:
        sensor[name].append(np.average(data[num]))
        num=num+1
    t.append(((time.time())-start_time))

    # Limit x and y lists to 20 items
    for name in config.SENSORNAME:
        sensor[name]=sensor[name][-config.NDATI:]
    t=t[-config.NDATI:]

    #save file on csv
    if nScan==0 :
        print "___________________________________________"
        print "training"
        print "___________________________________________"
        input("press one key for start...")
        input("press one key and thinking of open one hand...")
        countdown()
    else if nScan == 300:
        input("press one key and thinking of close one hand...")
        countdown()
    else if nScan == 600:
        print "___________________________________________"
        print "END TRAINING"
        print "___________________________________________"

    string=""
    for name in config.SENSORNAME:
        for i in config.NDATI:
            string= string + str(sensor[name][i])
            string= string + ','

    if nScan < 300:
        string= string + '1'
    else if nScan < 600:
        string= string + '0'

    data.writerow(string)

    # Draw x and y lists
    ax.clear()
    for name in config.SENSORNAME:
        ax.plot(t, sensor[name], color=config.COLOR[name])

    nScan=nScan+1

    # Format plot
    plt.title('sensor')
    plt.ylabel('electrode')
    plt.xlabel('time')
    plt.ylim(config.YMIN,config.YMAX)



# Set up plot to call animate() function periodically
def main():
    with open("open.csv", "wb") as data:
        ani = animation.FuncAnimation(fig, animate, fargs=(t,sensor,data), interval=(1), save_count=50)
        plt.show()