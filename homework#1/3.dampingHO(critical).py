import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

k = 0.001 
m = 1.0
c_crit = 2

omega = sqrt(k/m)

x0 = 1.0
v0 = 0.0

t = np.arange(0,100,1)

gamma_crit = 0.5 * c_crit/m
A = gamma_crit * x0 + v0
B = x0

x_t_crit = A * t * np.exp(-gamma_crit * t) + B * np.exp(-gamma_crit * t)

plt.grid(True)
plt.plot(t, x_t_crit, 'r')
plt.show()