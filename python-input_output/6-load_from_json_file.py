#!/usr/bin/python3
"""Module for load_from_json_file function."""

import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
