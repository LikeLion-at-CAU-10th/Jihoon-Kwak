from ast import NamedExpr
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# linear function fitting
# def f(mass, a, b):
#   return np.zeros(4) + a * mass +b

# 2차 function fitting
# def f(mass, a, b, c):
#   return np.zeros(4) + a * mass * mass + b * mass + c

def f(mass, a):
  return np.zeros(4) + a

counts = np.array([7.0, 9.0, 12.0, 10.0]) # data
errors = np.sqrt(counts) # uncertainties of data

mass = np.array([0.5, 1.5, 2.5, 3.5]) # x-axis or time

print("Data=", counts)
print("Error on the data=", errors)
print("X axis = n", mass)

a = 0

# a = 0
# b = 0
# Mu = f(a) # np.zeros(4) + a # model

# a = 0
# b = 0
# c = 0

# start = (1,1,1)

start = (1)

# start = (1,1) #starting position for slope and y-intersec

popt, pcov = curve_fit (f, mass, counts, sigma=errors, p0=start, absolute_sigma=True) #()

print("Result popt= ", popt)
print("Result pcov= ", pcov)

perr = np.sqrt(np.diag(pcov)) #take the squre root ion the 1x1 convariance matrix = variance = error^2

print ("Uncertainty = ",perr)

Nexp = f(mass, *popt) #result function mu = a line mu = 9.147
r = counts - Nexp #numerator in the chisquare function

chisquare = np.sum( (r/errors) * (r/errors) ) # chisquare function at the best fit position
print("Minimum Chisquare = ", chisquare)

plt.errorbar (mass, counts, yerr = errors, fmt='o') # data point drawing
plt.plot(mass, Nexp) # line or model drawing
plt.show()