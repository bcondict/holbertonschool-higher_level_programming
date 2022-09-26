#!/usr/bin/python3
'''
Add Louisiana to hbtn_0e_6_usa state's table
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

    state_to_change = session.query(State).get(2)
    state_to_change.name = "New Mexico"

    session.add(state_to_change)
    session.commit()

    session.close()
