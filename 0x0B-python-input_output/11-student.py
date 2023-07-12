#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represent Student"""
    def __init__(self, first_name, last_name, age):
        """initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student"""
        for k, v in json.items():
            setattr(self, k, v)
