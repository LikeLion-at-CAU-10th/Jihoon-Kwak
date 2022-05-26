import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.05)
y0 = x*0.0 + 1 #1 constant
y1 = x*1.0 #x

z = 1 + x

plt.figure()

plt.subplot(311)
plt.grid(True)
plt.plot(x,y0)

plt.subplot(312)
plt.grid(True)
plt.plot(x,y1)

plt.subplot(313)
plt.grid(True)
plt.plot(x,z)

plt.show()