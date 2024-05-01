#!/usr/bin/python3
"""
A module that contains a class definition of City and inherits from base
class attr id that rep column of auto gen, unique int, not null and pri key
class attr name that rep column of string 128 max and not null
class attr state_id that rep column of an int, not null and foreign key to
states.id
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

Base = declarative_base()


class City(Base):
    """Represents a City for a MySQL database.
    ___table___(str): The name of the MySQL table to store cities
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
