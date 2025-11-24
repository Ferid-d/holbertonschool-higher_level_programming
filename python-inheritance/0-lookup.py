#!/usr/bin/python3
"""Module that defines a lookup function.

It returns all attributes and methods of an object.
"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return dir(obj)
