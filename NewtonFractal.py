import numpy as np
import matplotlib.pyplot as plt

print("Working")

# Parameters for the grid and fractal
grid_size = 500  # Resolution of the fractal image
x_range = np.linspace(-1.5, 1.5, grid_size)  # x-axis range
y_range = np.linspace(-1.5, 1.5, grid_size)  # y-axis range

# Initialize the complex plane grid
Re, Im = np.meshgrid(x_range, y_range)
z = Re + 1j * Im
#z = complex(Re, Im)


# Define the roots of the equation z^3 - 1 = 0
roots = np.array([1, -0.5 + np.sqrt(3)/2 * 1j, -0.5 - np.sqrt(3)/2 * 1j])

# Tolerance and maximum iterations
tolerance = 1e-6
max_iterations = 50

# Initialize an array to store the fractal result
fractal_image = np.zeros(z.shape, dtype=int)

# Newton's method iteration
for k in range(max_iterations):
    # Update z using Newton's method for z^3 - 1 = 0
    z = z - (z**3 - 1) / (3 * z**2)
    
    # Check convergence to each root and assign colors
    for i, root in enumerate(roots):
        converged = np.abs(z - root) < tolerance
        fractal_image[converged] = i + 1  # Assign different color index for each root

# Plot the fractal
plt.figure(figsize=(8, 8))
plt.imshow(fractal_image, extent=(-1.5, 1.5, -1.5, 1.5), cmap="viridis")
plt.colorbar(ticks=[1, 2, 3], label="Root Convergence")
plt.title("Newton Fractal for $z^3 - 1 = 0$")
# Save the plot as an image
plt.savefig("newton_fractal.png")
# Optionally show the plot (in case the environment supports it)
plt.show()
print("Done")