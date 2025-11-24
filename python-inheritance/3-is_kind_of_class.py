#!/usr/bin/python3
"""Defines is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclasses.

    Args:
        obj: object to check
        a_class: class to compare

    Returns:
        True if isinstance(obj, a_class), otherwise False
    """
    return isinstance(obj, a_class)
