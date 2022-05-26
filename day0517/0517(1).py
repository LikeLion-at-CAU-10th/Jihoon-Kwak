from tkinter import Y
import numpy as np
from math import pow, gamma, inf
import matplotlib.pyplot as plt
from scipy.integrate import quad

def func (nu, y) :
  norm = pow(2, nu/2.0) * gamma(nu/2.0) # denominator of normalization
  powe = np.power(y, nu/2.0 -1) # power function part
  expo = np.exp(-y/2.0) # exponential part

  return (1.0/norm) * powe * expo

# a function
nu = 3 # number of degrees of freedom

#numerical integral
# minchisqare = 1.41
# I = quad(func, minchisqare, +inf, args = (nu))

# print( "Integral = ", I)

y = np.linspace(0, 10, 100) # 0 to 10 by 0.1 increment 
f_y = func(nu, y) # afuncton that has 1(=NDF) and y(=chisquare)

# print ("X-axis values: ", y)
# print ("Y-axis values: ", f_y)

#drawing the function
plt.plot (y, f_y, "C4", )

plt.grid()
plt.show()