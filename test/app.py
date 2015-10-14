#!/bin/python3
# coding: UTF-8

import hashlib
import time

salt = str(time.time())
passwd = 'pass'
text=(passwd+salt).encode('utf-8')

result = hashlib.sha512(text).hexdigest()
print(result)
