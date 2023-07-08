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


# =================================Handler Class Table=============================================================
# Many to Many Association

# Pet-< Jobs >- Handlers


class Handler(Base):
    __tablename__ = "handlers"
    __table_args__ = (PrimaryKeyConstraint('id'), )

    id = Column(Integer())
    name = Column(String())
    email = Column(String())
    phone = Column(Integer())
    hourly_rate = Column(Float())

    def __repr__(self):
        return f"""
            id: {self.id},
            Name: {self.name},
            Email: {self.email},
            Phone: {self.phone},
            Hourly_rate: {self.hourly_rate}
        """

# =================================Job Class Table=============================================================
# Many to Many Association

# Pet-< Jobs >- Handlers


class Job(Base):
    __tablename__ = "jobs"
    __table_args__ = (PrimaryKeyConstraint('id'), )

    id = Column(Integer())
    request = Column(String())
    data = Column(Date())
    notes = Column(String())
    fee = Column(Float())
    pet_id = Column(Integer(), ForeignKey('pets.id'))
    handler_id = Column(Integer(), ForeignKey('handlers.id'))

    # Association the models relationship (NodelHere, backref=backref(tableName))
    pet = relationship("Pet", backref=backref("pets"))
    handler = relationship("Handler", backref=backref("handlers"))

    def __repr__(self):
        return f"""
            id: {self.id},
            Request: {self.request},
            Data: {self.data},
            Pet_id: {self.pet_id},
            Handler_id: {self.handler_id}
        """
