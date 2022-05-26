# 미분방정식을 푸는 방법
# first order미분방정식

import numpy as np
import matplotlib.pyplot as plt

# variables
m = 2.0
k = 2.0

# x-axis
delta_t = 0.01
time = np.arange(0.0, 40.0, delta_t)

# initial condition
x0, v0 = 1.0, 0.0

# states
x,v = x0, v0

# result list
Y = []

# time-steps
for t in time :
  v = v + delta_t * (-k/m)*x
  x = x + delta_t * v
  Y.append(x)

#plot the result
plt.grid(True)
plt.plot(time,Y,'r')
plt.show()