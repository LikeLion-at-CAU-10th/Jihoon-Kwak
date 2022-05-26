# import numpy as np
# import matplotlib.pyplot as plt
# from numpy.linalg import inv
# from math import*

# def G (t, y) :
#   F[0] = -g * y[1]
#   return inv_L.dot(F)


# def RK4 (t, y, delta_t):
#   k1 = G(t,y)
#   k2 = G(t + 0.5*delta_t, y + 0.5*delta_t * k1)
#   k3 = G(t + 0.5*delta_t, y + 0.5*delta_t * k2)
#   k4 = G(t + 0.5*delta_t, y + 0.5*delta_t * k3)
#   return 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4

# g = 9.8
# l = 1.0

# omega = sqrt(g/l)

# delta_t = 0.01
# time = np.arange(0, 5, delta_t)

# theta0 = 10.0 * pi/180
# thetadot0 = 0

# y = np.array([thetadot0, theta0])

# L = np.array()

# # 강의보면서 다시 만들기 