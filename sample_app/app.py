#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, session, request, redirect, render_template
import sqlite3
import hashlib
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'The secret key which ciphers the cookie'


def connect_db():
    con = sqlite3.connect('data.db')
    con.row_factory = sqlite3.Row
    return con

def check_login():
    if session.get('user_id') is not None:
        return True
    return False

def check_loan():
    con = connect_db()
    cur = con.cursor()
    cur.execute('select * from LoanInfo where user_id=?',(session['user_id'],))
    loanInfo = cur.fetchone()
    return loanInfo is not None

def calculate_password_hash(password, salt):
    return hashlib.sha256(password + ':' + salt).hexdigest()

@app.before_request
def before_request():
    if request.path == '/login':
        return

    if check_login():
        return
    else:
        return redirect('/login')


@app.route('/')
def index_view():
    if check_loan():
        return render_template('return.html')
    else:
        con = connect_db()
        cur = con.cursor()
        cur.execute('select name from Books')
        books = cur.fetchall()
        con.close()
        return render_template('index.html',books=books)


@app.route('/login', methods=['GET', 'POST'])
def login_view():
    error = None
    if request.method == 'POST':
        con = connect_db()
        cur = con.cursor()
        cur.execute('select * from Users where name=?',(request.form['name'],))
        user = cur.fetchone()
        con.close()

        if (user is not None) and (user['pass'] == request.form['pass']):
            session['user_id'] = user['id']
            return redirect('/')
        else:
            error='invalid user name or password'

    return render_template('login.html',error=error)


@app.route('/logout')
def logout_view():
    session.pop('user_id', None)
    return 'logout'

@app.route('/loan/<book_id>', methods=['POST'])
def loan_view(book_id):
        con = connect_db()
        cur = con.cursor()
        cur.execute('insert into LoanInfo(user_id,book_id) values(?,?)',(session['user_id'], book_id))
        con.commit()
        con.close()
        return '貸出処理しました!'

@app.route('/return', methods=['GET','Post'])
def return_book_view():
    con = connect_db()
    cur = con.cursor()
    cur.execute('delete from LoanInfo where user_id=?',(session['user_id'],))
    con.commit()

    return '返却処理しました!'


if __name__ == '__main__':
        app.run(debug=True)
