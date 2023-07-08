import ipdb

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import (Base, Pet)


if __name__ == '__main__':

    # create an Engine to connect to the datbase
    egine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(egine)

    # create sessions and bind to the engine => object to Run Crud Queries Through
    Session = sessionmaker(bind=egine)
    session = Session()

    # ✅ CREATE
    rose = Pet(name="rose", species="cat", breed="domestic longhair",
               temperament="relaxed", owner_id=1)
    spot = Pet(name="spot", species="dog", breed="german-shepherd",
               temperament="playful", owner_id=1)
    scooby = Pet(name="scooby", species="rabbit", breed="belgium-knight",
                 temperament="mischevious", owner_id=1)

    # session.add(rose)
    # session.add(spot)
    # session.add(scooby)
    session.bulk_save_objects([rose, spot, scooby])
    session.commit()

    # 🐪 Read
    # retrieving all Pets
    pets = session.query(Pet)
    # prints all the pets
    print([pet for pet in pets])
    # print all the names
    names = [name.name for name in pets]
    print(names)

    # filter by temparemnt wirh session.query and filter
    filter_by_temperament = session.query(
        Pet).filter(Pet.temperament.like("%relaxed%"))

    # 🔼 UPDATE

    ipdb.set_trace()
