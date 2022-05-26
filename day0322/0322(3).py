from re import M
import numpy as np
import matplotlib.pyplot as plt
from math import *

k = 5.0
m = 1.0
c = 1.0

gamma = 0.5*c/m
omega = sqrt(k/m)

omega_d = sqrt(omega**2 - gamma**2)

x0 = 1.0
v0 = 0.0

phi0 = pi/2.
B_d = sqrt(x0**2 + v0**2 / omega**2)

t = np.linspace(0, 20, 1000)

x_t_under = np.exp(-gamma * t) * B_d * np.sin(omega_d * t + phi0)

x_t_decay_plus = B_d * np.exp(-gamma * t)
x_t_dacay_minus = -1.0 * B_d * np.exp