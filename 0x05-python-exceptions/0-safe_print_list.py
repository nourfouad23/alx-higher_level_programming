#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    listIndex = 0
    while True:
        try:
            if listIndex < x:
                print(my_list[listIndex], end='')
                listIndex += 1
            else:
                print()
                return listIndex
        except IndexError:
            print()
            return listIndex
