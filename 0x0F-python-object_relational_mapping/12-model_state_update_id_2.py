#!/usr/bin/python3
"""
A script that changes the name of State object from the database hbtn_0e_6_usa
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

    # Query the State object with id = 2
    update_state = session.query(State).filter_by(id=2).first()

    if update_state:
        # Update the name of the State object
        update_state.name = "New Mexico"

        # Commit the transaction
        session.commit()

        print("Success")
    else:
        print("Nothing")

    # Close session
    session.close()
