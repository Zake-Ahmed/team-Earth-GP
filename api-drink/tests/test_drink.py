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
    def test_get_drink(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('get_drink'))
            self.assertIn(b'Juice', response.data)
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_drink'))
            self.assertIn(b'Milkshake', response.data)
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('get_drink'))
            self.assertIn(b'Smoothie', response.data)
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('get_drink'))
            self.assertIn(b'Coffee', response.data)
        with patch('random.randint') as r:
            r.return_value = 4
            response = self.client.get(url_for('get_drink'))
            self.assertIn(b'Iced Tea', response.data)


