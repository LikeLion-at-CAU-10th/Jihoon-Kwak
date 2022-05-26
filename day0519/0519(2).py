#기말고사 대비 코드 공부하기

from calendar import c
from msilib.schema import MsiAssembly
from poplib import POP3_PORT
import numpy as np
import matplotlib.pyplot as plt


#2
# def f(mass, a, b) :
#   return np.zeros(N) + a*mass + b


#3
def f(mass, a, b, c) :
  return np.zeros(N) + a*mass*mass + b*mass + c


# #2
# a = 10 # init. the const. function
# b = 1 # y-intersect
# N = 4


#3
a = 10 # init. the const. function
b = 1 # y-intersect
c = 1
N = 4


counts = np.array([7, 9, 12, 10])
mass = np.array([0.5, 1.5, 2.5, 3.5])
error = np.sqrt(counts)


print("Mass (x)", mass)
print("counts (y)", counts)
print("Error in counts = ", error)


#2
# A = f(mass, a, b)
# print(A)

#3
A = f(mass, a, b, c)
print(A)


start = (10, 1)


from scipy.optimize import curve_fit


popt, pcov = curve_fit (f, mass, counts, sigma=error, p0=start, absolute_sigma=True)
print(popt)
print(pcov)


perr = np.sqrt(np.diag(pcov))
print(perr)
print(*popt)


#2
# Nexp = f(mass, *popt) 
# r = counts - Nexp 
# chisq = np.sum( (r/error) * (r/error) )
# df = N-2
# print("chisq = ", chisq, "df = ", df)


#3
Nexp = f(mass, *popt) 
r = counts - Nexp 
chisq = np.sum( (r/error) * (r/error) )
df = N-3
print("chisq = ", chisq, "df = ", df)


# plt.errorbar (mass, counts, yerr = error, fmt='o')
# plt.plot(mass, Nexp)
# plt.show()