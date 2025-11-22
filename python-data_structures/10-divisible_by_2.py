#!/usr/bin/python3
"""Module that defines a function to check if integers in a list
are divisible by 2.
"""


def divisible_by_2(my_list=[]):
    """Return a new list of True/False for each element in my_list,
    depending on whether it is divisible by 2.
    """
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
