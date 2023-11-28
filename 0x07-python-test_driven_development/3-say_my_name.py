#!/usr/bin/python3
"""Print func"""


def say_my_name(first_name, last_name=""):
    """Print names.

    Args:
        first_name (str): Prints first name
        last_name (str): Print last name
    Raises:
        TypeError: First_name or last_name not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
