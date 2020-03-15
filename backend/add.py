#!C:\Users\elipsa\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-

from ahmUtil.common import resp
from ahmUtil.http_header import putHttpRespHeaders
from ahmUtil.http import Http

putHttpRespHeaders()

# grab parameters
http = Http()
x = http.getPostArgAsInt('x', 0)
y = http.getPostArgAsInt('y', 0)

# do logics
z = x + y

# send back response
print(resp(1, z))
