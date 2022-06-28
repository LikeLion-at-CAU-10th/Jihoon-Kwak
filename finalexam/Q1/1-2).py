import numpy as np

mass = np.array([80478, 80432, 80336, 80270, 80415, 80440, 80376, 80370, 80433])
error = np.array([83, 79, 67, 55, 52, 51, 23, 19, 9])

counts = mass/error * mass/error
print(counts)