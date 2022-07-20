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
            m.get('http://service2:5001/get/food', text='Apples')
            m.get('http://service3:5050/get/drink', text='Juice')

            response = self.client.get(url_for('get_order'))
            self.assertIn(b'Apples Juice', response.data)

    def test_apples_milkshake(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/food', text='Apples')
            m.get('http://service3:5050/get/drink', text='Milkshake')

            response = self.client.get(url_for('get_order'))
            self.assertIn(b'Apples Milkshake', response.data)

    def test_apples_smoothie(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/food', text='Apples')
            m.get('http://service3:5050/get/drink', text='Smoothie')

            response = self.client.get(url_for('get_order'))
            self.assertIn(b'Apples Smoothie', response.data)

    def test_apples_coffee(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/food', text='Apples')
            m.get('http://service3:5050/get/drink', text='Coffee')

            response = self.client.get(url_for('get_order'))
            self.assertIn(b'Apples Coffee', response.data)

    def test_bananas_smoothie(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/food', text='Bananas')
            m.get('http://service3:5050/get/drink', text='Smoothie')

            response = self.client.get(url_for('get_order'))
            self.assertIn(b'Bananas Smoothie', response.data)