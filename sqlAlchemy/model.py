from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pet(Base):
    # set tables name
    __tablename__ = 'pets'
    __table_args = (PrimaryKeyConstraint('id'), )

    # set columns
    id = Column(Integer, primary_key=True)
    name = Column(String())
    species = Column(String())
    breed = Column(String())
    temperament = Column(String())
    owner_id = Column(Integer())

    def __repr__(self):
        return f"""
            id: {self.id},
            Name: {self.name},
            Species: {self.species},
            Breed: {self.breed},
            Temperament: {self.temperament},
            Owner_Id: {self.owner_id}
        """
