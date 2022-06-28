import numpy as np
import matplotlib.pyplot as plt

experiment = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
mass = np.array([80478, 80432, 80336, 80270, 80415, 80440, 80376, 80370, 80433])
error = np.array([83, 79, 67, 55, 52, 51, 23, 19, 9])

plt.errorbar(experiment, mass, yerr=error, fmt = 'o')
plt.show()