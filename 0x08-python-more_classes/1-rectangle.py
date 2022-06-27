#!/usr/bin/python3
""" Module contains a Rectangle class """


class Rectangle:
    """ This class contains width and height as methods in the class """
    def __init__(self, width=0, height=0):
        """Initialization of the Current Rectangle class
        Args:
            width (int) - width of the rectangle
            height (int) - height of the triangle
        """
        self.width = width
        self.heigh = height

    @property
    def width(self):
        """ To retrieve the width """
        return self.__width

    @width.setter
    def width(self, value):
        """Method that set the width to value
        Args:
            value - width to be set to.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ To retrieve height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method to set the height of the rectangle to value
        Args:
            value - height to set the height to
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
