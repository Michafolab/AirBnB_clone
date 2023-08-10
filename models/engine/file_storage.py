#!/usr/bin/env python3
"""
A FileStorage module that handles how our applications
stores file and retrieve them
"""
import json


class FileStorage:
    """
    A FileStorage class:
        handles serializations to a file for our engine and
        deserialization for the application engine. AirBnB
    """
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """
        the initialization method for the FileStorage
        class
        """
        pass

    def all(self):
        """
        returns the dictionary `__objects`
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the `obj` with key `<obj classname>.id`
        """
        obj_class_name = obj.__class__.__name__
        obj_id = obj.id
        FileStorage.__objects[f"{obj_class_name}.{obj_id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        basically you are saving your data to a file defined in
        the __file_path private class variable
        """
        with open(FileStorage.__file_path, 'w') as f:
            obj = {}
            obj.update(FileStorage.__objects)
            for key, value in FileStorage.__objects.items():
                obj[key] = value.to_dict()
            f.write(json.dumps(obj))

    def reload(self):
        """
        deserializes the JSON file back to the __objects variable
        """
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, 'r') as f:
                content = json.loads(f.read())
                for key, value in content.items():
                    FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
