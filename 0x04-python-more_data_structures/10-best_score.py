#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None or my_dict == {}:
        return None
    largest = max(my_dict.values())
    for x, y in my_dict.items():
        if y is largest:
            return x
