#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


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

    # Queries to List all City objects sorted by id
    cities = session.query(City).order_by(City.id).all()

    # Print results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close session
    session.close()
