#!C:\Users\elipsa\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-

from ahmUtil import common

# capture http arguments
http = common.Http()

# put an http response header for json compliance
# Content-type: application/json
common.putHttpRespHeaders()

# grab parameters
x = http.getPostArgAsInt('x', 0)
y = http.getPostArgAsInt('y', 0)

# do logics
z = x + y

# send back response
print(common.resp(1, z))
