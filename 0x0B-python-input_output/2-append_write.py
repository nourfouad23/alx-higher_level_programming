#!/usr/bin/python3
"""append file func"""


def append_write(filename="", text=""):
    """Add a string to file
    Args:
        filename (str): param
        text (str): param
    Returns:
        Number of added chars
    """
    with open(filename, "a", encoding="utf-8") as x:
        return x.write(text)
