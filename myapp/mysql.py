import sqlite3
def connect(sql):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    res = c.execute(sql)
    # conn.commit()
    # conn.close()
    return res