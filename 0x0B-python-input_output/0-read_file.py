#!/usr/bin/python3
"""
read file func
"""


def read_file(filename=""):
    """read file and print
    Get nothing
    """
    with open(filename, "r", encoding="utf-8") as x:
        print(x.read(), end="")
