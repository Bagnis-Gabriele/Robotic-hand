from pyemotiv import Epoc
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np

time_passed = 0.0

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
epoc = Epoc()
af3=[]
f7=[]
t=[]

def animate(i, t, af3, f7):

    global time_passed

    data = epoc.get_raw()

    # Add x and y to lists
    af3.append(np.average(data[0]))
    f7.append(np.average(data[1]))
    t.append(time_passed)

    # Limit x and y lists to 20 items
    af3 = af3[-20:]
    f7 = f7[-20:]
    t = t[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(t, af3)
    ax.plot(t, f7)

    # Format plot
    plt.subplots_adjust(bottom=0.30)
    plt.title('sensor')
    plt.ylabel('af3')
    plt.xlabel('time')

    time_passed += 1./2048.

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(t, af3, f7))
plt.show()
