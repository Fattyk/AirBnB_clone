#!/usr/bin/python3
"""A unittest module for basemodel

This module (test_base_model.py) performs unittest on module basemodel.py
"""

from unittest import TestCase
from models.base_model import BaseModel


class TestBaseModel(TestCase):
        def setUp(self):
                 my_model = BaseModel()
                 my_model.name = "My First Model"
                 my_model.my_number = 89
                 my_model.save()
                 self.my_model = my_model

        def test_model_name(self):
                self.assertEqual(self.my_model.name, "My First Model")
                
        def test_my_model_json_type(self):
                my_model_json = self.my_model.to_dict()
                self.assertEqual(type(my_model_json), dict)

        def test_my_model_json_key_type(self):
                my_model_json = self.my_model.to_dict()
                for key in my_model_json.keys():
                        self.assertIn(type(key), [int, str])
