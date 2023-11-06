#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolist = my_list[:]
    for counter, x in enumerate(my_list):
        if x % 2 == 0:
            boolist[counter] = True
        else:
            boolist[counter] = False
    return(boolist)
