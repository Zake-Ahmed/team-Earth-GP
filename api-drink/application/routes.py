from application import app
from flask import Flask, Response
import random

@app.route('/get/drink', methods=['GET'])
def get_drink():
    drinks = ['Juice', 'Milkshake', 'Smoothie', 'Coffee', 'Iced Tea']
    randomnum = random.randint(0,4)
    return Response(drinks[randomnum], mimetype='text/plain')