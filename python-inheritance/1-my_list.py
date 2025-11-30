#!/usr/bin/python3
"""
this module defines a class MyList that inherits from list.
it demonstrates how to extend built-in types to add custom utility methods.
"""


class MyList(list):
    """
    a custom list class that inherits from the built-in list.
    it includes a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        it prints the list, but sorted (ascending sort).
        does not modify the original list order.
        """
        # it uses the built-in function sorted() which returns a NEW list.
        # it passes 'self' (the current object) to it.
        print(sorted(self))
