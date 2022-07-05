#!/usr/bin/python3
import json
""" module that contains to_json_string function """


def to_json_string(my_obj):
    """
    Function that returns the JSON
    representation of an object (string):
    """
    return json.dumps(my_obj)
    
