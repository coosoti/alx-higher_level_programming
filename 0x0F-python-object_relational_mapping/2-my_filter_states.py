#!/usr/bin/python3

"""
This script selects states that match a user input
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(name)

    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        if row[1] == name:
            print(row)
    cur.close()
    db.close()
