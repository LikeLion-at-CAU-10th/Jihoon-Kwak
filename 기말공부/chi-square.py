from tracemalloc import start
from unittest import findTestCases
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def f(mass, a):
  return np.zeros(N) + a

a = 10
N = 4

counts = np.array([7, 9, 12, 10])
mass = np.array([0.5, 1.5, 2.5, 3.5])
error = np.sqrt(counts)

A = f(mass, a)

start = (1)
popt, pcov = curve_fit(f, mass, counts, sigma = error, p0 = start, absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))
print(perr)


Nexp = f(mass, *popt)
r = counts - Nexp
chisq = np.sum((r/error)**2)
df = N-1
print("chisq =", chisq, "df =", df)

plt.errorbar(mass, counts, yerr=error, fmt = 'o')
plt.plot(mass, Nexp)
plt.show()