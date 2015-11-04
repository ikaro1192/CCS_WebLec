#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/login")

@app.route("/login")
def login():
    return "login"

if __name__ == "__main__":
    app.run(debug=True)

