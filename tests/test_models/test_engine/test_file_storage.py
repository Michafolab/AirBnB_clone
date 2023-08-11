#!/usr/bin/python3
"""
Testing module for the FileStorage module and class
"""
import unittest
import models.engine.file_storage as file_storage
from models.base_model import BaseModel
from models import storage
FileStorage = file_storage.FileStorage


class TestFileStorage(unittest.TestCase):
    """
    TestFileStorage:
        A class containing a suite of tests for the FileStorage
        module
    """
    def setUp(self):
        """
        sets up configuration for each test
        """

        self.my_model = BaseModel()
        self.my_model.name = "My_Testing_Model"
        self.my_model.number = 89
        self.my_model.save()

    def test_storage(self):
        """
        checks if it truely saves to storage
        """
        self.assertIsNotNone(storage.all())

    def test_model_not_none(self):
        """
        checks if the model created is not NULL
        """
        self.assertIsNotNone(self.my_model)

    def test_documentation(self):
        """
        checks if the module and all functions and
        classes are documented
        """
        self.assertIsNotNone(file_storage.__doc__)
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
