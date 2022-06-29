#!/usr/bin/python3
""" modeule that divides all elements in matrix """


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix and return a new matrix
    Args:
        matrix (list): A list containing either float or an integer
        div (int/float): The divisor of the list

    Raise:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
                   Each row of the matrix must have the same size
                   div must be a number
        ZeroDivisionError: division by zero not possible

    Return:
        A new matrix which entails the division of matrix
    """

    result = 0
    new_matrix = []
    new_list = []
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    err4 = "division by zero"

    if not matrix:
        raise TypeError(err1)
    if type(div) != int and type(div) != float:
        raise TypeError(err3)
    if div == 0:
        raise TypeError(err4)
    longitude = len(matrix[0])
    for element in matrix:
        if type(element) is not list:
            raise TypeError(err1)
        if len(element) != longitude:
            raise TypeError(err2)
        for item in element:
            if type(item) is not int and type(item) is not float:
                raise TypeError(err1)
            num = item / div
            new_list.append(round(num, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
