#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, redirect ,request,render_template

app = Flask(__name__)

@app.route("/check")
def check():
    return render_template('check.html')

@app.route('/',methods=['POST'])
def index():
    my_age = int(request.form["age"])
    my_name = request.form["name"]
    return render_template('index.html',age=my_age,name=my_name)

if __name__ == '__main__':
    app.run(debug=True)
