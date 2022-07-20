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
            self.assertIn(b'Apple Juice would be nice', response.data)

    def test_bananas_juice(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/food', text='Bananas')
            m.get('http://service3:5050/get/drink', text='Juice')

            response = self.client.get(url_for('get_order'))
            self.assertIn(b'Bananas Juice', response.data)
            self.assertIn(b'Not sure about Banana Juice', response.data)

    def test_grapes_juice(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/food', text='Grapes')
            m.get('http://service3:5050/get/drink', text='Juice')

            response = self.client.get(url_for('get_order'))
            self.assertIn(b'Grapes Juice', response.data)
            self.assertIn(b'Grape Juice sounds good', response.data)

    def test_strawberries_juice(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/food', text='Strawberries')
            m.get('http://service3:5050/get/drink', text='Juice')

            response = self.client.get(url_for('get_order'))
            self.assertIn(b'Strawberries Juice', response.data)
            self.assertIn(b'Strawberry juice is an interesting one', response.data)

    def test_oranges_juice(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/food', text='Oranges')
            m.get('http://service3:5050/get/drink', text='Juice')

            response = self.client.get(url_for('get_order'))
            self.assertIn(b'Oranges Juice', response.data)
            self.assertIn(b'Cannot go wrong with OJ', response.data)
   




    def test_apples_milkshake(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/food', text='Apples')
            m.get('http://service3:5050/get/drink', text='Milkshake')

            response = self.client.get(url_for('get_order'))
            self.assertIn(b'Apples Milkshake', response.data)
            self.assertIn(b'unavailable', response.data)

    def test_apples_smoothie(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/food', text='Apples')
            m.get('http://service3:5050/get/drink', text='Smoothie')

            response = self.client.get(url_for('get_order'))
            self.assertIn(b'Apples Smoothie', response.data)
            self.assertIn(b'unavailable', response.data)

    def test_apples_coffee(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/food', text='Apples')
            m.get('http://service3:5050/get/drink', text='Coffee')

            response = self.client.get(url_for('get_order'))
            self.assertIn(b'Apples Coffee', response.data)
            self.assertIn(b'unavailable', response.data)

    def test_bananas_smoothie(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/food', text='Bananas')
            m.get('http://service3:5050/get/drink', text='Smoothie')

            response = self.client.get(url_for('get_order'))
            self.assertIn(b'Bananas Smoothie', response.data)
            self.assertIn(b'unavailable', response.data)