from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pickle
from compute_sta import compute_sta


FILENAME = 'c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

stim = data['stim']
rho = data['rho']

sampling_rate = 500 # In hz
window = 300 # in ms

sampling_period = 1000 / sampling_rate # in ms
num_timesteps = window / sampling_period

sta = compute_sta(stim, rho, num_timesteps)

time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.show()