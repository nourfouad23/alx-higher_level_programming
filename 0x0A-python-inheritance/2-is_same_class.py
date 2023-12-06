#!/usr/bin/python3
# is_same_class.py

"""Creates class"""


def is_same_class(obj, a_class):
    """Scan for a class
    Args:
        obj (any): param
        a_class (type): A class
    Returns:
        True or False
    """
    if type(obj) == a_class:
        return True
    return False
