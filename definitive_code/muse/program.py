"""
BAGNIS GABRIELE
PCTO project of ITIS MARIO DELPOZZO CUNEO
"""

import numpy as np 
import pandas as pd
from pylsl import StreamInlet, resolve_byprop
import time, utils, csv, winsound
import login_user as user
from sklearn.model_selection import train_test_split 
from sklearn.neural_network import MLPClassifier

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

def execute(eeg_buffer, filter_state, n_win_test, band_buffer, fileCSV):
    data = pd.read_csv(fileCSV) 
    x = data[['delta','theta','alpha','beta']] #INPUT
    y = data['mano']
    print("Numero di campioni totali: ",x.shape[0])
    model = MLPClassifier(hidden_layer_sizes=(100,100), random_state=1, max_iter=300)
    model.fit(x,y)
    while (True):
        sensor=readData(eeg_buffer, filter_state, n_win_test, band_buffer)
        print(model.predict([sensor]))
    


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

    """ USE """
    nome = user.login()
    print("UTENTE SELEZIONATO: " + nome)
    fileCSV = "utenti\\" + nome + ".csv"
    execute(eeg_buffer, filter_state, n_win_test, band_buffer, fileCSV)
    

