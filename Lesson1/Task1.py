import numpy as np
import matplotlib.pyplot as plt

k1 = 1
k2 = 2
x = np.linspace(-5, 5, 100)
y1 = np.cos(k1 * x)
y2 = np.cos(k2 * x)
plt.plot(x, y1)
plt.plot(x, y2)

plt.show()
