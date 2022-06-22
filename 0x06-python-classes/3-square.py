#!/usr/bin/python3
""" module that create a class of square """


class Square:
    """ Square class with an attribute of sixe """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ method that return the area of a square """
    def area(self):
        return self.__size**2
