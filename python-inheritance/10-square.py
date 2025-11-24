#!/usr/bin/python3
"""
Defines class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize square with a validated size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
