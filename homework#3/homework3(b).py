# from re import S
import numpy as np
import matplotlib.pyplot as plt

Fdata = np.array([2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0])
Ldata = np.array([15.0, 32.0, 49.0, 64.0, 79.0, 98.0, 112.0, 126.0, 149.0, 175.0, 190.0])
Ldata = Ldata/1000

# brute force fit model : f = ax + b
mini = 9999

for a in range(100, 2000, 1) :
  a = a/100000.

  for b in range (-100, 300, 1) :
    b = b/1000

    s = 0.0
    for i in range (11) :
      x = 2 * (i + 1)
      FF = a * x + b
      s += (Ldata[i] - FF) * (Ldata[i] - FF)
    if (s<mini) :
      mini = s
      print(a, b, 1./a, -b/a, s)

x = np.arange(15, 200, 0.1)
x = x/1000.
f = []

for i in x : 
  f. append(115.47 * i + 0.577)

plt.plot(f, x, 'b-', Fdata, Ldata, 'ro')
plt.grid()
plt.show()