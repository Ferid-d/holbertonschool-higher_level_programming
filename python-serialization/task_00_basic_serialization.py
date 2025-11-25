#!/usr/bin/python3
"""Basic serialization module for Python dictionaries using JSON."""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): Dictionary to serialize.
        filename (str): Filename to save the JSON data.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it into a Python dictionary.

    Args:
        filename (str): Filename of the JSON file.

    Returns:
        dict: Deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
