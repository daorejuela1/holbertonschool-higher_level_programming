#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""
import json
import os
import csv
import turtle
import random


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
            writer = csv.DictWriter(my_file, fieldnames=header_list)
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

    def draw(list_rectangles, list_squares):
        """Draws the rectangle and squares.

        Args:
            list_rectangles (list): List with instances with rectangle
            list_squares (list): List with instances of squares
        """
        dict_list = [x.to_dictionary() for x in list_rectangles]
        square_list = [y.to_dictionary() for y in list_squares]
        wn = turtle.Screen()
        wn.title("Display your figures")
        wn_size = (1024, 768)
        wn.setup(width=wn_size[0], height=wn_size[1], startx=0, starty=0)
        wn.setworldcoordinates(0, 1024, 768, 0)
        # len (first object)
        for my_dict in dict_list:
            rgb = [random.random() for x in range(3)]
            turtle.shape("square")
            turtle.hideturtle()
            turtle.penup()
            # Set object width and height
            turtle.shapesize(my_dict["width"]*0.5, my_dict["height"]*0.5, 2)
            turtle.fillcolor(rgb[0], rgb[1], rgb[2])
            # Set object pos x, y
            turtle.goto(my_dict["x"], my_dict["y"])
            turtle.showturtle()
            turtle.pendown()
            turtle.stamp()
            turtle.speed(1)
        for my_dict in square_list:
            rgb = [random.random() for x in range(3)]
            turtle.shape("square")
            turtle.hideturtle()
            turtle.penup()
            # Set object width and height
            turtle.shapesize(my_dict["size"]*0.5, my_dict["size"]*0.5, 2)
            turtle.fillcolor(rgb[0], rgb[1], rgb[2])
            # Set object pos x, y
            turtle.goto(my_dict["x"], my_dict["y"])
            turtle.showturtle()
            turtle.pendown()
            turtle.stamp()
            turtle.speed(1)
        input()
