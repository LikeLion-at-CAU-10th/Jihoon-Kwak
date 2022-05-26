# RK-4의 새로운 계산법2 이건 좀 존나 어려운듯.. 새로운 함수를 정의해서 가는 방법 근데 size가 커지면 좀 유리하다는 생각은 들거같긴 함.

import numpy as np
from numpy.linalg import inv
from math import *
import matplotlib.pyplot as plt

def ZZ (ttt, yyy) :
  F[0] = F0 *np.cos( omega * ttt)
  return inv(A).dot(F - B.dot(yyy))


def RK4 (tt, yy, dt):
  # F[0] = F0 * np.cos( omega * t)
  k1 = ZZ(tt,yy)

  # F[0] = F0 * np.cos( omega * (t + 0.5 * delta_t))
  k2 = ZZ(tt + 0.5*dt, yy + 0.5*dt * k1)

  #F[0] = F0 * np.cos( omega * (t + 0.5 * delta_t))
  k3 = ZZ(tt + 0.5*dt, yy + 0.5*dt * k2)

  #F[0] = F0 * np.cos( omega * (t + delta_t))
  k4 = ZZ(tt + 0.5*dt, yy + 0.5*dt * k3)

  return 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4
  # return k1 #RK-1

m = 1.0
k = 1.0

omega = sqrt(k/m)

c = 0.2
F0 = 0.0

delta_t = 0.01
time = np.arange(0, 50, delta_t)

x0 = 1.0
v0 = 0.0

y = np.array( [v0 , x0] )

A = np.array( [ [m  , 0.0] ,[ 0.0 , 1.0]  ])
B = np.array( [ [c  , k  ] ,[-1.0 , 0.0]  ])

F = np.array( [ 0.0, 0.0])

VV = []
XX = []

# inverse_A = inv(A) 로 한뒤 밑에서 계산하면 큰 matrix를 계산할 때 특히 유리하다.

for t in time:
  # G = k1/6.0 + 2*k2/6.0 + 2*k3/6.0 + k4/6.0

  y = y + delta_t * RK4 (t, y, delta_t)

  VV.append (y[0])
  XX.append (y[1])
# 위에 있는 2줄이 의미하는것을 파악할 필요가 있음

plt.plot(time, XX)
plt.show()