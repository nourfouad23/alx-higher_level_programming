#!/usr/bin/python3
"""A class."""


class Square:
    """Present a class"""

    def __init__(self, size):
        """Initialize a new instance.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("it must be integer")
        elif size < 0:
            raise ValueError("it must be greater than or equal 0")
        self.__size = size
