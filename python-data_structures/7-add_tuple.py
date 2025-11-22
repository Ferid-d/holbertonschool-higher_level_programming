#!/usr/bin/python3
"""Module that defines a function to add two tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples element-wise, using 0 for missing elements."""
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a0 + b0, a1 + b1)
