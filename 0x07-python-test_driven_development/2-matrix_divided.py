#!/usr/bin/python3

"""A matrix division function"""

def matrix_divided(matrix, div):

    """Divides all elements of matrix by div"""

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError('matrix must be a matrix (list of lists) of'
                        'integers/floats')
    for i in matrix:
        if type(i) is not list or len(i) == 0:
            raise TypeError('matrix must be a matrix (list of lists) of'
                        'integers/floats')
        for a in matrix[i]:
            if type(a) is not int and type(a) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of'
                        'integers/floats')
    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new = [i[:] for i in matrix]
    for i in range(len(matrix)):
        for a in range(len(matrix[0])):
            new[i][a] = round(matrix[i][a] / div, 2)

    return new
