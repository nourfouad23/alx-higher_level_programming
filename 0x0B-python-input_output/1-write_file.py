#!/usr/bin/python3
"""
writes string to file func
"""


def write_file(filename="", text=""):
    """ write file
    """
    with open(filename, 'w') as f:
        return f.write(text)
