#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:string>")
def print_string(string):
    print(string)
    return string

@app.route('/count/<int:number>')
def count(number):
    count = f''
    for n in range(number):
        count += f'{n}\n'
    return count
    
@app.route('/math/<int:num1>/<string:opperator>/<int:num2>')
def math(num1, opperator, num2):
    if opperator == '+':
        return str(num1 + num2)
    elif opperator == '-':
        return str(num1 - num2)
    elif opperator == '*':
        return str(num1 * num2)
    elif opperator == 'div':
        return str(num1 / num2)
    elif opperator == "%":
        return str(num1 % num2)