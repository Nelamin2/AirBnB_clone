#!/usr/bin/python3
"""This is the Basemodel module"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """the  Basemodel class of HBNB"""

    def __init__(self, *args, **kwargs):
        """class initilizer
        Args:
            *args: Unused.
            **kwargs : Key/value pairs of attributes for dictionary.
        """

        t = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, t)
                else:
                    self.__dict__[k] = v
            else:
                models.storage.new(self)

    def __str__(self):
        """print the string represntation of the class with id and dic"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}"\
               .format(classname, self.id, self.__dict__)

    def save(self):
        """a method to save upated_at with the current datetime."""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the created instance of class."""

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
