#!/usr/bin/python3
"""Creates student class"""


class Student:
    """Student presentation"""

    def __init__(self, first_name, last_name, age):
        """Creates new Student
        Args:
            first_name (str): param
            last_name (str): param
            age (int): param
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Student dict presentation
        Attributess is a list of strings
        included in the list.
        Args:
            attrs (list): param
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attrs of Student
        Args:
            json (dict): param
        """
        for k, v in json.items():
            setattr(self, k, v)
