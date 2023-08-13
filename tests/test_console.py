#!/usr/bin/env python3
"""
Testing module for the console.
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    TestConsole:
        A testing class to test our application console functionality
    """

    def test_console(self):
        """
        test our console!!!!
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), '')
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), '')
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), '')

    def test_console_2(self):
        """
        test our console
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertIsNotNone(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
            f.seek(0)
            f.truncate()
            HBNBCommand().onecmd("show 1342")
            self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')

    def test_console_3(self):
        """
        test our console!!!
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), '** instance id missing **\n')
            f.seek(0)
            f.truncate()
            HBNBCommand().onecmd("show BaseModel 132")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
            f.seek(0)
            f.truncate()
            HBNBCommand().onecmd("destroy Base")
            self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
            f.seek(0)
            f.truncate()
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("all BaseModel")
            self.assertIsNotNone(f.getvalue())
            f.seek(0)
            f.truncate()
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue(), '** class name missing **\n')
            f.seek(0)
            f.truncate()
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
            f.seek(0)
            f.truncate()
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd(f"update BaseModel {f.getvalue()} name clement")
            self.assertIsNotNone(f.getvalue())
            f.seek(0)
            f.truncate()
            HBNBCommand().onecmd("BaseModel.all()")
            self.assertIsNotNone(f.getvalue())

    def test_console_4(self):
        """
        tests for our application console
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            instance_id = f.getvalue()
            f.seek(0)
            f.truncate()
            # ----- remove the new line -----
            instance_id = instance_id[:-1]
            command = f"update BaseModel {instance_id}"
            HBNBCommand().onecmd(command)
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")
            f.seek(0)
            f.truncate()
            command = f"update BaseModel {instance_id} attr_name"
            HBNBCommand().onecmd(command)
            self.assertEqual(f.getvalue(), "** value missing **\n")

    def test_console_5(self):
        """
        unittests for our application console
        """
        with patch('sys.stdout', new=StringIO()) as f:
            command = "BaseModel.all()"
            HBNBCommand().onecmd(command)
            self.assertIsNotNone(f.getvalue())
