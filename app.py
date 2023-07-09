# 🤪  setUp Imports

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate

from flask_restful import Api, Resource

from models import db, Production, CastMember

# 🤪  Intialize the App
app = Flask(__name__)

# 🤪  setUp database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False  # configures JSON response to print Indented lines

# 🤪  setUp migration and initialize instance with 'db.init)app(app)
migrate = Migrate(app, db)
db.init_app(app)

# 🤪  initialize Api
api = Api(app)

# =========================================Productions Routes=============================================


class Productions(Resource):
    def get(self):
        # production_list = [{
        # "title": production.title,
        # "genre": production.genre,
        # "Budget": production.budget,
        # "Image": production.image,
        # "Director": production.director,
        # "director": production.director,
        # "Description": production.description,
        # "Ongoing": production.ongoing,
        # } for production in Production.query.all()]
        production_list = [production.to_dict()
                           for production in Production.query.all()]

        response = make_response(
            {"data_length": len(production_list),
             "data": production_list}, 200
        )
        return response

    def post(self):
        # gets the input from the client
        request_json = request.get_json()
        new_production = Production(
            title=request_json['title'],
            genre=request_json['genre'],
            budget=request_json['budget'],
            image=request_json['image'],
            director=request_json['director'],
            description=request_json['description'],
            ongoing=request_json['ongoing'],
        )
        db.session.add(new_production)
        db.session.commit()

        # convert it into dictionary
        response_dict = new_production.to_dict()
        response = make_response(
            response_dict,
            201
        )
        return response


    # creating path
api.add_resource(Productions, "/productions")


class ProductionByID(Resource):
    def get(self, id):
        production = Production.query.filter(
            Production.id == id).first().to_dict()
        response = make_response(
            production,
            200
        )
        return response


api.add_resource(ProductionByID, "/productions/<int:id>")


# ===================================Cast Members Route===================================================

class CastMembers(Resource):
    def get(self):
        cast_member_list = [member.to_dict()
                            for member in CastMember.query.all()]
        response = make_response(
            cast_member_list,
            200
        )
        return response


api.add_resource(CastMembers, "/castmembers")

# @app.before_request
# def preprocess_request():
#     # Code to be executed before each request
#     print("Executing before_request...")
#     print("Request Path:", request.path)


# @app.route('/productions/<string:title>')
# def production(title):
#     production = Production.query.filter(Production.title == title).first()
#     production_response = {
#         "title": production.title,
#         "genre": production.genre,
#         "Budget": production.budget,
#         "Image": production.image,
#         "Director": production.director,
#         "director": production.director,
#         "Description": production.description,
#         "Ongoing": production.ongoing,
#     }

#     response = make_response(
#         jsonify(production_response), 200
#     )

#     return response


# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
