#!/usr/bin/python3
"""
base class
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
Square class
"""


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ size of square """
        self.__size = size
        super().__init__(self.__size, self.__size)
