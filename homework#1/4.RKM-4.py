import numpy as np
from numpy.linalg import inv
from math import *
import matplotlib.pyplot as plt

m = 2.0
k = 2.0

omega = sqrt(k/m)

c = 0.0
F0 = 0.0

delta_t = 0.01
time = np.arange(0, 40, delta_t)

x0 = 1.0
v0 = 0.0

y = np.array( [v0 , x0] )

A = np.array( [ [m  , 0.0] ,[ 0.0 , 1.0]  ])
B = np.array( [ [c  , k  ] ,[-1.0 , 0.0]  ])

F = np.array( [ 0.0, 0.0])

YY = []
VV = []

for t in time:
  k1 = inv(A).dot(F - B.dot(y))
  k2 = inv(A).dot(F - B.dot(y+0.5*delta_t*k1))
  k3 = inv(A).dot(F - B.dot(y+0.5*delta_t*k2))
  k4 = inv(A).dot(F - B.dot(y+1.0*delta_t*k3))

  G = k1/6.0 + 2*k2/6.0 + 2*k3/6.0 + k4/6.0

  y = y + delta_t * G

  YY.append (y[1])
  VV.append (y[0])

plt.plot(time, YY)
plt.show()