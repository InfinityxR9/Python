# plotting graphs
import numpy as np
import math as mat
import matplotlib.pyplot as plt

x = np.arange(0, 1, mat.pi)
y = np.sin(x)

plt.plot(x,y)
plt.show()

