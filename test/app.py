#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sqlite3 import connect,Row

con = connect('test.db')
#取得する形式をディクショナリに
con.row_factory = Row

cur = con.cursor()
cur.execute('select * from Books')
books = cur.fetchall()
for book in books:
    print(book['name']+"の価格は"+str(book['price'])+"です")
