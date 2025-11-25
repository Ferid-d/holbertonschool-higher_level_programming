#!/usr/bin/python3
"""Module for serializing and deserializing a custom Python object using pickle."""

import pickle


class CustomObject:
    """Represents a custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.

        Returns None if an exception occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, pickle.PickleError, IOError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file and return it.

        Returns None if an exception occurs.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except (FileNotFoundError, pickle.PickleError, EOFError, IOError):
            return None
