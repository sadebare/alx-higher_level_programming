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
        This method returns the JSON string representation of list_dictionaries
        """
        new = []
        if list_dictionaries is None or list_dictionaries == 0:
            return new
        else:
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
        """ Returns a list of instances """
        new_l = []
        rtn_empty = []
        file = "{}.json".format(cls.__name__)
        if path.isfile(file):
            with open(file, 'r') as f:
                new_l = cls.from_json_string(f.read())
            for val in new_l:
                rtn_empty.append(cls.create(**val))
            return (rtn_empty)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to csv file
        """

        res = [item.to_dictionary() for item in list_objs]
        with open(cls.__name__ + ".csv", mode="w") as save_file:
            write_to = csv.DictWriter(save_file, res[0].keys())
            write_to.writeheader()
            write_to.writerows(res)

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
