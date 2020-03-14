#!C:\Users\elipsa\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-

import cgi


def add(x, y):
    return x+y


def mul(x, y):
    return x*y


def onSuccess(res):
    r = '"success":"true", "res":"{}"'.format(res)
    r = '{' + r + '}'
    return r


def onFailure(err):
    r = '"success":"false", "err":"{}"'.format(err)
    r = '{' + r + '}'
    return r


print("Content-type: application/json")
print()

form = cgi.FieldStorage()
x = form.getvalue("x")
y = form.getvalue("y")
func = form.getvalue("func")
z = 0

try:
    x = int(x)
    y = int(y)
    pass
except Exception as ex:
    print(onFailure('BAD PARAMETERS '))
    pass
else:
    if(func == 'add'):
        z = add(x, y)
        print(onSuccess(z))
    elif(func == 'mul'):
        z = mul(x, y)
        print(onSuccess(z))
    else:
        print(onFailure('UNSUPPORTED FUNCTION'))
