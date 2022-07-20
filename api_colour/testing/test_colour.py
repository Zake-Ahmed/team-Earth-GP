from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app
import requests
import requests_mock
import pytest

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_apples_juice(self):
        with requests_mock.Mocker() as m:
            with patch('requests.post') as p:
                m.get('http://localhost:5001/get/food', text='Apples')
                m.get('http://localhost:5050/get/drink', text='Juice')
                p.return_value.text = 'Apple Juice would be nice'

                response = self.client.get(url_for('get_order'))
                self.assertIn(b'Apples Juice', response.data)
                self.assertIn(b'Apple Juice would be nice', response.data)