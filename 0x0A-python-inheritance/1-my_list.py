#!/usr/bin/python3
""" module that entails a class of MyList """


class MyList(list):
    """ A class that inherit from list class and method print_sorted"""
    pass

    def print_sorted(self):
        """ method that print sorted list in ascending order """

        print(sorted(list(self)))
