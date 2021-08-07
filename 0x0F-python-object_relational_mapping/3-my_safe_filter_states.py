#!/usr/bin/python3

"""
This script selects states based on user input while avoiding SQL injection
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]
    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
