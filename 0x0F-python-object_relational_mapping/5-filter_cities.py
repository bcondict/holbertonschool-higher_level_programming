#!/usr/bin/python3
'''
Module to list all cities from database hbtn_0e_0_usa
'''


if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    st = sys.argv[4].split('\'')
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                 FROM cities JOIN states ON cities.state_id = states.id\
                 WHERE states.name='{}'\
                 ORDER BY cities.id ASC".format(st[0]))
    query_rows = cur.fetchall()
    for i in range(0, len(query_rows)):
        if i < (len(query_rows) - 1):
            print(query_rows[i][0], end=", ")
        else:
            print(query_rows[i][0], end="")
    print()
    cur.close()
