#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""
import json
import os
import csv


class Base():
    """Base object template"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base init for object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json rep of a list of dictionaries

        Args:
            list_dictionaries ([list]): dict lis

        Returns:
            json: dict in json format
        """
        if list_dictionaries:
            return (json.dumps(list_dictionaries))
        return("[]")

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves class and list of objects into a file

        Args:
            list_objs (int): list with the instances
        """
        dict_list = [x.to_dictionary() for x in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w") as my_file:
            my_file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of json string

        Args:
            json_string ([list]): [list of dictionaries]

        Returns:
            list represented by json string
        """
        if json_string:
            return(json.loads(json_string))
        return ("[]")

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance from a dictionary
        """
        if (cls.__name__ == "Square"):
            dummy = cls(2)
        elif (cls.__name__ == "Rectangle"):
            dummy = cls(2, 2)
        dummy.update(**dictionary)
        return(dummy)

    @classmethod
    def load_from_file(cls):
        """Loads file and returns a list of instances
        """
        instance_list = []
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return (instance_list)
        with open(filename) as my_file:
            my_data = cls.from_json_string(my_file.read())
            for instance in my_data:
                instance_list.append(cls.create(**instance))
        return (instance_list)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves instance dict inf, in a csv file

        Args:
            list_objs (list): [List of csv files]
        """
        dict_list = [x.to_dictionary() for x in list_objs]
        filename = cls.__name__ + ".csv"
        if (cls.__name__ == "Rectangle"):
            header_list = ["id", "width", "height", "x", "y"]
        elif (cls.__name__ == "Square"):
            header_list = ["id", "size", "x", "y"]
        with open(filename, "w") as my_file:
            writer = csv.DictWriter(my_file, fieldnames = header_list)
            writer.writeheader()
            for my_dict in list_objs:
                writer.writerow(my_dict.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads csv and return list of instances with those
            characteristics
        """
        instance_list = []
        filename = cls.__name__ + ".csv"
        if not os.path.isfile(filename):
            return (instance_list)
        with open(filename) as my_file:
            csv_reader = csv.DictReader(my_file)
            for row in csv_reader:
                row = {key: int(row[key]) for key in row.keys()}
                instance_list.append(cls.create(**row))
        return(instance_list)
