#!/usr/bin/python3
"""Module for Student class with JSON serialization/deserialization."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes in attrs are included.
        Otherwise, all attributes are included.
        """
        obj_dict = self.__dict__.copy()
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in obj_dict.items() if k in attrs}
        return obj_dict

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with values from json.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        if isinstance(json, dict):
            for key, value in json.items():
                setattr(self, key, value)
