#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sqlite3 import connect,Row

con = connect('test.db')
cur = con.cursor()
cur.execute('insert into Books(name,price) values("test",500)')
con.commit()
