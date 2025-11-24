#!/usr/bin/python3
"""
Defines class BaseGeometry based on 6-base_geometry.py
"""


class BaseGeometry:
    """Base class"""

    def area(self):
        """Raises an exception (not implemented)"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
