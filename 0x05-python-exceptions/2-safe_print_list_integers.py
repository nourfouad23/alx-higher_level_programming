#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    listIndex = intsToPrint = 0
    while True:
        try:
            if listIndex < x:
                print("{:d}".format(my_list[listIndex]), end='')
                listIndex += 1
                intsToPrint += 1
            else:
                print()
                return intsToPrint
        except (ValueError, TypeError):
            listIndex += 1
