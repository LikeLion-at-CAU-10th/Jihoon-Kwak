import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from math import *

def G (t, y) :
  F[0] = F0*np.cos(omega_res*t)
  return inv_A.dot(F-B.dot(y))

def RK4(t, y, delta_t) :
  k1 = G(t, y)
  k2 = G(t + 0.5*delta_t, y+0.5*delta_t * k1)
  k3 = G(t + 0.5*delta_t, y+0.5*delta_t * k2)
  k4 = G(t + 0.5*delta_t, y+0.5*delta_t * k3)

  return k1/6.0 + k2/3.0 + k3/3.0 + k4/6.0

m = 1.0
k = 1.0
c = 0.05
F0 = 0.9993

omega = sqrt(k/m)

xi = 0.5*c*1 / sqrt(m*k)
omega_res = omega * sqrt(1-2*xi*xi)
print("Xi = ", xi, "W_t = ", omega_res)

delta_t = 0.001
time = np.arange(0, 200, delta_t)

x0 = 1.0
v0 = 0.0

y = np.array([v0, x0])

A = np.array( [ [m, 0.0],
                [0.0, 1.0]])

B = np.array( [ [c, k],
                [-1.0, 0.0]])

F = np.array( [0.0, 0.0] )

XX = []
FF = []

inv_A = inv(A)

for t in time :
  y = y + delta_t * RK4(t, y, delta_t)

  XX.append(y[1])
  FF.append(F[0])

plt.grid(True)
plt.plot(time, XX,'b',time, FF, 'r')
plt.show()