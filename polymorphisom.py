class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"The area of the circle is {3.14159 * self.radius * self.radius}"

# Create instances of different shapes
# shape1 = Shape()  # Uncommenting this will raise an AttributeError when calling area()
circle1 = Circle(5)

# Calculating the area of a circle
print(circle1.area())  # Output: The area of the circle is 78.53975
