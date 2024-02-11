#!/usr/bin/python3
"""The unittests for console.py.

classes:
    TestHBNBCommand_prompt
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import unittest
from models import storage
import os
import sys
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """testing prompting."""

    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """testing help messages."""
    def test_help_create(self):
        test_hp = ("Usage: create <class>\n        "
                   "Create an instance and print its id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(test_hp, output.getvalue().strip())

    def test_help_show(self):
        test_hp = ("Usage: show <class> <id> or <class>.show(<id>)\n        "
                   "Display the string representation of a class instance of"
                   " a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(test_hp, output.getvalue().strip())

    def test_help_show(self):
        test_hp = ("Usage: show <class> <id> or <class>.show(<id>)\n        "
                   "Display the string representation of a class instance of"
                   " a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(test_hp, output.getvalue().strip())

    def test_help_quit(self):
        test_hp = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_destroy(self):
        test_hp = ("Usage: destroy <class> <id> or"
                   "<class>.destroy(<id>)\n        "
                   "Delete a class instance of a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(test_hp, output.getvalue().strip())

    def test_help_EOF(self):
        test_hp = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(test_hp, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
