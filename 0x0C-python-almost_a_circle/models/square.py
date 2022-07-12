#!/usr/bin/python3
""" module that contains the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class of Square that inherit from  the Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Method that returns the size """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x,
                                             self.y, self.size)

    def update(self, *args, **kwargs):
        """ This method assigns an argument to each attribute """
        if args:
            for id in range(len(args)):
                if id == 0:
                    self.id = args[id]
                if id == 1:
                    self.size = args[id]
                if id == 2:
                    self.x = args[id]
                if id == 3:
                    self.y = args[id]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ method that returns the dictionary representation of a Square """
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})
