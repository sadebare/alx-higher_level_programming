#!/usr/bin/python3
""" module with method lookup """


def lookup(obj):
    """ function that returns the lists of available attr and mthd """
    return dir(obj)
