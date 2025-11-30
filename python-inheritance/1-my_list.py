#!/usr/bin/python3
"""
Module that defines the MyList class.
"""


class MyList(list):
    """Custom list class that can print a sorted version of itself."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))

