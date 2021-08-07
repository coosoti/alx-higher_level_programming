#!/usr/bin/python3
"""
This script lists all cities from the database that are in a specified state
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]
    cities = []

    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states ON cities.state_id = states.id
    WHERE states.name=%s
    ORDER BY id ASC""", (state,))

    rows = cur.fetchall()
    for row in rows:
        cities.append(row[1])
    print(', '.join(cities))
    cur.close()
    db.close()
