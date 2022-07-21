from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

import requests_mock
import pytest

class TestBase(TestCase):
    def create_app(self):
        return app

class TestRandom(TestBase):
    def test_get_applej(self):
        response = self.client.post(url_for('post_message'), data="Apples Juice")
        self.assertIn(b'Apple Juice would be nice', response.data)
    
    def test_get_banj(self):
        response = self.client.post(url_for('post_message'), data="Bananas Juice")
        self.assertIn(b'Not sure about Banana Juice', response.data)
    
    def test_get_grapej(self):
        response = self.client.post(url_for('post_message'), data="Grapes Juice")
        self.assertIn(b'Grape Juice sounds good', response.data)
    
    def test_get_oj(self):
        response = self.client.post(url_for('post_message'), data="Oranges Juice")
        self.assertIn(b'Cannot go wrong with OJ', response.data)
    
    def test_get_strawj(self):
        response = self.client.post(url_for('post_message'), data="Strawberries Juice")
        self.assertIn(b'Strawberry juice is an interesting one', response.data)
    
    def test_get_unav(self):
        response = self.client.post(url_for('post_message'), data="Oranges Coffee")
        self.assertIn(b'unavailable', response.data)