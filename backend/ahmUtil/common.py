
import cgi


def resp(ok, result):
    r = '"success":"{}", "res":"{}"'.format(ok, result)
    r = '{' + r + '}'
    return r


def putHttpRespHeaders():
    print("Content-type: application/json")
    print()


class Http:
    def __init__(self):
        self.form = cgi.FieldStorage()

    def getPostArg(self, key):
        val = self.form.getvalue(key)
        return val

    def getPostArgAsInt(self, key, default=0):
        val = self.getPostArg(key)
        d = 0
        try:
            d = int(val)
            pass
        except Exception:
            d = default
        return d
