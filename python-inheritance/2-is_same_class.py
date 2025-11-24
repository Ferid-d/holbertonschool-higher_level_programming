#!/usr/bin/python3
"""Defines is_same_class function."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class.

    Args:
        obj: object to check
        a_class: class to compare

    Returns:
        True if type(obj) is exactly a_class, otherwise False
    """
    return type(obj) is a_class
