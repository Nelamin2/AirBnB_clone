#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
unitests includes three classes:
TestBaseModel_instantiation
TestBaseModel_save
TestBaseModel_to_dict"""

import unittest
from models.base_model import BaseModel
import os
from datetime import datetime
from time import sleep


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_instantiation_without_argument(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_obj_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all())

    def test_id__str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_ids_is_unique(self):
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(A.id, B.id)

    def test_args_not_used(self):
        a = BaseModel(x)
        self.assertNotIn(x, a.__dict__.values())

    def test_passing_kwargs(self):
        time = datetime.today.isoformat()
        bm = BaseModel(id="345", created_at=time, updated_at=time)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, datetime.today)
        self.assertEqual(bm.updated_at, datetime.today)


class TestBaseModel_save(unittest.TestCase):
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
        a = BaseModel()
        sleep(0.1)
        time_updated_at = a.updated_at
        a.save()
        self.assertLess(time_updated_at, a. updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict."""

    def test_to_dict_type(self):
        a = BaseModel()
        self.assertTrue(dict, type(a.to_dict()))


if __name__ == "__main__":
    unittest.main()
