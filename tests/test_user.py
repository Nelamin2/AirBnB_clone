#!/usr/bin/python3
""" unittests for models/user.py.
test classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_user_instantiation_without_argument(self):
        self.assertEqual(User, type(User()))

    def test_user_stored_in_objects(self):
        self.assertIn(User(), models.storage.all())

    def test_user_id__str(self):
        self.assertEqual(str, type(User().id))

    def test_user_created_at_is_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_user_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_user_ids_is_unique(self):
        a = User()
        b = User()
        self.assertNotEqual(a.id, b.id)

    def test_user_args_not_used(self):
        a = User(x)
        self.assertNotIn(x, a.__dict__.values())

    def test_passing_kwargs(self):
        time = datetime.today.isoformat()
        a = User(id="345", created_at=time, updated_at=time)
        self.assertEqual(a.id, "345")
        self.assertEqual(a.created_at, datetime.today)
        self.assertEqual(a.updated_at, datetime.today)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "test")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("test", "file.json")
        except IOError:
            pass

    def test_one_user_save(self):
        a = User()
        sleep(0.1)
        time_updated_at = a.updated_at
        a.save()
        self.assertLess(time_updated_at, a. updated_at)


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict."""

    def test_user_to_dict_type(self):
        a = User()
        self.assertTrue(dict, type(a.to_dict()))


if __name__ == "__main__":
    unittest.main()

