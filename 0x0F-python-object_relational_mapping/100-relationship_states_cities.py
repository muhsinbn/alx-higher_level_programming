#!/usr/bin/python3
"""
A script that creates the  State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    # Create engine to connect to MySQL server
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
            )

    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State and City
    new_state = City(name="San Francisco", state=State(name="California"))

    # Add the new State and City to the session and commit the transaction
    session.add(new_state)

    session.commit()

    # Close session
    session.close()
