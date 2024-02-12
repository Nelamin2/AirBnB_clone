#!/usr/bin/python3
"""Defines the FileStorage module."""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent the filestorage.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieves allobjects from storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        FileStorage.__objects["{}.{}"
                              .format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        tempdic = FileStorage.__objects
        newobjdict = {obj: tempdic[obj].to_dict() for obj in tempdic.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(newobjdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                newobjdict = json.load(f)
                for o in newobjdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
