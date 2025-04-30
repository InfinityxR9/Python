import numpy as np
import matplotlib.pyplot as plt

# Generate x values
start = -2 * np.pi
end = 2 * np.pi
step = 0.000001
x_values = np.arange(start, end, step)

# Compute y values using the function y = tan(x)
y_values = np.tan(x_values)

# Create the plot
plt.plot(x_values, y_values, label='y = tan(x)')

# Set y-axis limits to avoid extremely large values due to vertical asymptotes
plt.ylim(-10, 10)

# Add labels and title
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Plot of y = tan(x)')

# Add horizontal and vertical lines for reference
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline((np.pi)/2, color='red', linewidth=1, linestyle='--')

# Show legend
plt.legend()

# Display the plot
plt.show()
