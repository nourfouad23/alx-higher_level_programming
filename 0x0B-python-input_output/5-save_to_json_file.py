#!/usr/bin/python3
''' writes an obj in a text file
'''
import json


def save_to_json_file(my_obj, filename):
    ''' save to json file func
    accepts obj
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
