#!/usr/bin/python3
""" Module that contains Rectangle module """


from turtle import width


class Rectangle:
    """ Class of Rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ method to retrieve the width value """
        return self.__width

    @property
    def height(self):
        """ Method to retrieve the height value """
        return self.__height

    @width.setter
    def width(self, value):
        """ Method to set the value of the width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @width.setter
    def height(self, value):
        """ Method to set the value of the width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """ Method that calculate the area of rectangle """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """ Method that calculate the perimter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return perim == 0
        perim = 2 * (self.__width + self.__height)
        return perim
