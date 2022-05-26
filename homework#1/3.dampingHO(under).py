import numpy as np
import matplotlib.pyplot as plt
from math import *

k = 5.0
m = 1.0
c = 1.0

gamma = 0.5*c/m
omega = sqrt(k/m)

omega_d = sqrt(omega*omega - gamma*gamma)

x0 = 1.0
v0 = 0.0

phi0 = pi/2.
A_1  = sqrt(x0*x0 + v0*v0 /omega*omega)

t = np.linspace(0, 20, 1000)

x_t_under = np.exp(-gamma * t) * A_1 * np.sin(omega_d* t + phi0)

x_t_decay_plus  =  A_1 * np.exp(-gamma * t)
x_t_decay_minus =  -1.0* A_1 * np.exp(-gamma * t)

plt.grid(True)
plt.plot(t, x_t_under,'r')
plt.show()