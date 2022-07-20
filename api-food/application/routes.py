from application import app
from flask import Flask, Response
import random

@app.route('/get/food', methods=['GET'])
def get_food():
    foods = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries']
    randomnum = random.randint(0,4)
    return Response(foods[randomnum], mimetype='text/plain')