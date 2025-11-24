#!/usr/bin/python3
"""
Defines class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize square with validated size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the square description for print() and str()"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

    def area(self):
        """Return the area of the square"""
        return self._Rectangle__width * self._Rectangle__height
