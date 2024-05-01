#!/usr/bin/python3
""" A module that contains a class definition of a State and an instance
Base = declarative_base()
class attr id that rep a column of auto gen, unique int, cant be null and
is a primary key
class attr name that rep a column of string with max 128 chars and not null
class attr cities rep a relationship with class City, if State object
is deleted: all linked City obj must be automatically deleted
Reference from a City object to his State must be named state
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """Represents a state for a MySQL database.
    ___table__(str); The name of the MySQL table to store states.
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
