from os import times_result
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from math import *

m = 2.0
k = 2.0
c = 0.0
F0 = 0.0

delta_t = 0.01
time = np.arange(0, 40, delta_t)

x0 = 1.0
v0 = 0.0

y = np.array([1.0, 0.0])
A = np.array([[m, 0.0], [0.0, 1.0]])
B = np.array([[c, k], [-1.0, 0.0]])
F = np.array([0.0, 0.0])

VV = []
YY = []

for t in time :
  y = y + delta_t * inv(A).dot(F - B.dot(y))
  VV.append(y[0])
  YY.append(y[1])

plt.plot(time, VV)
plt.show()