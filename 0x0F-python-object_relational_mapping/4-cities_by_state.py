#!/usr/bin/python3
""" This script list all cities from the database "hbtn_0e_0_usa."""


import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MYSQL server
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to select all cities and sort them by id
    query = "SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query)

    # Fetch all rows
    cities = cursor.fetchall()

    # Print results
    for city in cities:
        print(city)

    # Close cursor and database connection
    cursor.close()
    db.close()
