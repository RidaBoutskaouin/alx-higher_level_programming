#!/usr/bin/python3
"""Module that contains a function that returns True if the object
is an instance of a class that inherited (directly or indirectly)
from the specified class"""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class"""
    if type(obj) is not a_class:
        return isinstance(obj, a_class)
    return False
