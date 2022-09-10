#!/usr/bin/python3
"""
Write a script that lists all State objects,
and corresponding City objects, contained in the database hbtn_0e_101_usa
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
    rows = session.query(City).all()
    for city in rows:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
