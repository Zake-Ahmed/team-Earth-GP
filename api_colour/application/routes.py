from application import app
from flask import Flask, Response, render_template
import requests


@app.route('/', methods=['GET', 'POST'])
def get_order():
    food = (requests.get('http://localhost:5001/get/food')).text
    drink = (requests.get('http://localhost:5050/get/drink')).text
    
    order = food + " " + drink
    
    message = (requests.post('http://localhost:5005' + '/post/message', order)).text
    
    return render_template('home.html', order=order, message=message) 