import numpy as np 
from pylsl import StreamInlet, resolve_byprop
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time, utils, csv, winsound

class Band:
    Delta = 0
    Theta = 1
    Alpha = 2
    Beta = 3

BUFFER_LENGTH = 5
EPOCH_LENGTH = 1
OVERLAP_LENGTH = 0.8
SHIFT_LENGTH = EPOCH_LENGTH - OVERLAP_LENGTH
INDEX_CHANNEL = [0]

def readData(eeg_buffer, filter_state, n_win_test, band_buffer):

    """ ACQUIRE DATA """
    eeg_data, timestamp = inlet.pull_chunk(timeout=1, max_samples=int(SHIFT_LENGTH * fs))
    ch_data = np.array(eeg_data)[:, INDEX_CHANNEL]
    eeg_buffer, filter_state = utils.update_buffer(eeg_buffer, ch_data, notch=True, filter_state=filter_state)

    """ COMPUTE BAND POWERS """
    data_epoch = utils.get_last_data(eeg_buffer, EPOCH_LENGTH * fs)
    band_powers = utils.compute_band_powers(data_epoch, fs)

    return band_powers

def writeValue(sensor,fileCSV,mod):
    fileCSV.writerow([str(sensor[0]),str(sensor[1]),str(sensor[2]),str(sensor[3]),mod])

def bip_start():
    try:
        Beep(5000,1000)
    except: 
        pass

def bip_stop():
    try:
        Beep(10000,3000)
    except: 
        pass

def countdown():
    print("3")
    bip_start()
    time.sleep(1)
    print("2")
    bip_start()
    time.sleep(1)
    print("1")
    bip_start()
    time.sleep(1)

def Training(eeg_buffer, filter_state, n_win_test, band_buffer, fileCSV):

    """ TRAINING """
    print("--------------------------------------")
    print("focus on opening your hand")
    print("--------------------------------------")
    countdown()

    for _ in range(0,100):
        sensor=readData(eeg_buffer, filter_state, n_win_test, band_buffer)
        writeValue(sensor,fileCSV,"O")

    bip_stop()

    print("--------------------------------------")
    print("now, focus on closing your hand")
    print("--------------------------------------")
    countdown()

    for _ in range(0,100):
        sensor=readData(eeg_buffer, filter_state, n_win_test, band_buffer)
        writeValue(sensor,fileCSV,"C")

    bip_stop()


if __name__ == "__main__":

    """ CONNECT TO EEG STREAM """
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

    """ INITIALIZE BUFFERS """
    eeg_buffer = np.zeros((int(fs * BUFFER_LENGTH), 1))
    filter_state = None  # for use with the notch filter
    n_win_test = int(np.floor((BUFFER_LENGTH - EPOCH_LENGTH) / SHIFT_LENGTH + 1))
    band_buffer = np.zeros((n_win_test, 4))

    """ TRAINING """
    with open('data.csv', mode='w') as data_file:
        fileCSV = csv.writer(data_file)
        fileCSV.writerow(['delta','theta','alpha','beta','state'])
        Training(eeg_buffer, filter_state, n_win_test, band_buffer, fileCSV)
    

