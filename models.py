
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import Bcrypt  # Import the bcrypt module

db = SQLAlchemy()
bcrypt = Bcrypt()

# # =========================================Production=============================================

# Production Table


class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"  # Table name for the Production model

    # Primary key column for the Production table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)  # Column for storing the production's title
    genre = db.Column(db.String)  # Column for storing the production's genre
    budget = db.Column(db.Float)  # Column for storing the production's budget
    image = db.Column(db.String)  # Column for storing the production's image
    # Column for storing the production's director
    director = db.Column(db.String)
    # Column for storing the production's description
    description = db.Column(db.String)
    # Column indicating if the production is ongoing
    ongoing = db.Column(db.Boolean)
    # Column for storing the creation timestamp
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(
    ), onupdate=db.func.now())  # Column for storing the update timestamp

    # Relationship with the CastMember model
    cast_members = db.relationship('CastMember', backref='production')
    # Serialization rules for the Production model
    serialize_rules = ('-cast_members.production',
                       '-created_at', '-updated_at')

    @validates('image')
    def validates_image(self, key, image_path):
        # Validation for the image path to ensure it is a .jpg file
        if '.jpg' not in image_path:
            raise ValueError("Image must be a .jpg")
        return image_path

    def __repr__(self):
        return f"""
            Id: {self.id},
            Title: {self.title},
            Genre: {self.genre},
            Budget: {self.budget},
            Image: {self.image},
            Director: {self.director},
            Description: {self.description},
            Ongoing: {self.ongoing},
            Create At: {self.created_at},
            Updated At: {self.updated_at}
        """

# # =========================================CastMember=============================================


# CastMember Table

class CastMember(db.Model, SerializerMixin):
    __tablename__ = 'cast_members'  # Table name for the CastMember model

    # Primary key column for the CastMember table
    id = db.Column(db.Integer, primary_key=True)
    # Column for storing the cast member's name
    name = db.Column(db.String, nullable=False)
    # Column for storing the cast member's role
    role = db.Column(db.String, nullable=False)
    # Column for storing the creation timestamp
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(
    ), onupdate=db.func.now())  # Column for storing the update timestamp
    # Foreign key column referencing the Production table
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
    # Serialization rules for the CastMember model
    serialize_rules = ('-production.cast_members',
                       '-created_at', '-updated_at')

    def __repr__(self):
        return f"""
            Id: {self.id},
            Name: {self.name},
            Role: {self.role},
            Production_id: {self.production_id}
        """

# # =========================================User=============================================


# User Table

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'  # Table name for the User model

    # Primary key column for the User table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)  # Column for storing the user's name
    email = db.Column(db.String)  # Column for storing the user's email address
    # Column for storing the hashed password (treated as a private attribute)
    _password_hash = db.Column(db.String)
    # Column indicating if the user has admin privileges
    admin = db.Column(db.Boolean, default=False)

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        # Generate and set the password hash based on the provided password
        # Convert the password to a string if it's an integer
        password_str = str(password)
        password_hash = bcrypt.generate_password_hash(
            password_str.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        # Check if the provided password matches the stored password hash
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    def __repr__(self):
        return f"""
            Id: {self.id},
            Name: {self.name},
            Email: {self.email},
            Admin: {self.admin}
        """


# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy_serializer import SerializerMixin


# # import validates from sqlalchemy.orm
# from sqlalchemy.orm import validates

# # instantiate sqlalchemy
# db = SQLAlchemy()

# # Production Table

# # =========================================Production=============================================


# class Production(db.Model, SerializerMixin):
#     __tablename__ = "productions"

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     genre = db.Column(db.String)
#     budget = db.Column(db.Float)
#     image = db.Column(db.String)
#     director = db.Column(db.String)
#     description = db.Column(db.String)
#     ongoing = db.Column(db.Boolean)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(
#         db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

#     cast_members = db.relationship('CastMember', backref='production')
#     # serialize_only = ('title',)
#     serialize_rules = ('-cast_members.production',
#                        '-created_at', '-updated_at')

#     # create a validation for images
#     @validates('image')
#     def validates_image(self, key, image_path):
#         if '.jpg' not in image_path:
#             raise ValueError("Image must be a .jpg")
#         return image_path

#     def __repr__(self):
#         return f"""
#             Id: {self.id},
#             Title: {self.title},
#             Genre: {self.genre},
#             Budget: {self.budget},
#             Image: {self.image},
#             Director: {self.director},
#             Description: {self.description},
#             Ongoing: {self.ongoing},
#             Create At: {self.created_at},
#             Updated At: {self.updated_at}
#         """

# # =========================================CastMember=============================================


# class CastMember(db.Model, SerializerMixin):
#     __tablename__ = 'cast_members'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     role = db.Column(db.String, nullable=False)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(
#         db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
#     production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
#     # production = db.relationship('Production', backref=db.backref('cast_members', lazy=True))
#     # serialize_only = ('name',)
#     serialize_rules = ('-production.cast_members',
#                        '-created_at', '-updated_at')

#     def __repr__(self):
#         return f"""
#             Id: {self.id},
#             Name:{self.name},
#             Role:{self.role},
#             Production_id:{self.production_id}
#         """


# class User(db.Model, SerializerMixin):
#     __tablename__ = 'users'  # The name of the database table for the User model

#     # Primary key column for the User table
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)  # Column for storing the user's name
#     email = db.Column(db.String)  # Column for storing the user's email address
#     # Column for storing the hashed password (treated as a private attribute)
#     _password_hash = db.Column(db.String)
#     # Column indicating if the user has admin privileges
#     admin = db.Column(db.Boolean, default=False)

#     @hybrid_property
#     def password_hash(self):
#         return self._password_hash

#     @password_hash.setter
#     def password_hash(self, password):
#         # Generate and set the password hash based on the provided password
#         password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
#         self._password_hash = password_hash.decode('utf-8')

#     def authenticate(self, password):
#         # Check if the provided password matches the stored password hash
#         return bcrypt.check_password(self._password_hash, password.encode('utf-8'))

#     def __repr__(self):
#         # Return a string representation of the User object
#         return f"""
#             Id: {self.id},
#             Name: {self.name},
#             Email: {self.email},
#             Admin: {self.admin},
#         """
