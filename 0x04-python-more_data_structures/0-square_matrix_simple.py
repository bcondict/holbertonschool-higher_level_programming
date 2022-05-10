#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_value = []
    row_matrix = []
    for i in matrix:
        for j in i:
            row_matrix.append(j ** 2)
        square_value.append(row_matrix)
        row_matrix = []
    return square_value
