#!/usr/bin/python3
"""Func to print square"""


def print_square(size):
    """Print a square with the #

    Args:
        size (int): Height or width of square
    Raises:
        TypeError: Height or width are not an int
        ValueError: Size less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
