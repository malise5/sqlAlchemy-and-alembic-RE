import ipdb


class Owner:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nPhone Number: {self.phone_number}"


# class Owner:
#     def __init__(self, age):
#         self.age = age

#     def __str__(self):
#         return f"""
#         Pet Owner: {self.age}
#         """

#     def get_name(self):
#         print("retreive owner's name")
#         return self._name

#     def set_name(self, name):
#         print("setting owner's name")
#         if (isinstance(name, str)):
#             self._name = name
#         else:
#             print("Name must be a string")

#     name = property(get_name, set_name)


# ipdb.set_trace()
