#!/usr/bin/python3
"""
Write a script that creates the State
“California” with the City “San Francisco”from
the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    cali = State(name="California")
    cali.cities = [City(name="San Francisco")]
    session.add(cali)
    session.commit()
    session.close()
