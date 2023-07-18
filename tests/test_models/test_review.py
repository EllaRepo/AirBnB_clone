#!/usr/bin/python3
"""Defines unittests for models/review.py.
    Unittest classes:
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
    """Unittests for testing instantiation of the Review class.
    """

    def test_no_args_instantiates(self):
        """Test for Review instantiation with no args
        """
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        """Test for Review instance in stored objects dict
        """
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test for id attribute type
        """
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        """Test for created_at attribute type
        """
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test for updated_at attribute type
        """
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        """Test place_id attribute type
        """
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_public_class_attribute(self):
        """Test for user_id attribute type
        """
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_public_class_attribute(self):
        """Test for text attribute type
        """
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_two_reviews_unique_ids(self):
        """Test for two review instances' ids
        """
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_two_reviews_different_created_at(self):
        """Test for two city review created at different time
        """
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_two_reviews_different_updated_at(self):
        """Test for two review instances' updated_at atttibute value
        """
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_str_representation(self):
        """Test for str method representation
        """
        dt = datetime.today()
        dt_repr = repr(dt)
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        rvstr = rv.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

    def test_args_unused(self):
        """Test for Review instantiation with unused args
        """
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test for Review instantiation with kwargs
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "345")
        self.assertEqual(rv.created_at, dt)
        self.assertEqual(rv.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test for Review instantiation with none kwargs
        """
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review class.
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
        """Test for teardown method
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
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        self.assertLess(first_updated_at, rv.updated_at)

    def test_two_saves(self):
        """Test for two saves
        """
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        second_updated_at = rv.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rv.save()
        self.assertLess(second_updated_at, rv.updated_at)

    def test_save_with_arg(self):
        """Test for save with arg
        """
        rv = Review()
        with self.assertRaises(TypeError):
            rv.save(None)

    def test_save_updates_file(self):
        """Test for save updates file
        """
        rv = Review()
        rv.save()
        rvid = "Review." + rv.id
        with open("file.json", "r") as f:
            self.assertIn(rvid, f.read())


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class.
    """

    def test_to_dict_type(self):
        """Test for to_dict type
        """
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test for to_dict constains correct keys
        """
        rv = Review()
        self.assertIn("id", rv.to_dict())
        self.assertIn("created_at", rv.to_dict())
        self.assertIn("updated_at", rv.to_dict())
        self.assertIn("__class__", rv.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test for to_dict contains added attributes
        """
        rv = Review()
        rv.middle_name = "Alx"
        rv.my_number = 98
        self.assertEqual("Alx", rv.middle_name)
        self.assertIn("my_number", rv.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test for to_dict datetime attributes type
        """
        rv = Review()
        rv_dict = rv.to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test for to_dict output
        """
        dt = datetime.today()
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(rv.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test for to_dict vs __dict__
        """
        rv = Review()
        self.assertNotEqual(rv.to_dict(), rv.__dict__)

    def test_to_dict_with_arg(self):
        """Test for to_dict with args
        """
        rv = Review()
        with self.assertRaises(TypeError):
            rv.to_dict(None)


if __name__ == "__main__":
    unittest.main()
