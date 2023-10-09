#!/usr/bin/python3
"""4-inherits_from"""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class"""
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
