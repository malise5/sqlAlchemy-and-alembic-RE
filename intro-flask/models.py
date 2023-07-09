from flask_sqlalchemy import SQLAlchemy

# instantiate sqlalchemy
db = SQLAlchemy()

# Production Table

# =========================================Production=============================================


class Production(db.Model):
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
