#!/usr/bin/python3
""" module that creates a class of Square """


class Square:
    """ Square class with an attribute of size """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ method that return the value of size """
        return self.__size

    @size.setter
    def size(self, value):
        """method that set size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ method that return the area of a square """
        return self.__size**2
