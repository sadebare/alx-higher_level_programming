#!/usr/bin/python3
""" module with Base class """
import json
from os import path
import csv


class Base:
    """ A class of base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization of id attribute """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            returns JSON string repr of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method that writes the JSON string
        representation of list_objs to a file:
        """
        file = "{}.json".format(cls.__name__)
        new = []
        with open(file, 'w') as f:
            if list_objs is None:
                f.write("{}")
            for obj in list_objs:
                new.append(obj.to_dictionary())
            f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """
        method that returns the list of the
        JSON string representation json_string:
        """
        new = []
        if json_string is None or json_string == 0:
            return new
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        method that returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new_c = cls(1, 1)
        if cls.__name__ == "Square":
            new_c = cls(1)
        new_c.update(**dictionary)
        return (new_c)

    @classmethod
    def load_from_file(cls):
        """
            returns a list of instances
        """
        fname = cls.__name__ + ".json"

        try:
            with open(fname, encoding='utf8') as jfile:
                content = cls.from_json_string(jfile.read())
        except:
            return []

        instances = []

        for instance in content:
            temp = cls.create(**instance)
            instances.append(temp)

        return

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the JSON strin representation of list_objs to a file
        """
        fname = cls.__name__ + ".json"
        content = []

        if list_objs is not None:
            for obj in list_objs:
                obj = obj.to_dictionary()
                json_dict = json.loads(cls.to_json_string(obj))
                content.append(json_dict)

        with open(fname, "w") as jfile:
            json.dump(content, jfile)

    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv file
        """

        res = []
        res_dict = {}
        with open(cls.__name__ + ".csv", mode="r") as read_file:
            read_from = csv.DictReader(read_file)
            for item in read_from:
                for k, v in dict(item).items():
                    res_dict[k] = int(v)
                # formatting with create()
                res.append(cls.create(**res_dict))
        return res
