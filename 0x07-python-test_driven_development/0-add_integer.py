#!/usr/bin/python3
""" module that returns the addition of two integers """


def add_integer(a, b=98):
    """Function that adds 2 integers

    Args:
        a (int): first number
        b (int): second number

    Returns:
        a + b

    Raise:
        TypeError: if not an integer or a float raise TypeError

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
