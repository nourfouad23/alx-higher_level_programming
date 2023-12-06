#!/usr/bin/python3
''' a list
'''


class MyList(list):
    ''' Shows a list
    '''

    def print_sorted(self):
        '''
        sort a list and print it
        '''
        print(sorted(self))
