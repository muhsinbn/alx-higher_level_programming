#!/usr/bin/python3
""" A script that takes in the name of a state as an argument and list all
cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    state_name = sys.argv[4]
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to select states with matching name
    q = "SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(q, (state_name,))

    # Fetch all rows
    cities = cursor.fetchall()

    # Concatenates city names
    city_names = ", ".join(city[0] for city in cities)

    # Print results
    print(city_names)

    # Close cursor and database
    cursor.close()
    db.close()
