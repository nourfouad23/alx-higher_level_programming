#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_letter = sentence[0] if length > 0 else "None"
    to_return = length, first_letter
    return(to_return)
