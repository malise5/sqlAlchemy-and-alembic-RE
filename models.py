from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# import validates from sqlalchemy.orm
from sqlalchemy.orm import validates

# instantiate sqlalchemy
db = SQLAlchemy()

# Production Table

# =========================================Production=============================================


class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    cast_members = db.relationship('CastMember', backref='production')
    # serialize_only = ('title',)
    serialize_rules = ('-cast_members.production',
                       '-created_at', '-updated_at')

    # create a validation for images
    @validates('image')
    def validates_image(self, key, image_path):
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

# =========================================CastMember=============================================


class CastMember(db.Model, SerializerMixin):
    __tablename__ = 'cast_members'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
    # production = db.relationship('Production', backref=db.backref('cast_members', lazy=True))
    # serialize_only = ('name',)
    serialize_rules = ('-production.cast_members',
                       '-created_at', '-updated_at')

    def __repr__(self):
        return f"""
            Id: {self.id}, 
            Name:{self.name}, 
            Role:{self.role}, 
            Production_id:{self.production_id}
        """
