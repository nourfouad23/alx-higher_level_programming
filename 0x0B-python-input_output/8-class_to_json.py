#!/usr/bin/python3
'''describe dict func
'''


def class_to_json(obj):
    ''' class to json func
       returns a dict
    '''
    return obj.__dict__
