#!/usr/bin/python3
"""Defines a Rectangle class with instance counting, print symbol, area,
perimeter, recreatable representation, deletion message, and comparison."""


class Rectangle:
    """Represents a rectangle with width and height."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a printable string of the rectangle using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Returns a string to recreate a new instance with eval()."""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance is deleted and updates count."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the bigger area or rect_1 if equal."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
