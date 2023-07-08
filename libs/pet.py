import ipdb


class Pet:
    total_pets = 0

    def __init__(self, name, age, breed, temperament):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        Pet.pet_increased()

    def __str__(self):
        return f'''
            name: {self.name}
            Age: {self.age}
            Breed: {self.breed}
            Temperament: {self.temperament}
        '''

    def details(self):
        print(f'''
            name: {self.name}
            Age: {self.age}
            Breed: {self.breed}
            Temperament: {self.temperament}
        ''')

    @classmethod
    def pet_increased(cls):
        cls.total_pets += 1
        print("New pet added")


# ipdb.set_trace()
