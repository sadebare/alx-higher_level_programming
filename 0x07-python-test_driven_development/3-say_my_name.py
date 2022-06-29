#!/bin/usr/python3
""" Module that prints name """


def say_my_name(first_name, last_name=""):
    """ Function that prints My name is <first name> <last name>
    Args:
        first_name: string format to print
        last_name: string format to print

    Raise:
        TypeError: if first_name and last_name not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
