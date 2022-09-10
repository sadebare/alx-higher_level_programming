#!/usr/bin/python3
"""
write a script 14-model_city_fetch_by_state.py that
prints all City objects from the database hbtn_0e_14_usa:
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base
from model_city import City

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    rows = session.query(City, State).filter(City.state_id == State.id)\
                                     .order_by(City.id).all()
    for city, state in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
