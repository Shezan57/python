import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure
fig, ax = plt.subplots()

# Set the aspect of the plot to be equal
ax.set_aspect('equal')

# Add a rectangle
# Rectangle(xy, width, height)
rect = patches.Rectangle((0.1, 0.1), 0.6, 0.4, edgecolor='blue', facecolor='none')
ax.add_patch(rect)

# Add a circle
# Circle(xy, radius)
circ = patches.Circle((0.5, 0.5), 0.2, edgecolor='red', facecolor='none')
ax.add_patch(circ)

# Add a polygon (triangle in this case)
# Polygon(xy, closed=True)
triangle = patches.Polygon([[0.2, 0.8], [0.3, 0.6], [0.4, 0.8]], closed=True, edgecolor='green')
ax.add_patch(triangle)

# Set the limits of the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Display the plot
plt.show()
