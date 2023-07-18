#!/usr/bin/python3
"""Defines unittests for models/user.py.
    Unittest classes:
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
    """Unittests for testing instantiation of the User class.
    """

    def test_no_args_instantiates(self):
        """Test for User instantiation with no args
        """
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        """Test for User instance in stored objects dict
        """
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test for id attribute type
        """
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """Test for City instantiation with no args
        """
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test for updated_at attribute type
        """
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        """Test for email attribute type
        """
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        """Test for password attribute type
        """
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        """Test for first_name attribute type
        """
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        """Test for last_name attribute type
        """
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        """Test for two State instances' ids
        """
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_users_different_created_at(self):
        """Test for two State instances created at different time
        """
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_users_different_updated_at(self):
        """Test for two user instances' updated_at atttibute value
        """
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_str_representation(self):
        """Test for str method representation
        """
        dt = datetime.today()
        dt_repr = repr(dt)
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        usstr = us.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + dt_repr, usstr)
        self.assertIn("'updated_at': " + dt_repr, usstr)

    def test_args_unused(self):
        """Test for City instantiation with unused args
        """
        us = User(None)
        self.assertNotIn(None, us.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test for City instantiation with kwargs
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us.id, "345")
        self.assertEqual(us.created_at, dt)
        self.assertEqual(us.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test for City instantiation with none kwargs
        """
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the  class
    """

    @classmethod
    def setUp(self):
        """Test setup method
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Test teardown method
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test for one save
        """
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        self.assertLess(first_updated_at, us.updated_at)

    def test_two_saves(self):
        """Test for two saves
        """
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        second_updated_at = us.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        us.save()
        self.assertLess(second_updated_at, us.updated_at)

    def test_save_with_arg(self):
        """Test for save with arg
        """
        us = User()
        with self.assertRaises(TypeError):
            us.save(None)

    def test_save_updates_file(self):
        """Test for save update file
        """
        us = User()
        us.save()
        usid = "User." + us.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class.
    """

    def test_to_dict_type(self):
        """Test for to_dict type
        """
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test for to_dict constains correct keys
        """
        us = User()
        self.assertIn("id", us.to_dict())
        self.assertIn("created_at", us.to_dict())
        self.assertIn("updated_at", us.to_dict())
        self.assertIn("__class__", us.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test for to_dict contains added attributes
        """
        us = User()
        us.middle_name = "Alx"
        us.my_number = 98
        self.assertEqual("Alx", us.middle_name)
        self.assertIn("my_number", us.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test for to_dict datetime attributes type
        """
        us = User()
        us_dict = us.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test for to_dict output
        """
        dt = datetime.today()
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(us.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test for to_dict vs __dict__
        """
        us = User()
        self.assertNotEqual(us.to_dict(), us.__dict__)

    def test_to_dict_with_arg(self):
        """Test for to_dict with args
        """
        us = User()
        with self.assertRaises(TypeError):
            us.to_dict(None)


if __name__ == "__main__":
    unittest.main()
