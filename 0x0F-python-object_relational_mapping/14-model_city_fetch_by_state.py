#!/usr/bin/python3
'''
List all cities from hbtn_0e_14_usa
'''


if __name__ == "__main__":
    from model_city import City
    from model_state import Base, State
    from sqlalchemy import create_engine, MetaData
    from sqlalchemy.orm import Session
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    engine.connect()

    metadata = MetaData()

    session = Session(engine)

    for city in session.query(City).order_by(City.id).all():
        state = session.query(State).get(city.state_id)
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
