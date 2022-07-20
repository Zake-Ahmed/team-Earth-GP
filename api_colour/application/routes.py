from application import app
from flask import Flask, Response

@app.route('/', methods=['GET'])
def get_colour():
    food = (requests.get('http://service1:5001/get/food')).text
    if food == 'Apples':
        colour = 'Green'
    elif food == 'Bananas':
        colour = 'Yellow'
    elif food == 'Oranges':
        colour = 'Orange'
    elif food == 'Grapes':
        colour = 'Purple'
    else:
        colour = 'Red'
    return render_template('home.html', food=food, colour=colour)