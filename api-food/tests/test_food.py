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
    def test_get_food(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('get_food'))
            self.assertIn(b'Apple', response.data)
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_food'))
            self.assertIn(b'Bananas', response.data)
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('get_food'))
            self.assertIn(b'Oranges', response.data)
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('get_food'))
            self.assertIn(b'Grapes', response.data)
        with patch('random.randint') as r:
            r.return_value = 4
            response = self.client.get(url_for('get_food'))
            self.assertIn(b'Strawberries', response.data)


