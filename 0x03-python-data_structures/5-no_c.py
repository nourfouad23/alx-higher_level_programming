#!/usr/bin/python3
def no_c(my_string):
    returned_str = ""
    for i in my_string:
        if i is not 'c' and i is not 'C':
            returned_str += i
    return (returned_str)
