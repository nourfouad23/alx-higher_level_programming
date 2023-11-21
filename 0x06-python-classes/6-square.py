#!/usr/bin/python3
"""A class."""


class Square:
    """Present a class"""

    def __init__(self, size):
        """Initialize a new instance.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size


    @property
    def size(self):
        """Get/set size of square."""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("it must be integer")
        elif size < 0:
            raise ValueError("it must be greater than or equal 0")
        self.__size = size


    def area(self):
        """Get the area of a square."""
        return (self.__size * self.__size)


    def my_print(self):
        """Print a square with #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
