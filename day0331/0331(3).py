# RK-4의 새로운 계산법

import numpy as np
from numpy.linalg import inv
from math import *
import matplotlib.pyplot as plt

def RK4 (t, y, delta_t):
  F[0] = F0 * np.cos( omega * t)
  k1 = inv(A).dot(F - B.dot(y))

  F[0] = F0 * np.cos( omega * (t + 0.5 * delta_t))
  k2 = inv(A).dot(F - B.dot(y+0.5*delta_t*k1))

  F[0] = F0 * np.cos( omega * (t + 0.5 * delta_t))
  k3 = inv(A).dot(F - B.dot(y+0.5*delta_t*k2))

  F[0] = F0 * np.cos( omega * (t + delta_t))
  k4 = inv(A).dot(F - B.dot(y+1.0*delta_t*k3))

  return 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4

m = 2.0
k = 2.0

omega = sqrt(k/m)

c = 0.0
F0 = 0.0

delta_t = 0.01
time = np.arange(0, 200, delta_t)

x0 = 1.0
v0 = 0.0

y = np.array( [v0 , x0] )

A = np.array( [ [m  , 0.0] ,[ 0.0 , 1.0]  ])
B = np.array( [ [c  , k  ] ,[-1.0 , 0.0]  ])

F = np.array( [ 0.0, 0.0])

YY = []
VV = []

# inverse_A = inv(A) 로 한뒤 밑에서 계산하면 큰 matrix를 계산할 때 특히 유리하다.

for t in time:
  # G = k1/6.0 + 2*k2/6.0 + 2*k3/6.0 + k4/6.0

  y = y + delta_t * RK4 (t, y, delta_t)

  YY.append (y[1])
  VV.append (y[0])
# 위에 있는 2줄이 의미하는것을 파악할 필요가 있음

plt.plot(time, YY)
plt.show()