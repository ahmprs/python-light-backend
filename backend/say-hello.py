#!C:\Users\elipsa\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-

import cgi


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
print(onSuccess("HELLO FROM PYTHON BACK-END"))
