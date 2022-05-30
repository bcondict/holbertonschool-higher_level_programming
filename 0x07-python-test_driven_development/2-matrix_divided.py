#!/usr/bin/python3
""" function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    error_mesage = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(num, int) or isinstance(num, float))
                    for num in [height for row in matrix for height in row])):
        raise TypeError(error_mesage)
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in j] for j in matrix]
