#!/usr/bin/python3
""" unittests for models/city.py.
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
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_city_instantiation_without_argument(self):
        self.assertEqual(City, type(City()))

    def test_city_stored_in_objects(self):
        self.assertIn(City(), models.storage.all())

    def test_city_id__str(self):
        self.assertEqual(str, type(City().id))

    def test_city_created_at_is_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_city_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_city_ids_is_unique(self):
        a = City()
        b = CIty()
        self.assertNotEqual(a.id, b.id)

    def test_city_args_not_used(self):
        a = City(x)
        self.assertNotIn(x, a.__dict__.values())

    def test_passing_kwargs(self):
        time = datetime.today.isoformat()
        a = City(id="345", created_at=time, updated_at=time)
        self.assertEqual(a.id, "345")
        self.assertEqual(a.created_at, datetime.today)
        self.assertEqual(a.updated_at, datetime.today)


class TestCity_save(unittest.TestCase):
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
        a = City()
        sleep(0.1)
        time_updated_at = a.updated_at
        a.save()
        self.assertLess(time_updated_at, a. updated_at)


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict."""

    def test_city_to_dict_type(self):
        a = User()
        self.assertTrue(dict, type(a.to_dict()))


if __name__ == "__main__":
    unittest.main()

