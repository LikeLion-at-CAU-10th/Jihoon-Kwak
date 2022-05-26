# harminic oscillator
# 행렬의 곱을 이용하여 oscillator의 미분방정식을 완성한다.
# 1st order Runge-Kutta method Python Implementation

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from math import *

# variables
m = 2.0
k = 2.0

c = 0.0 #no damping
F0 = 0.0 #no driving force --> SHO

delta_t = 0.001
time = np.arange(0.0, 40.0, delta_t)

# initial condition
x0 = 1.0
v0 = 0.0

# initial state
y = np.array([v0, x0])

A = np.array([[m,   0.0],
              [0.0, 1.0]])

B = np.array([[c,    k],
              [-1.0, 0.0]])

F = np.array([0.0, 0.0])

# result list
Y = [] # list of positions each time interval

#time-steps aka RK-1 method
for t in time :
  y = y + delta_t * inv(A).dot( F - B.dot(y))
  Y.append(y[1])

  plt.grid(True)
  plt.plot(time,Y)
  plt.show()

  # 지금 오류발생함 이유 찾아봐야함