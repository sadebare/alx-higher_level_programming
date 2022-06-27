#!/usr/bin/python3
""" Module that contains Rectangle module """


class Rectangle:
    """ Class of Rectangle """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Instantiate height and width """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @height.setter
    def height(self, value):
        """ Method to set the value of the width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """ Method that calculate the area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Method that calculate the perimter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        " Prints a rectangle with `#` "
        if self.__width == 0 or self.__height == 0:
            return ""
        res = ""
        for i in range(self.__height):
            for j in range(self.__width):
                res += "#"
            res += "\n"
        return res[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Print a message when an instance of Rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
