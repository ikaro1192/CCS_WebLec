#!/bin/python3

from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    who = request.args.get("who")
    return who

if __name__ == '__main__':
    app.run(debug=True)
