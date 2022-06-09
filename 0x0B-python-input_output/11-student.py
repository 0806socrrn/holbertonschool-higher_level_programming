#!/usr/bin/python3
"""student"""


class Student():
    """Class student"""

    def __init__(self, first_name, last_name, age):
        """Initialization method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student instance"""
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return(self.__dict__)

    def reload_from_json(self, json):
        """json"""
        for i, it in json.items():
            self.__dict__[it] = it
