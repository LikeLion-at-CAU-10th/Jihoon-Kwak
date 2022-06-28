from math import pow, exp, gamma, inf
from scipy.integrate import quad
import numpy as np

def func (y, nu) :
  norm = pow(2, nu/2.0) * gamma(nu/2.0)
  powe = np.power(y, nu/2.0 -1)
  expo = np.exp(-y/2.0)

  return (1.0/norm) * powe * expo

nu = 3
minchisqare = 1.41
I = quad(func, minchisqare, +inf, args = (nu))

print( "Integral = ", I)

