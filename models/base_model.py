#!/usr/bin/env python3
"""
A base model module for the airbnb project
"""
import uuid 
from datetime import datetime


class BaseModel:
    """
    A BaseModel class part of the base model module
    for the hbnb project
    """
    def __init__(self):
        """
        the init method to initialize our objects
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        returns a string representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the object created from the class
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_to_return = self.__dict__
        dict_to_return["__class__"] =  self.__class__.__name__
        dict_to_return["created_at"] = self.created_at.isoformat()
        dict_to_return["updated_at"] = self.updated_at.isoformat()
        return dict_to_return
