#!/usr/bin/python3
"""It's an add function"""


def add_integer(a, b=98):
    """Get the integer after adding a and b.

    Float args are casted to ints before additing

    Raises:
        TypeError: If a or b are not integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
    