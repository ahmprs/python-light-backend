import os
import time
import hashlib

from datetime import datetime


def getHash(str):
    result = hashlib.sha1(str.encode())
    return result.hexdigest()


def getCookie(key):

    si = ''
    try:
        cs = os.environ["HTTP_COOKIE"]

        if (cs == None):
            return ""

        if (cs == ''):
            return ""

        s = cs.index(key)
        if (s == -1):
            return ""

        ln = len(cs)
        k = s + len(key) + 1
        while (True):
            if (k >= ln):
                break
            if (cs[k] == ' '):
                break
            if (cs[k] == ';'):
                break
            si = si + cs[k]
            k = k + 1
    except:
        si = ''
    finally:
        return si


def setCookie(key, val):
    print("Set-Cookie: {0}={1}".format(key, val))


def putHttpRespHeaders():

    print("Content-type: application/json")

    # assign a session id only if it is not set yet
    session_name = getCookie('session_name')
    if(session_name == ''):
        ts = datetime.now()
        seed = ts.strftime("%M:%S.%f")
        session_name = getHash(seed)
        setCookie('session_name', session_name)

    print()
