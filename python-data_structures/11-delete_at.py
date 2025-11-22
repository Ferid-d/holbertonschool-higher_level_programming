#!/usr/bin/python3
"""Module that defines a function to delete an element at a specific
index in a list.
"""


def delete_at(my_list=[], idx=0):
    """Delete the item at a specific index in my_list.
    If idx is out of range or negative, return the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = []
    for i, item in enumerate(my_list):
        if i != idx:
            new_list.append(item)
    my_list[:] = new_list
    return my_list
