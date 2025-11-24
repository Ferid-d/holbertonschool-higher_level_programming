#!/usr/bin/python3
"""Defines inherits_from function."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    Args:
        obj: object to check.
        a_class: class to compare.

    Returns:
        True if obj is instance of a subclass of a_class
        (directly or indirectly), otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
