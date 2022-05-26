import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

m = 1
k = 1
omega = sqrt(k/m)

x0 = 1.0
v0 = 0.0

t = np.linspace(0,20,100)
x_t = x0 * np.cos(omega * t) + v0/omega * np.sin(omega * t)

plt.grid(True)
plt.plot(t, x_t, 'r')
plt.show()