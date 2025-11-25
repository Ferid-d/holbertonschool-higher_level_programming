#!/usr/bin/python3
"""Module for class_to_json function."""


def class_to_json(obj):
    """
    Return the dictionary description of a class instance
    with only simple data structures (list, dict, str, int, bool).
    """
    return obj.__dict__.copy()
