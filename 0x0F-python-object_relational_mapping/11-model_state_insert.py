#!/usr/bin/python3
"""
A script that adds the  State object "Louisiana" to the database hbtn_0e_6_usa
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

    # Create a new State object
    new = State(name="Louisiana")

    # Add the new State object to the session and commit the transaction
    session.add(new)
    session.commit()

    # Print the new state's id
    print(new.id)

    # Close session
    session.close()
