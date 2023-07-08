import ipdb

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import (Base, Pet, Owner, Handler, Job)

#  ==============================================QUERY=============================================================


if __name__ == '__main__':

    # create an Engine to connect to the datbase
    egine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(egine)

    # create sessions and bind to the engine => object to Run Crud Queries Through
    Session = sessionmaker(bind=egine)
    session = Session()

    # ome to Many - Testing

    # Getting an Owners Pets
    first_owner = session.query(Owner).first()

    # get Owners pets from pet
    owners_pets = session.query(Pet).filter_by(id=first_owner.id)

    # print owners pet
    print([pet for pet in owners_pets])

    # Getting a pets owner
    # grab first pet
    first_pet = session.query(Pet).first()
    # get the owner assiciated with the pet
    pet_owner = session.query(Owner).filter_by(id=first_pet.owner_id)

    # print owner
    print([owner for owner in pet_owner])

    #  ============================================Many-Many===============================================================

    # get first handle
    first_handler = session.query(Handler).first()

    # grab the handler_job
    handler_jobs = session.query(Job).filter_by(id=first_handler.id)

    # print handlers_jobs
    print("=======this handler_job ==========")
    print([job for job in handler_jobs])

    #  ============================================dEBUG===============================================================
    ipdb.set_trace()
