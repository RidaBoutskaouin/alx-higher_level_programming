#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list."""
    new_list = []
    for item in my_list:
        new_list.append(True) if item % 2 == 0 else new_list.append(False)
    return new_list
