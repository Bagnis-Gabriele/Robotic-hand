import numpy as np 
from pylsl import StreamInlet, resolve_byprop
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import utils

class Band:
    Delta = 0
    Theta = 1
    Alpha = 2
    Beta = 3

""" EXPERIMENTAL PARAMETERS """

BUFFER_LENGTH = 5
EPOCH_LENGTH = 1
OVERLAP_LENGTH = 0.8
SHIFT_LENGTH = EPOCH_LENGTH - OVERLAP_LENGTH
INDEX_CHANNEL = [0]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
nScan=0
t=[]
sensor={}
sensor['A']=[]
sensor['B']=[]
sensor['G']=[]
sensor['T']=[]
start_time=time.time()

def animate(i, eeg_buffer, filter_state, n_win_test, band_buffer):

    global t, start_time

    """ 3.1 ACQUIRE DATA """
    eeg_data, timestamp = inlet.pull_chunk(timeout=1, max_samples=int(SHIFT_LENGTH * fs))
    ch_data = np.array(eeg_data)[:, INDEX_CHANNEL]
    eeg_buffer, filter_state = utils.update_buffer(eeg_buffer, ch_data, notch=True, filter_state=filter_state)

    """ 3.2 COMPUTE BAND POWERS """
    data_epoch = utils.get_last_data(eeg_buffer, EPOCH_LENGTH * fs)
    band_powers = utils.compute_band_powers(data_epoch, fs)

    # Add x and y to lists
    sensor['A'].append(band_powers[0])
    sensor['B'].append(band_powers[1])
    sensor['G'].append(band_powers[2])
    sensor['T'].append(band_powers[3])
    t.append(((time.time())-start_time))

    # Limit x and y lists to 20 items
    sensor['A']=sensor['A'][-40:]
    sensor['B']=sensor['B'][-40:]
    sensor['G']=sensor['G'][-40:]
    sensor['T']=sensor['T'][-40:]
    t=t[-40:]

    # Draw x and y lists
    ax.clear()
    ax.plot(t, sensor['A'], color="blue")
    ax.plot(t, sensor['B'], color="red")
    ax.plot(t, sensor['G'], color="green")
    ax.plot(t, sensor['T'], color="black")

    # Format plot
    plt.title('sensor')
    plt.ylabel('data')
    plt.xlabel('time')
    plt.ylim(-2,4)


if __name__ == "__main__":

    """ 1. CONNECT TO EEG STREAM """

    # Search and active LSL streams
    print('Looking for an EEG stream...')
    streams = resolve_byprop('type', 'EEG', timeout=2)
    if len(streams) == 0:
        raise RuntimeError('Can\'t find EEG stream.')
    print("Start acquiring data")
    inlet = StreamInlet(streams[0], max_chunklen=12)
    eeg_time_correction = inlet.time_correction()
    info = inlet.info()
    description = info.desc()
    fs = int(info.nominal_srate())

    """ 2. INITIALIZE BUFFERS """
    eeg_buffer = np.zeros((int(fs * BUFFER_LENGTH), 1))
    filter_state = None  # for use with the notch filter
    n_win_test = int(np.floor((BUFFER_LENGTH - EPOCH_LENGTH) / SHIFT_LENGTH + 1))
    band_buffer = np.zeros((n_win_test, 4))

    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig, animate, fargs=(eeg_buffer, filter_state, n_win_test, band_buffer), interval=(1), save_count=50)
    plt.show()
    

