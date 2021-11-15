import pickle
import numpy as np
import matplotlib.pyplot as plt

# Outputs a plot of neuronal response tuning curves for 4 neurons
# Given sampling data of each in Hz

plt.title('Neuronal Tuning Curves')
plt.xlabel('Stimulus')
plt.ylabel('Avg. Firing Rate')

with open('tuning.pickle', 'rb') as f:
    neurons = pickle.load(f)

stim = neurons.pop('stim')

for neuron, samples in neurons.items():
    plt.plot(stim, np.mean(samples, axis=0, dtype=np.float64))

plt.show()