from math import pow, exp, gamma, inf
from pyparsing import null_debug_action
from scipy.integrate import quad


def func (x, nu) :
  norm = pow(2, nu/2.0) * gamma (nu / 2.0)
  powe = pow(x, nu/2.0-1)
  expo = exp(-x / 2.0)
  return (1.0 / norm) * powe *expo


#nu = 33
# nu = 3
# minichisquare = 1.41
# p_value = 0.703192


# nu = 2
nu = 2
minichisquare = 0.532
# p_value = 0.766439


I = quad(func, minichisquare, +inf, args = (nu))


print ("Integral = ", I)