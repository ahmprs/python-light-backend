from ahmUtil.mysql_db import insert, select, update, delete
from ahmUtil.http_header import getCookie


def forget():
    session_name = getCookie('session_name')
    if (session_name == ''):
        return

    sql = "delete from tbl_sessions where session_name = '{0}';".format(
        session_name)
    delete(sql, None)


def getSessionId(sessionName):

    sql = "select session_id from tbl_sessions where session_name = '{0}'".format(
        sessionName)

    recs = select(sql)

    if (len(recs) > 0):
        return recs[0][0]
    return ""


# returns session_id
def registerNewSession():

    session_name = getCookie('session_name')

    # if the session already exists, return its id
    session_id = getSessionId(session_name)
    if (session_id != ''):
        return session_id

    # make a sha128 hash string for session name
    sql = "INSERT INTO `tbl_sessions`(`session_id`, `session_name`, `session_active`, `session_desc`) VALUES(NULL, '{0}', '1', '');".format(
        session_name)

    (id, cnt) = insert(sql, None)

    # if the new session was not succeeded
    if (cnt == 0):
        return ""

    return id


def getSessionVal(key):
    session_name = getCookie('session_name')
    if (session_name == ""):
        return ''

    id = getSessionId(session_name)
    if (id == ''):
        return ""

    sql = "select * from tbl_session_data where session_id = '{0}' and session_key = '{1}';".format(
        id, key)
    recs = select(sql)
    if (len(recs) <= 0):
        return ""

    return recs[0][3].decode()


def setSessionVal(key, val):
    session_name = getCookie('session_name')
    if (session_name == ""):
        return ''

    id = getSessionId(session_name)

    if (id == ''):
        return ""

    sql = "select * from tbl_session_data where session_id = '{0}' and session_key = '{1}';".format(
        id, key)

    recs = select(sql)
    if (len(recs) > 0):
        sql = "update tbl_session_data set session_val = '{0}' where session_id = '{1}' and session_key = '{2}'; ".format(
            val, id, key)

        update(sql, None)

        return ""
    else:
        sql = "INSERT INTO `tbl_session_data`(`session_data_id`,`session_id`,`session_key`, `session_val`) VALUES(NULL, '{0}', '{1}', '{2}')".format(
            id, key, val)

        insert(sql, None)
        return ""
    return ""
