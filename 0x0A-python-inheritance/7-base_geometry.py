#!/usr/bin/python3
"""Creates a geometry class"""


class BaseGeometry:
    """Shows base geometry"""

    def area(self):
        """No implementation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check parameter if int
        Args:
            name (str): param
            value (int): param
        Raises:
            TypeError: Value not an int
            ValueError: Value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
