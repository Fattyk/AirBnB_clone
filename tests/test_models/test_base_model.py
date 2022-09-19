#!/usr/bin/python3
"""A unittest module for basemodel

This module (test_base_model.py) performs unittest on module basemodel.py
"""

from unittest import TestCase
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(TestCase):
    """A class that defines properties and methods for testing
    BaseModel classes.
    """
    def setUp(self):
        """This method prepare the fixture data for testing
        the BaseModel cases
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()
        self.my_model = my_model

    def test_model_name(self):
        """Assert that model name equals 'My First Model'"""
        self.assertEqual(self.my_model.name, "My First Model")

    def test_my_model_json_type(self):
        """Assert that the conversion type of model to json is dict"""
        my_model_json = self.my_model.to_dict()
        self.assertEqual(type(my_model_json), dict)

    def test_my_model_json_key_type(self):
        """Assert that all keys type in models dict exist in given list"""
        my_model_json = self.my_model.to_dict()
        for key in my_model_json.keys():
            self.assertIn(type(key), [int, str])


class TestBaseModelDict(TestBaseModel):
    """Extend existing Basemodel test class and add new cases"""
    def test_base_model_dict(self):
        """Assert that models are created from dict"""
        old_id = self.my_model.id
        my_model_json = self.my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.id, old_id)

