#!/usr/bin/python3
"""Module that defines a function to find the biggest integer in a list.
"""


def max_integer(my_list=[]):
    """Return the biggest integer in a list.
    If the list is empty, return None.
    """
    if not my_list:
        return None

    max_val = my_list[0]
    for num in my_list[1:]:
        if num > max_val:
            max_val = num
    return max_val
