from flask import Flask
import requests

service2 = 'http://service2:5001/get/food'
service3 = 'http://service3:5050/get/drink'

app = Flask(__name__)

from application import routes
