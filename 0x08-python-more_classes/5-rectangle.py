#!/usr/bin/python3
"""Makes a class."""


class Rectangle:
    """A rectangle."""

    def __init__(self, width=0, height=0):
        """Implement a new Rectangle.
        Args:
            width (int): The rect width 
            height (int): The rect height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The rect width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The rect height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The rect area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """The rect perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """The rect printable presentation.
        Shows rectangle with the # char.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """The rect string presentation."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        '''method: __del__
           removes rect instance, and prints "bye" message
        '''
        print("Bye rectangle...")
