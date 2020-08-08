#!/usr/bin/python3
""" lists all state objects in database """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    newstate = State(name="Louisiana")
    session.add(newstate)
    print(session.query(State).filter_by(name='Louisiana').first().id)
    session.commit()

    session.close()
