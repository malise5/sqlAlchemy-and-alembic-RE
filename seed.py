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

    # Add delete methods to clear in tables
    session.query(Pet).delete()
    session.query(Owner).delete()

    # Intialize faker
    faker = Faker()

    # create list of species with "cat" and "Dog"
    species = ["cat", "Dog"]

    # create a list of cats breeds
    cat_breeds = ["Domestic skunk", "Siamse", "Kature", "Lencho"]

    # create a list of dogs breeds
    dog_breeds = ["husky", "Shepherd", "Bulldog", "sare"]

    # create a list of temperaments
    temperaments = ["freizy", "Calm", "Navous", "Mischevious"]

    # create a list of owners
    owners = []

    # create a loop that itarates 50 times
    for _ in range(50):
        # 3creating Owner
        owner = Owner(
            name=f"{faker.first_name()} {faker.last_name()}",
            email=faker.email(),
            phone=random.randint(1000000000, 9999999999),
            address=faker.address()
        )
        # commit and save owner one at a time so we maintain the owner Id
        session.add(owner)
        session.commit()

        # Append to owners
        owners.append(owner)

    # create empty pets array
    pets = []

    # 3create a loop that iterates over the owners
    for owner in owners:
        # create a for loop that iterates 1 - 3 times
        for _ in range(random.randint(1, 3)):
            # use faker and the species, cat breeds, dog breeds and temperament list to create a pet
            rand_species = random.choice(species)

            pet = Pet(
                name=faker.name(),
                species=rand_species,
                breed=random.choice(
                    cat_breeds) if rand_species == "cat" else random.choice(dog_breeds),
                temperament=random.choice(temperaments),
                owner_id=owner.id
            )
            # commit and save pet
            session.add(pet)
            session.commit()

            # Append to pets
            pets.append(pet)

    session.commit()
    session.close()
