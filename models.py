from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

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
    serialize_rules = ('-cast_members.production', )

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
    name = db.Column(db.String)
    role = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
    # production = db.relationship('Production', backref=db.backref('cast_members', lazy=True))
    serialize_rules = ('-production.cast_members', )

    def __repr__(self):
        return f"""
            Id: {self.id}, 
            Name:{self.name}, 
            Role:{self.role}, 
            Production_id:{self.production_id}
        """
