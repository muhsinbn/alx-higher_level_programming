#!/usr/bin/python3
""" A script that takes in an argument and displays all values in the `states`
table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to select states with matching name
    q = "SELECT * FROM `states` WHERE BINARY `name` = '{}'".format(sys.argv[4])
    cursor.execute(q)

    # Fetch all rows
    states = cursor.fetchall()

    # Print results
    for state in states:
        print(state)

    # Close cursor and database
    cursor.close()
    db.close()
