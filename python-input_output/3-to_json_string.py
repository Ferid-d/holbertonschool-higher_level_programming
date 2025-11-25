#!/usr/bin/python3
"""Module for to_json_string function."""

import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object as a string.
    """
    return json.dumps(my_obj)
