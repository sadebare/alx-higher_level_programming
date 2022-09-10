#!/usr/bin/python3
"""
Write a script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""

from ast import arg
from re import S
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
    s = '%a%'
    delete_state = session.query(State).filter(State.name.like(s))
    for state in delete_state:
        session.delete(state)
    session.commit()
    session.close()
