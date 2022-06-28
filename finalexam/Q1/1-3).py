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

counts = mass/error * mass/error
print(counts)

A = f(experiment, a)
start = (80000)


popt, pcov = curve_fit(f, experiment, mass, sigma = error, p0 = start, absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))


Nexp = f(experiment, *popt)
r = mass - Nexp
chisq = np.sum((r/error)**2)
df = N-1
print("chisq =", chisq, "df =", df)

plt.errorbar(experiment, mass, yerr=error, fmt = 'o')
plt.plot(experiment, Nexp)
plt.show()