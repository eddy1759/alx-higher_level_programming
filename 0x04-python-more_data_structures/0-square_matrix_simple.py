#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    data = []
    for i in matrix:
        data.append([j ** 2 for j in i])
    return data
