import mysql.connector

# IMPORTANT: KEEP THE FOLLOWING SECRET
_host = "localhost"
_user = "root"
_passwd = ""
_database = "db_test_1"
# ------------------------------------


def select(sql):
    # connect to database
    db = mysql.connector.connect(
        host=_host,
        user=_user,
        passwd=_passwd,
        database=_database
    )

    # acquire a cursor
    cur = db.cursor()

    # run a select query
    cur.execute(sql)

    # fetch all records
    rec_set = cur.fetchall()

    return rec_set


# INSERT INTO tbl_books (book_title, book_author, book_price) VALUES (%s, %s, %s)
# val = ("My Book", "Me", "100")
def insert(sql, val):
    # connect to database
    db = mysql.connector.connect(
        host=_host,
        user=_user,
        passwd=_passwd,
        database=_database
    )

    # acquire a cursor
    cur = db.cursor()

    # execute the sql
    inserted_rows_count = cur.execute(sql, val)

    # commit the transaction
    db.commit()

    return (cur.lastrowid, inserted_rows_count)

# sql = "UPDATE tbl_books SET book_price = %s WHERE book_id = %s"
# val = ("120.5", "6")


def update(sql, val):

    # connect to database
    db = mysql.connector.connect(
        host=_host,
        user=_user,
        passwd=_passwd,
        database=_database
    )

    # acquire a cursor
    cur = db.cursor()

    # execute the sql
    cnt = cur.execute(sql, val)

    # commit the transaction
    db.commit()

    return cnt


# sql = "DELETE FROM tbl_books WHERE book_id = %s"
# val = ("6",)
def delete(sql, val):
    # connect to database
    db = mysql.connector.connect(
        host=_host,
        user=_user,
        passwd=_passwd,
        database=_database
    )

    # acquire a cursor
    cur = db.cursor()

    # execute the sql
    cur.execute(sql, val)

    # commit the transaction
    db.commit()
