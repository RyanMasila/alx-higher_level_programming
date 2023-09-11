#!/usr/bin/python3
"""Module with class BaseGeometry"""

class BaseGeometry
    """Empty class"""

    def area(self):
        """Raises an exception"""
        
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate if a num is an ineger"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
