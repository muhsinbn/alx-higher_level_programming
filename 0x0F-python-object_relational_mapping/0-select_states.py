import sys
import MySQLdb

def list_states(username, password, database):
    with MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database) as db:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM states ORDER BY id ASC")
            states = cursor.fetchall()

            for state in states:
                print(state)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
