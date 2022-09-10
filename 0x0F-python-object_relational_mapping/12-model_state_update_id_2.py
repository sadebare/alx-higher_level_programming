#!/usr/bin/python3
"""
Write a script that changes the name of
a State object from the database hbtn_0e_6_usa
"""

from ast import arg
from unicodedata import name
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    change_state = session.query(State).filter(State.id == 2).first()
    change_state.name = "New Mexico"
    session.commit()
    session.close()
