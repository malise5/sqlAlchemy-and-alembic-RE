# 🤪  setUp Imports

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate

from flask_restful import Api, Resource

from models import db, Production

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

# =========================================Routes=============================================


class Productions(Resource):
    def get(self):
        # production_list = [{
        #     "title": production.title,
        #     "genre": production.genre,
        #     "Budget": production.budget,
        #     "Image": production.image,
        #     "Director": production.director,
        #     "director": production.director,
        #     "Description": production.description,
        #     "Ongoing": production.ongoing,
        # } for production in Production.query.all()]
        production_list = [production.to_dict()
                           for production in Production.query.all()]

        response = make_response(
            {"data_length": len(production_list),
             "data": production_list}, 200
        )
        return response

    # creating path
api.add_resource(Productions, "/productions")


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
