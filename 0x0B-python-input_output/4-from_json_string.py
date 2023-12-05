#!/usr/bin/python3
''' presented a JSON string
'''

import json


def from_json_string(my_str):
    ''' from json string func
     return objs
    '''
    return json.loads(my_str)
