DROP TABLE owners;
CREATE TABLE owners(
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    email TEXT,
    phone INTEGER
);

DROP TABLE pets;
CREATE TABLE pets(
    id INTEGER PRIMARY KEY,
    owner_id INTEGER,
    name TEXT,
    birthdate DATETIME,
    breed TEXT,
    favorite_treats TEXT,
    lats_fed_at DATETIME,
    FOREIGN KEY (owner_id) REFERENCES owners(id)
);

ALTER TABLE pets
ADD COLUMN image_url TEXT;

-- Insert data into the owners table
INSERT INTO owners (name, address, email, phone)
VALUES ('John Doe', '123 Main St', 'john.doe@example.com', '1234567890');

INSERT INTO owners (name, address, email, phone)
VALUES ('Kudez', '103 linet St', 'kude.doe@example.com', '07034750123');

-- Insert data into the pets table
INSERT INTO pets (owner_id, name, birthdate, breed, favorite_treats,image_url, lats_fed_at)
VALUES (1, 'Fluffy', '2019-05-15', 'Dog', 'Bones','image.jpg', '2023-07-06');

INSERT INTO pets (owner_id, name, birthdate, breed, favorite_treats,image_url, lats_fed_at)
VALUES (2, 'Bob', '2019-05-25', 'Cat', 'Crisp','image.jpg', '2023-07-06');

--reading CRUD

SELECT * FROM pets
WHERE name = 'Bob';