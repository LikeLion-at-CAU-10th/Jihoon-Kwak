import numpy as np
import matplotlib.pyplot as plt
from math import *

k = 0.1
m = 1.0
c = 1.0

omega = sqrt(k/m)
gamma = 0.5 * c/m
q = sqrt(gamma*gamma - omega*omega)

x0 = 1.0
v0 = 0.0

t = np.arange(0, 100, 1)

A_1 = 0.5 * ( ( 1 + gamma/q ) * x0 + v0/q)
A_2 = 0.5 * ( ( 1 + gamma/q ) * x0 - v0/q)

x_t = A_1 * np.exp(-(gamma - q) * t) + A_2 * np.exp(-1 * (gamma + q) * t)

plt.plot(t, x_t, 'r')
plt.show()