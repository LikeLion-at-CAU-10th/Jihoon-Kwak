import numpy as np
import matplotlib.pyplot as plt

# variables
m = 2.0
k = 2.0

# x-axis
delta_t = 0.01 #time step
time = np.arange(0, 40, delta_t) #time from 0 to 40 sec. by 4000sample

# initial condition
x0, v0 = 1.0, 0.0

# states
x, v = x0, v0

# result list
X = [] # updated position
V = [] # updated position

# time-steps
for t in time :
  v = v + delta_t * (-k/m)*x
  x = x + delta_t * v
  X.append (x)
  V.append (v)


#plot the results
plt.plot(time, X, time, V, 'r')
plt.show()