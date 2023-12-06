#!/usr/bin/python3
''' inherits_from
'''


def inherits_from(obj, a_class):
    '''inherit from class
    obj: param
    a_class: class
    returns Nothing
    '''
    return type(obj) != a_class and isinstance(obj, a_class)
