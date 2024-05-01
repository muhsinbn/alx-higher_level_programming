#!/usr/bin/python3
"""
A script that deletes all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
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

    # Query State objects that contain the letter 'a'
    states_a = session.query(
            State).filter(State.name.like('%a%')).all()

    # Deletes the State objects from the session
    for state in states_a:
        session.delete(state)

    # Commit the transaction
    session.commit()

    # Close session
    session.close()
