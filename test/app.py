#!/bin/python3

from flask import Flask,request

app = Flask(__name__)

@app.route('/calc',methods=['GET'])
def hello_world():
    return request.args.get("name")

if __name__ == '__main__':
    app.run(debug=True)
