import numpy as np
import matplotlib.pyplot as plt

# Define the size of the image (number of pixels)
width, height = 800, 800

# Set up the limits for the plot
xmin, xmax, ymin, ymax = -2.5, 1.5, -2.0, 2.0

# Maximum number of iterations to check if a point belongs to the Mandelbrot set
max_iter = 100

# Create a 2D array to store the color value of each pixel
mandelbrot_image = np.zeros((height, width))

# Create a grid of complex numbers
for x in range(width):
    for y in range(height):
        # Convert pixel coordinate to a point in the complex plane
        c = complex(x * (xmax - xmin) / width + xmin, y * (ymax - ymin) / height + ymin)
        z = 0.0j
        for i in range(max_iter):
            z = z * z + c
            if abs(z) > 2.0:
                mandelbrot_image[y, x] = i
                break

# Plot the Mandelbrot set using matplotlib
plt.imshow(mandelbrot_image.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
plt.colorbar()
plt.title('Mandelbrot Set')
plt.show()
print("Done")