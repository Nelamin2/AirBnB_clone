#!/usr/bin/python3
""" unittests for models/amenity.py.
test classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_amenity_instantiation_without_argument(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_amenity_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id__str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_ids_is_unique(self):
        a = Amenity()
        b = Amenity()
        self.assertNotEqual(a.id, b.id)

    def test_args_not_used(self):
        a = Amenity()
        self.assertNotIn(x, a.__dict__.values())

    def test_passing_kwargs(self):
        time = datetime.today().isoformat()
        a = Amenity(id="345", created_at=time, updated_at=time)
        self.assertEqual(a.id, "345")
        self.assertEqual(a.created_at, datetime.today)
        self.assertEqual(a.updated_at, datetime.today)


class Amenity_save(unittest.TestCase):
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

    def test_one_save(self):
        a = Amenity()
        sleep(0.1)
        time_updated_at = a.updated_at
        a.save()
        self.assertLess(time_updated_at, a. updated_at)


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict."""

    def test_to_dict_type(self):
        a = Amenity()
        self.assertTrue(dict, type(a.to_dict()))


if __name__ == "__main__":
    unittest.main()
