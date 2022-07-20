from application import app
from flask import Flask, Response
import requests

@app.route('/', methods=['GET'])
def get_order():
    food = (requests.get('http://service2:5001/get/food')).text
    drink = (requests.get('http://service3:5050/get/drink')).text
    
    order = food + " " + drink
    
    message = requests.post('http://service4:5005' + '/post/message', order)
    
    return render_template('home.html', order=order, message=message)
   