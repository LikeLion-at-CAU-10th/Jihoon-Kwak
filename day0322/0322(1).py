#Harmonic Oscillator-2 Damped Harmonic Oscillators : case1

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

#Overdamping case where spring is weak

#consts & initial conditions
k = 0.001 # spring const. has to be very small
m = 1.0
c = 1.0 # damping constant high value means more resistance

omega = sqrt(k/m)
gamma = 0.5 * c/m

q = sqrt(gamma*gamma - omega*omega)

#initial comdition
x0 = 1.0 # 1m pull from equil.
v0 = 0.0 # did not have initial speed

t = np.arange(0,100,1) # 0 to 100second every second

A_1 = 0.5 * ( (1 + gamma/q)*x0 + v0/q)
A_2 = 0.5 * ( (1 - gamma/q)*x0 - v0/q)

x_t = A_1 * np.exp(-1 * (gamma -q)*t ) + A_2 * np.exp(-1 * (gamma + q)*t)

plt.plot(t, x_t)
plt.show()