#!/usr/bin/python3
""" module that contains load_to_json_file module """
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”:
    """
    with open(filename, mode="r") as a_file:
        json.load(a_file)
