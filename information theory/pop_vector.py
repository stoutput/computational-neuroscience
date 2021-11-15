import pickle
import numpy as np
import math

def cart2pol(x, y=None):
    if (y is None):
        y = x[1]
        x = x[0]
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return (rho, phi)

# Calculates and outputs the direction angle of the population stimulus vector
# given 4 reponse vectors and their corresponding basis vectors

with open('pop_coding.pickle', 'rb') as f:
    vectors = pickle.load(f)

with open('tuning.pickle', 'rb') as f:
    neurons = pickle.load(f)

# Pop. vector is given by the sum from a=1 to 4 of ((r - r0)/rmax) * Ca
# Where Ca is the preferred-direction (basis) vector that defines the selectivity of the neuron

stim = neurons.pop('stim')
rmax = dict()
v_total = np.zeros(2)

# First, calculate rmax from tuning data for each neuron
for neuron, samples in neurons.items():
    rmax[neuron[-1]] = np.max(np.mean(samples, axis=0, dtype=np.float64))

# Next, sum together each neuron's population vector to get v_total
for vector, firingRates in vectors.items():
    if ('r' in vector):
        i = vector[-1]
        r = np.mean(firingRates)
        v_total += (r/rmax[i]) * vectors['c' + i] 

# Now, convert certesian coordinates to polar
rho, phi = cart2pol(v_total)

# Lastly, convert rad to deg and normalize to coordinate system
angle = (-math.degrees(phi) + 90) % 360

print('Angle of stimulus population vector: ' + str(round(angle)) + '°')