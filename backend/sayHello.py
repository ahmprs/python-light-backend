#!C:\Users\elipsa\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-

from ahmUtil.http_header import putHttpRespHeaders
from ahmUtil.common import resp
from ahmUtil.session import setSessionVal, getSessionVal, registerNewSession, forget

# put an http response header for json compliance
putHttpRespHeaders()
# print(resp(1,  'Hi'))


# session_name = getCookie('session_name')
registerNewSession()
setSessionVal('height', '180')
setSessionVal('height', '181')
forget()
d = getSessionVal('height')

print(resp(1,  d))
