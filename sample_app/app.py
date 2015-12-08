#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, session, request, redirect, render_template
from functools import wraps
import sqlite3
import hashlib
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xfe\xbaK\xc4\xb2\xd5t\xf7\x189\xf1p<\xf4\xa2\xc1\xf4\x88\x9e\xc6\xd7\xa3\xda\xde'

# 認証ページ用デコレータ
def auth_require(page):
    @wraps(page)
    def decorated_function(*args, **kwargs):
        if not check_login():
            return redirect('/login')
        return page(*args, **kwargs)
    return decorated_function

def connect_db():
    con = sqlite3.connect('data2.db')
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
    text=(password+salt).encode('utf-8')
    result = hashlib.sha512(text).hexdigest()
    return result

@app.route('/')
@auth_require
def index_view():
    if check_loan():
        return render_template('return.html')
    else:
        con = connect_db()
        cur = con.cursor()
        cur.execute('select * from Books')
        books = cur.fetchall()
        con.close()
        print(books[0]['id'])
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

        if (user is not None) and (user['pass_hash'] == calculate_password_hash(request.form['pass'], user['salt'])):
            session['user_id'] = user['id']
            return redirect('/')
        else:
            error='invalid user name or password'

    return render_template('login.html',error=error)


@app.route('/logout')
@auth_require
def logout_view():
    session.pop('user_id', None)
    return 'logout'

@app.route('/loan/<book_id>', methods=['POST'])
@auth_require
def loan_view(book_id):
        con = connect_db()
        cur = con.cursor()
        cur.execute('insert into LoanInfo(user_id,book_id) values(?,?)',(session['user_id'], book_id))
        con.commit()
        con.close()
        return '貸出処理しました!'

@app.route('/return', methods=['GET','Post'])
@auth_require
def return_book_view():
    con = connect_db()
    cur = con.cursor()
    cur.execute('delete from LoanInfo where user_id=?',(session['user_id'],))
    con.commit()

    return '返却処理しました!'


if __name__ == '__main__':
        app.run(debug=True)
