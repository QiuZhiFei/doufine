# encoding: utf-8

import MySQLdb


def execute(cmd):
    db = MySQLdb.connect("127.0.0.1", "root", "", "doufine", charset='utf8')
    cursor = db.cursor()

    res = None

    try:
        cursor.execute(cmd)
        db.commit()
    except:
        db.rollback()
    
    # res = cursor.fetchall()

    db.close()

    return cursor
    # res = cursor.fetchall()

    # return res