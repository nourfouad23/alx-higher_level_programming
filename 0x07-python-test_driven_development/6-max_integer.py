#!/usr/bin/python3
"""List max int
"""


def max_integer(list=[]):
    """Max int a list func
        Func returns None if empty
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
