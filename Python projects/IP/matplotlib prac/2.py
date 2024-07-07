import matplotlib.pyplot as plt
import numpy as np

xVal = np.arange(0, 1.001, 0.01)
yVal = 2*xVal

# plt.plot(xVal, yVal, marker=".", color="c", markersize = 10)
# plt.plot(xVal, yVal, marker=".", color="c", linewidth=4, linestyle='dashdot')
plt.plot(xVal, yVal, marker=".", color="c")

plt.grid()
plt.yticks(np.arange(0, 2.5, 0.5))
plt.xticks(np.arange(0, 1.25, 0.25))

plt.xlabel("Values of x")
plt.ylabel("Values of y = 2x")

# plt.ylim(0.5, 1)


plt.title("Graph of y = 2x under resticted domain")

plt.show()
