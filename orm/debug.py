from owner import Owner, CONN, CURSOR
from pet import Pet, CONN, CURSOR
import ipdb


# Owner.create_table()
# frank=Owner("frank", "555-555-555", "frank@gmail.com", "555-Somwhere")
# frank.save()

Pet.create_table()
spot = Pet("spot", "dog", "chihuahua", "feisty")
rex = Pet("rex", "dog", "chihuahua", "chill")
grace = Pet("grace", "cat", "chihuahua", "funny")

spot.save()
rex.save()
grace.save()

ipdb.set_trace()
