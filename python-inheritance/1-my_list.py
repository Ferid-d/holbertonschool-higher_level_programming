#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list.

>>> my_list = MyList()
>>> my_list.append(1)
>>> my_list.append(2)
>>> my_list.print_sorted()
[1, 2]
"""

class MyList(list):
    """Represents a list with a method to print it sorted."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying it."""
        print(sorted(self))
