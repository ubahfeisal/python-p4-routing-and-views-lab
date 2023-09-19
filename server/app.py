#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/<string>')
def print ():
    return f'<h1>print hello</h1>'

@app.route('/<int:count>')
def count(count):
    return f'<h1>{count}</h1>'

@app.route('/<integer>')
def math (num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else: 
        result = f'<h1>there is nothing like that</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
