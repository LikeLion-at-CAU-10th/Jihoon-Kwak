import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

k = 0.001 
m = 1.0
# c = 10.0 # Overdamping
c_crit = 2 # critical damping condition -->c^2 = 4mk

omega = sqrt(k/m)
# gamma = 0.5 * c/m
# q = sqrt(gamma*gamma - omega*omega)

#initial comdition
x0 = 1.0
v0 = 0.0

#function
t = np.arange(0,100,1) # 0 to 100second every second

#over damping case
# A_1 = 0.5 * ( (1 + gamma/q)*x0 + v0/q)
# A_2 = 0.5 * ( (1 - gamma/q)*x0 - v0/q)

gamma_crit = 0.5 * c_crit/m
A = gamma_crit * x0 + v0
B = x0

x_t_crit = A * t * np.exp(-gamma_crit * t) + B * np.exp(-gamma_crit * t)

plt.grid(True)
plt.plot(t, x_t_crit, 'r')
plt.show()