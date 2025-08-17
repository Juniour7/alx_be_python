import math

class Shape:
    """
    A base class for geometric shapes.
    """
    def area(self):
        """
        Calculate the area of the shape. This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the area() method")

class Rectangle(Shape):
    """
    A class representing a rectangle, derived from Shape.
    """
    def __init__(self, length: float, width: float):
        """
        Initializes a Rectangle instance with length and width.
        """
        self.length = length
        self.width = width

    def area(self) -> float:
        """
        Overrides the base class method to calculate the area of the rectangle.
        Returns:
            The area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    A class representing a circle, derived from Shape.
    """
    def __init__(self, radius: float):
        """
        Initializes a Circle instance with a radius.
        """
        self.radius = radius

    def area(self) -> float:
        """
        Overrides the base class method to calculate the area of the circle.
        Returns:
            The area of the circle.
        """
        return math.pi * (self.radius ** 2)