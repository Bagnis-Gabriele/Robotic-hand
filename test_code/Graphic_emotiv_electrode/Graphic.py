from pyemotiv import Epoc
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time, config
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

epoc = Epoc()

t=[]
sensor={}
for name in config.SENSORNAME:
    sensor[name]=[]

start_time=time.time()

def animate(i,t,sensor):

    data = epoc.get_raw()

    # Add x and y to lists
    num=0
    for name in config.SENSORNAME:
        sensor[name].append(np.average(data[num]))
        num=num+1
    t.append(((time.time())-start_time))

    # Limit x and y lists to 20 items
    for name in config.SENSORNAME:
        sensor[name]=sensor[name][-40:]
    t=t[-40:]

    # Draw x and y lists
    ax.clear()
    for name in config.SENSORNAME:
        ax.plot(t, sensor[name], color=config.COLOR[name])

    # Format plot
    plt.title('sensor')
    plt.ylabel('electrode')
    plt.xlabel('time')
    plt.ylim(config.YMIN,config.YMAX)


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(t,sensor), interval=(1), save_count=50)
plt.show()