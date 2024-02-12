#!/usr/bin/python3
""" unittests for models/state.py.
test classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_stae_instantiation_without_argument(self):
        self.assertEqual(State, type(Amenity()))

    def test_state_stored_in_objects(self):
        self.assertIn(State(), models.storage.all())

    def test_state_id__str(self):
        self.assertEqual(str, type(State().id))

    def test_state_created_at_is_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_state_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_state_ids_is_unique(self):
        a = State()
        b = State()
        self.assertNotEqual(a.id, b.id)

    def test_state_args_not_used(self):
        a = State(x)
        self.assertNotIn(x, a.__dict__.values())

    def test_passing_kwargs(self):
        time = datetime.today.isoformat()
        a = State(id="345", created_at=time, updated_at=time)
        self.assertEqual(a.id, "345")
        self.assertEqual(a.created_at, datetime.today)
        self.assertEqual(a.updated_at, datetime.today)


class TestState_save(unittest.TestCase):
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
        a = State()
        sleep(0.1)
        time_updated_at = a.updated_at
        a.save()
        self.assertLess(time_updated_at, a. updated_at)


class TestState_to_dict(unittest.TestCase):
    """Unittests for testing to_dict."""

    def test_state_to_dict_type(self):
        a = State()
        self.assertTrue(dict, type(a.to_dict()))


if __name__ == "__main__":
    unittest.main()
