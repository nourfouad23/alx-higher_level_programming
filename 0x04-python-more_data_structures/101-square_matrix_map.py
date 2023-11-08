#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda result: list(map(lambda i: i**2, result)), matrix)))
