#!C:\Users\elipsa\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-

from ahmUtil.common import putHttpRespHeaders, resp


# put an http response header for json compliance
# Content-type: application/json
putHttpRespHeaders()


# send back response
print(resp(1, "Hello from python back-end"))
