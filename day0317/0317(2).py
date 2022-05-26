import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, atan

m = 1 # mass 1kg
k = 1 # spring const. 1
omega = sqrt(k/m) # freq.

x0 = 10.0 # init. position
v0 = 1.0 # init. velocity

t = np.linspace(0,20,100) # time

x_t = x0 * np.cos(omega * t) +v0/omega * np.sin(omega * t) # solution

# B = sqrt(x0*x0 + v0*v0/omega/omega) # another const
# phi = atan(x0*omega/v0) # phasw

# #solution or the function
# y_t = B * np.sin (omega * t + phi)

# x_t_dot = -x0 * omega * np.sin(omega * t) + v0 * np.cos(omega * t) #velocity

# E = 0.5 * m * x_t_dot * x_t_dot + 0.5 * k * x_t * x_t

# plt.plot(t, x_t, 'r', t, y_t, 'b', t, E, 'g')

plt.plot(t, x_t, 'r')
plt.show()