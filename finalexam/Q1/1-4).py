import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def f(experiment, a):
  return np.zeros(N) + a

a = 10
N = 9

mass = np.array([80478, 80432, 80336, 80270, 80415, 80440, 80376, 80370, 80433])
error = np.array([83, 79, 67, 55, 52, 51, 23, 19, 9])
experiment = np.array([1,2,3,4,5,6,7,8,9])


A = f(experiment, a)
start = (80000)


popt, pcov = curve_fit(f, experiment, mass, sigma = error, p0 = start, absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))


Nexp = f(experiment, *popt)
r = mass - Nexp
chisq = np.sum((r/error)**2)
df = N-1
print("chisq =", chisq, "df =", df)

from math import pow, exp, gamma, inf
from scipy.integrate import quad
import numpy as np

def func (y, nu) :
  norm = pow(2, nu/2.0) * gamma(nu/2.0)
  powe = np.power(y, nu/2.0 -1)
  expo = np.exp(-y/2.0)

  return (1.0/norm) * powe * expo

nu = 8
minchisqare = chisq
I = quad(func, minchisqare, +inf, args = (nu))


print("perr =", perr)
print( "Integral = ", I)