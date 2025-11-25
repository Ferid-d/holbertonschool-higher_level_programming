#!/usr/bin/python3
"""Module for write_file function."""


def write_file(filename="", text=""):
    """
    Write a string to a UTF-8 text file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
