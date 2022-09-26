#!/usr/bin/python3
'''
Module to list all cities from database hbtn_0e_0_usa
'''


if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                 FROM cities JOIN states ON cities.state_id = states.id\
                 ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
