import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def gaus(x, *p):
  A, mu, sigma = p
  return A*np.exp(-(x-mu)**2 / (2.*sigma**2))

scores = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
nums = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,10,13,11,17,14,15,5,2,2,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
error = np.sqrt(nums)

A = (gaus, 10)


start = (15, 20, 2.5)


popt, pcov = curve_fit(gaus, scores, nums, p0 = start, absolute_sigma=True)
print(popt)
print(pcov)

perr = np.sqrt(np.diag(pcov))
print(perr)
print(*popt)


Nexp = gaus(scores, *popt)
r = nums - Nexp

plt.errorbar(scores, nums, yerr=error, fmt = 'o')
plt.plot(scores, Nexp)
plt.show()