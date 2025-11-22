#!/usr/bin/python3
"""Module that defines no_c function."""


def no_c(my_string):
    """Return a copy of my_string with all 'c' and 'C' removed."""
    new_string = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_string += ch
    return new_string
