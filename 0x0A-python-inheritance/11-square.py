#!/usr/bin/python3
""" module with the class BaseGeometry """


class BaseGeometry:
    """
    Class that contains area
    """

    @classmethod
    def area(self):
        """ method that raises an exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ methods that validates both value """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialization of privates"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """ method that prints the area of a rectangle """
        return self.__height * self.__width

    def __str__(self):
        """
        method that returns the implementation of
        the class in string format
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """Method for initialized the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """rectangle area"""

        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
