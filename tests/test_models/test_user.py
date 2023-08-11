#!/usr/bin/env python3
"""
Unittest module to test the User class
"""
import unittest
from models import user
User = user.User


class TestUserClass(unittest.TestCase):
    """
    Tests the User Class
    """

    def test_documentation(self):
        """
        check if all functions and class and the module
        itself is documented
        """
        self.assertIsNotNone(user.__doc__)
        self.assertIsNotNone(User.__doc__)
