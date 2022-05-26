import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-4,4,0.01)
y = 1 + np.cos(t)*np.cos(t)

plt.figure()
plt.plot(t, y,"g") # plot funtion 3rd argu is option color of line
plt.show()