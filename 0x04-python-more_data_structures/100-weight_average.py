#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    result = 0
    result2 = 0
    for i, j in my_list:
        result += i * j
        result2 += j
    return (result / result2)
