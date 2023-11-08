#!/usr/bin/python3
def multiply_by_2(my_dict):
    temp_dict = my_dict.copy()
    for i in temp_dict.keys():
        temp_dict[i] *= 2
    return (temp_dict)
