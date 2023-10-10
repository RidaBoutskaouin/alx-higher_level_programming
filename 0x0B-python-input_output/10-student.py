#!/usr/bin/python3
"""10-student.py - Defines the Student class"""


class Student:
    """retrieves a dictionary representation of a Student instance"""

    def __init__(self, first_name, last_name, age):
        """initializes a Student instance
        Args:
            first_name: first name of student
            last_name: last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=[]):
        """retrieves a dictionary representation of a Student instance
        Args:
            attrs: list of attributes to retrieve
        """
        if type(attrs) is not list:
            return self.__dict__
        for i in attrs:
            if type(i) is not str:
                return self.__dict__
        return {i: getattr(self, i) for i in attrs if hasattr(self, i)}

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Args:
            json: dictionary of attributes
        """
        for i in json:
            setattr(self, i, json[i])
