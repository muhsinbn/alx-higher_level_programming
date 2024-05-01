#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database}"
            )

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects
    cities = session.query(
            City, State).filter(City.state_id == State.id).order_by(City.id)

    # Print the City objects with their corresponding State names
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close session
    session.close()
