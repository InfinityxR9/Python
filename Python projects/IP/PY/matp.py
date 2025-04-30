import numpy as np
import matplotlib.pyplot as plt

# Generate x values
start = -4*np.pi
end = 4*np.pi
step = 0.1
x = np.arange(start, end, step)

# Compute y values using the function y = 3x
y_values = np.tan(x)
plt.ylim(-5, 5)

# Create the plot
plt.plot(x, y_values, label='y = tan x')
# plt.plot(x, y_values)

# Add labels and title
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Plot of y = tan x')

# Show legend
plt.legend()
plt.grid()

# Display the plot
plt.show()
