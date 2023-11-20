#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        toPrint = a / b
        print("Inside result: {:.1f}".format(toPrint))
    except:
        toPrint = None
        print("Inside result: {}".format(toPrint))
    finally:
        return toPrint
