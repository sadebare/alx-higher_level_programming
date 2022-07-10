#!/usr/bin/python3
""" Module that contains the Rectangle module """
from models.base import Base


class Rectangle(Base):
    """A class of Rectangle that inherit from  the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing width, height, x, y and id param """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getting width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setting the value of a width to the value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getting height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting the value of a height to the value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getting x value """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setting the value of a x to the value """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getting y value """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setting the value of a y to the value """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method that returns the area of a triangle """
        return self.__height * self.__width

    def display(self):
        """
        method that displays the recatngle mode base on height and width
        x is a new line
        and y is a space
        """
        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            print(self.__x * " " + '#' * self.__width)

    def __str__(self):
        """method that returns the string value of the input """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id,
                                                self.__x,
                                                self.__y,
                                                self.__width,
                                                self.__height)

    def update(self, *args, **kwargs):
        """ Method that assigns an argument to each attribute """
        if args:
            for arguments in range(len(args)):
                if arguments == 0:
                    self.id = args[arguments]
                if arguments == 1:
                    self.__width = args[arguments]
                if arguments == 2:
                    self.__height = args[arguments]
                if arguments == 3:
                    self.__x = args[arguments]
                if arguments == 4:
                    self.__y == args[arguments]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        This method returns the dictionary representation of a Rectangle
        """
        return ({'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width})
