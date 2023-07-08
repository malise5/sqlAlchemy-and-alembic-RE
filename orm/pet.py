import ipdb
import sqlite3


# creating connection to the database
CONN = sqlite3.connect("resources.db")

# setting the cursor accessing point
CURSOR = CONN.cursor()


# CREATING THE pet class
class Pet:
    def __init__(self, name, species, breed, temperament, id=None):
        self.id = id
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                breed TEXT,
                temperament TEXT
            );
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pets
        """
        CURSOR.execute(sql)

    # 3instance method
    def save(self):
        sql = """
            INSERT INTO pets(name, species, breed, temperament)
            VALUES(?,?,?,?)
        """
        CURSOR.execute(sql, (self.name, self.species,
                       self.breed, self.temperament))

    # save Database values using classmethod to combine instantiation and persistence
    @classmethod
    def create(cls, name, species, breed, temperament):
        # __init__ Method fires off
        pet = Pet(name, species, breed, temperament)
        pet.save()

        return pet

    # retrieve the newest input

    @classmethod
    def create_instance(cls, row):
        pet = Pet(
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4],
            id=row[0]
        )
        return pet

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM pets
        """
        # return CURSOR.execute(sql).fetchall()
        return [cls.create_instance(row) for row in CURSOR.execute(sql).fetchall()]

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM pets 
            WHERE name = ?
            LIMIT 1
        """
        row = CURSOR.execute(sql, (name, )).fetchone()

        if not row:
            return "Not found"

        return Pet(
            id=row[0],
            name=row[1],
            species=row[2],
            temperament=row[3],
        )

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM pets 
            WHERE id = ?
            LIMIT 1
        """
        row = CURSOR.execute(sql, (id, )).fetchone()

        if not row:
            return Pet.create_instance(row)

        return "Not found"

    @classmethod
    def find_or_create_by(cls, name=None, species=None, breed=None, temperament=None):
        sql = """
            SELECT * FROM pets 
            WHERE (name, species, breed, temperament) = (?,?,?,?)
            LIMIT 1
        """
        row = CURSOR.execute(
            sql, (name, species, breed, temperament)).fetchone()
        if not row:
            sql = """
                INSERT INTO pets(name, species, breed, temperament)
                VALUES(?,?,?,?)
            """

        return Pet.create_instance(row)

    def update(self):
        sql = """
            UPDATE pets
            WHERE name = ?,breed = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.breed, self.id))
