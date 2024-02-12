#!/usr/bin/python3
""" unittests for models/Review.py.
test classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_review_instantiation_without_argument(self):
        self.assertEqual(Review, type(Review()))

    def test_review_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all())

    def test_review_id__str(self):
        self.assertEqual(str, type(Review().id))

    def test_review_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_review_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_review_ids_is_unique(self):
        a = Review()
        b = Review)
        self.assertNotEqual(a.id, b.id)

    def test_review_args_not_used(self):
        a = Review(x)
        self.assertNotIn(x, a.__dict__.values())

    def test_passing_kwargs(self):
        time = datetime.today.isoformat()
        a = Review(id="345", created_at=time, updated_at=time)
        self.assertEqual(a.id, "345")
        self.assertEqual(a.created_at, datetime.today)
        self.assertEqual(a.updated_at, datetime.today)


class TestReview_save(unittest.TestCase):
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

    def test_one_review_save(self):
        a = Review()
        sleep(0.1)
        time_updated_at = a.updated_at
        a.save()
        self.assertLess(time_updated_at, a. updated_at)


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict."""

    def test_Review_to_dict_type(self):
        a = Review()
        self.assertTrue(dict, type(a.to_dict()))


if __name__ == "__main__":
    unittest.main()

