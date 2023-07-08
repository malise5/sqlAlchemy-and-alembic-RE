import random
from faker import Faker

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Pet, Owner

if __name__ == '__main__':

    # create an Engine to connect to the datbase
    egine = create_engine('sqlite:///pet_app.db')

    # create sessions and bind to the engine => object to Run Crud Queries Through
    Session = sessionmaker(bind=egine)
    session = Session()
