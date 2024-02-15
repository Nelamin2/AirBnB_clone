#!/usr/bin/python3
""" unittests for models/place.py.
test classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_place_instantiation_without_argument(self):
        self.assertEqual(Place, type(Place()))

    def test_place_stored_in_objects(self):
        self.assertIn(Place(), models.storage().values())

    def test_place_id__str(self):
        self.assertEqual(str, type(Place().id))

    def test_place_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_place_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_place_ids_is_unique(self):
        a = Place()
        b = Place()
        self.assertNotEqual(a.id, b.id)

    def test_place_args_not_used(self):
        x = Place()
        self.assertNotIn(x, a.__dict__.values())

    def test_passing_kwargs(self):
        time = datetime.today()
        time_iso.= time.isoformat()
        a = Place(id="345", created_at=time, updated_at=time)
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
        a = Place()
        sleep(0.1)
        time_updated_at = a.updated_at
        a.save()
        self.assertLess(time_updated_at, a. updated_at)


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict."""

    def test_place_to_dict_type(self):
        a = Place()
        self.assertTrue(dict, type(a.to_dict()))


if __name__ == "__main__":
    unittest.main()
