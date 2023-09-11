#!/usr/bin/python3
"""Module with method is_same_class"""

def is_same_class(obj, a_class):
    """Method to return True if an object belongs to a class"""

    return (type(obj) is a_class)
