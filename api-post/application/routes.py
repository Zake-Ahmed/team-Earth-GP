from application import app
from flask import Flask, Response, request
import random

@app.route('/post/message', methods=['POST'])
def post_message():
    order = request.data.decode('utf-8')
    x = order.split(" ", 1)
    food = x[0]
    drink = x[1]
    if food == "Apples" and drink == "Juice":
        return "Apple Juice would be nice"
    elif food == "Bananas" and drink == "Juice":
        return "Not sure about Banana Juice"
    elif food == "Grapes" and drink == "Juice":
        return "Grape Juice sounds good"
    elif food == "Strawberries" and drink == "Juice":
        return "Strawberry juice is an interesting one"
    elif food == "Oranges" and drink == "Juice":
        return "Cannot go wrong with OJ"
    else:
        return "unavailable"