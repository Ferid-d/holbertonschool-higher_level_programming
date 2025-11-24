#!/usr/bin/python3
"""Module that defines MyList class.

>>> my_list = MyList()
>>> my_list.append(1)
>>> my_list.append(4)
>>> my_list.append(2)
>>> my_list.append(3)
>>> my_list.append(5)
>>> my_list.print_sorted()
[1, 2, 3, 4, 5]
"""
class MyList(list):
    """Custom list that can print itself sorted."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying it."""
        print(sorted(self))
