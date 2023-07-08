from sqlalchemy import (PrimaryKeyConstraint, Column,
                        String, Integer, Float, Boolean, Date, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

# ====================================PET CLASS Table=====================================================


class Pet(Base):
    # set tables name
    __tablename__ = 'pets'
    __table_args__ = (PrimaryKeyConstraint('id'), )

    # set columns
    # id = Column(Integer, primary_key=True)
    id = Column(Integer())
    name = Column(String())
    species = Column(String())
    breed = Column(String())
    temperament = Column(String())
    # Add Foreign Key (owner's.id) to owner_id
    owner_id = Column(Integer(), ForeignKey('owners.id'))

    def __repr__(self):
        return f"""
            id: {self.id},
            Name: {self.name},
            Species: {self.species},
            Breed: {self.breed},
            Temperament: {self.temperament},
            Owner_Id: {self.owner_id}
        """

# =================================Owner Class Table=============================================================


class Owner(Base):
    __tablename__ = "owners"
    __table_args__ = (PrimaryKeyConstraint('id'), )

    id = Column(Integer())
    name = Column(String())
    email = Column(String())
    phone = Column(Integer())
    address = Column(String())
    # Associate the Pet model with the Owner Model
    # relationship('Pet', backref=backref('pet'))
    pets = relationship('Pet', backref=backref('pet'))

    def __repr__(self):
        return f"""
            id: {self.id},
            Name: {self.name},
            Email: {self.email},
            Phone: {self.phone},
            Address: {self.address}
        """

    # run => 'alembic revision --autogenerate -m "added table"
    # run => alembic upgrade head
