import numpy as np
import matplotlib.pyplot as plt

t1 = np.arange(-1,1, 0.5)
y1 = np.exp(t1)

t2 = np.arange(-1,1, 0.25)
y2 = np.exp(t2)

t3 = np.arange(-1,1, 0.1)
y3 = np.exp(t3)

plt.figure()
plt.subplot(131)
plt.plot(t1,y1)

plt.subplot(132)
plt.plot(t2,y2)

plt.subplot(133)
plt.plot(t3,y3)

plt.show()