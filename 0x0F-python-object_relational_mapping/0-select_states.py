import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of argument are provided
    if len(sys.arg) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name")
        sys.exit(1)

        # Get MySQL username, password, and database name from the argument
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # Connect to the MySQL server and retrieve states data
        db = MySQLdb.connect(host="localhost", port=3306, user=username passwd=password, db=database)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()

        # Display the states data
        for state in states:
            print(state)

            # Close cursor and database connection
            cursor.close()
            db.close()
