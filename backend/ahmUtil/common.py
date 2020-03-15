

def resp(ok, result):
    r = '"success":"{}", "res":"{}"'.format(ok, result)
    r = '{' + r + '}'
    return r
