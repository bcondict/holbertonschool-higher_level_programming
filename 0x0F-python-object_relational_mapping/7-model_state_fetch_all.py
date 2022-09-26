#!/usr/bin/python3
'''
List all states from hbtn_0e_6_usa
'''


if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine, MetaData
    from sqlalchemy.orm import Session
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    engine.connect()

    metadata = MetaData()

    session = Session(engine)

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()
