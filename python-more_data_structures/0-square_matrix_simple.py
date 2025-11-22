#!/usr/bin/python3
"""Module that defines a function to compute the square of all integers
in a 2D matrix.
"""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with the square of all values of the input matrix."""
    return [[value ** 2 for value in row] for row in matrix]
