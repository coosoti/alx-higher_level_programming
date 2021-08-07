#!/usr/bin/python3

"""
This script lists all cities from the database in ascending order by id
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states ON cities.state_id = states.id
    ORDER BY id ASC""")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
