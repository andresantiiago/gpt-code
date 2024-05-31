# Create a black sky in 4k ultrawide

import matplotlib.pyplot as plt
import numpy as np

# Define the size of the image
width = 5120  # 4K UltraWide resolution width
height = 1440  # 4K UltraWide resolution height

# Create a black background
background = np.zeros((height, width, 3), dtype=np.uint8)

# Generate random stars
num_stars = 3000  # Number of stars
x_coords = np.random.randint(0, width, num_stars)
y_coords = np.random.randint(0, height, num_stars)
brightness = np.random.randint(150, 256, num_stars)  # Brightness of stars

num_stars2 = 300  # Number of stars
x_coords2 = np.random.randint(0, width, num_stars2)
y_coords2 = np.random.randint(0, height, num_stars2)
brightness2 = np.random.randint(300, 512, num_stars2)  # Brightness of stars

num_stars3 = 100  # Number of stars
x_coords3 = np.random.randint(0, width, num_stars3)
y_coords3 = np.random.randint(0, height, num_stars3)
brightness3 = np.random.randint(1024, 2048, num_stars3)  # Brightness of stars

# Adjust the size of the stars
min_star_size = 1  # Minimum size of each star
max_star_size = 4  # Maximum size of each star

# Function to draw a star with Gaussian brightness
def draw_star(x, y, b, size):
    sigma = size / 2.0
    for i in range(-size*2, size*2 + 1):
        for j in range(-size*2, size*2 + 1):
            if 0 <= y + j < height and 0 <= x + i < width:
                distance = np.sqrt(i**2 + j**2)
                intensity = b * np.exp(-distance**2 / (2 * sigma**2))
                background[y + j, x + i] = np.clip(background[y + j, x + i] + intensity, 0, 255)

# Plot the stars on the background
for x, y, b in zip(x_coords, y_coords, brightness):
    size = np.random.randint(min_star_size, max_star_size)
    draw_star(x, y, b, size)

for x, y, b in zip(x_coords2, y_coords2, brightness2):
    size = np.random.randint(min_star_size, max_star_size)
    draw_star(x, y, b, size)

for x, y, b in zip(x_coords3, y_coords3, brightness3):
    size = np.random.randint(min_star_size, max_star_size)
    draw_star(x, y, b, size)

# Save the image
plt.imsave('black_star_sky_4k_ultrawide_realistic_stars.png', background)
