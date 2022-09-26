#!/usr/bin/python3
'''
Module to list all states starting with N from database hbtn_0e_0_usa
'''


if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    st = sys.argv[4]
    to = "SELECT * FROM states WHERE BINARY name='{}'\
         ORDER BY id ASC".format(st)
    cur.execute(to)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
