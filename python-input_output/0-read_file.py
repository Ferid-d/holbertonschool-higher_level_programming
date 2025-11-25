#!/usr/bin/python3
"""Module for read_file function."""

def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
