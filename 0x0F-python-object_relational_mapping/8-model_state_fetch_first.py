#!/usr/bin/python3
"""
A script that prints the first State object from the database hbtn_0e_6_usa
if the table states is empty, print Nothing followed by newline
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database}"
            )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object and print its details
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close session
    session.close()
