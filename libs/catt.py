import ipdb


from pet import *


class Cat(Pet):
    def __init__(self, name, age, breed, temperament, indoor):
        super().__init__(name, age, breed, temperament)
        self.indoor = indoor

    # def __str__(self):
    #     return f'''
    #         Name: {self.name}
    #         Age: {self.age}
    #         Breed: {self.breed}
    #         Temperament: {self.temperament}
    #         Indoor: {self.indoor}
    #     '''

    def cat_details(self):
        # print(f'''
        #     Name: {self.name}
        #     Age: {self.age}
        #     Breed: {self.breed}
        #     Temperament: {self.temperament}
        #     Indoor: {self.indoor}
        # ''')
        super().details()
        print(f'''
          Indoor: {self.indoor}
        ''')


# Uncomment this line to create the cat instance
# cat = Cat("Grace", 5, "Sise", "Cool", True)
ipdb.set_trace()
