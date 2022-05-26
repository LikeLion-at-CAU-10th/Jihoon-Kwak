import numpy as np
import matplotlib.pyplot as plt

Fdata = np.array([2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0])
Ldata = np.array([15.0, 32.0, 49.0, 64.0, 79.0, 98.0, 112.0, 126.0, 149.0, 175.0, 190.0])
Ldata = Ldata/1000

plt.figure()
plt.axis([0, 25, 0, 0.2])
plt.plot(Fdata, Ldata, "ro")
plt.grid()
plt.show()