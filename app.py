# 🤪  setUp Imports

from flask import Flask, jsonify, make_response, request, abort
from flask_migrate import Migrate

from flask_restful import Api, Resource

# error Handling
from werkzeug.exceptions import NotFound

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

    # ======== ⏫ Get =============

    # GET method to retrieve all productions
    def get(self):
        # Query all productions from the database and convert them to dictionaries
        production_list = [production.to_dict()
                           for production in Production.query.all()]

        # Create a response with the production list and status code 200 (OK)
        response = make_response(
            production_list,
            200
        )
        return response

    # ======== ⏫ Post =============

    # POST method to create a new production
    def post(self):
        # Retrieve the JSON data from the request from input Form (Frontend Request )
        request_json = request.get_json()

        # Create a new Production object with the data from the request
        new_production = Production(
            title=request_json['title'],
            genre=request_json['genre'],
            budget=request_json['budget'],
            image=request_json['image'],
            director=request_json['director'],
            description=request_json['description'],
            ongoing=request_json['ongoing'],
        )

        # Add the new production to the database session
        db.session.add(new_production)
        db.session.commit()

        # Convert the new production object to a dictionary
        response_dict = new_production.to_dict()

        # Create a response with the new production data and status code 201 (Created)
        response = make_response(
            response_dict,
            201
        )
        return response


# Add the Productions resource to the API at the "/productions" endpoint
api.add_resource(Productions, "/productions")


class ProductionByID(Resource):

    # ======== ⏫ Get =============

    # GET method to retrieve a specific production by ID
    def get(self, id):
        # Query the production from the database with the given ID
        production = Production.query.filter(Production.id == id).first()

        # If the production is not found, raise a NotFound exception
        if not production:
            abort(404, "The Production you were looking for was not found")

        # Convert the production object to a dictionary
        production_dict = production.to_dict()

        # Create a response with the production data and status code 200 (OK)
        response = make_response(production_dict, 200)

        # Return the response
        return response

    # ======== ⏫ Patch=============

    def patch(self, id):
        # Retrieve the production from the database with the given ID
        production = Production.query.filter_by(id=id).first()

        # If the production is not found, raise a NotFound exception with a 404 status code and an error message
        if not production:
            abort(404, "The Production you want to update was not found")

        # Retrieve the JSON data from the request FRontend
        request_json = request.get_json()

        # Update the production object with the values from the request
        for key in request_json:
            setattr(production, key, request_json[key])

        # Add the updated production to the database session
        db.session.add(production)
        db.session.commit()

        # Create a response with the updated production data and status code 201 (Created)
        response = make_response(
            production.to_dict(),
            201
        )

        # Return the response
        return response

    # ======== ⏫ Delete=============

    def delete(self, id):
        # Retrieve the production from the database with the given ID
        production = Production.query.filter_by(id=id).first()

        # If no production is found, raise a NotFound exception with a 404 status code and an error message
        if not production:
            abort(404, "The production is not available")

        # Delete the production from the database session
        db.session.delete(production)
        db.session.commit()

        response = make_response(
            # An empty dictionary or any desired response data
            {"Message": "The Production was Successfully Deleted!!! "},
            200  # Status code indicating successful deletion, e.g., 200 (OK)
        )

        # Return the response
        return response


# Add the ProductionByID resource to the API at the "/productions/<int:id>" endpoint
api.add_resource(ProductionByID, "/productions/<int:id>")


# ===================================Cast Members Route===================================================

class CastMembers(Resource):

    # ======== ⏫ Get =============

    # GET method to retrieve all cast members
    def get(self):
        # Query all cast members from the database and convert them to dictionaries
        cast_member_list = [member.to_dict()
                            for member in CastMember.query.all()]

        # Create a response with the cast member list and status code 200 (OK)
        response = make_response(cast_member_list, 200)

        # Return the response
        return response

    # ======== ⏫ Post=============

    # POST method to create a new cast member
    def post(self):
        # Retrieve the JSON data from the request
        response_json = request.get_json()

        # Create a new CastMember object with the data from the request
        new_cast_member = CastMember(
            name=response_json['name'],
            role=response_json['role'],
            production_id=response_json['production_id']
        )

        # Add the new cast member to the database session
        db.session.add(new_cast_member)

        # Commit the changes to the database
        db.session.commit()

        # Convert the new cast member object to a dictionary
        new_response = new_cast_member.to_dict()

        # Create a response with the new cast member data and status code 201 (Created)
        response = make_response(new_response, 201)

        # Return the response
        return response


# Add the CastMembers resource to the API at the "/castmembers" endpoint
api.add_resource(CastMembers, "/cast_members")


class CastMemberID(Resource):

    # ======== ⏫ Get=============

    # GET method to retrieve a specific cast member by ID
    def get(self, id):
        # Query the cast member from the database with the given ID
        member_id = CastMember.query.filter(CastMember.id == id).first()

        # If the cast member is not found, raise a NotFound exception with a 404 status code and an error message
        if not member_id:
            abort(404, "The Cast Member not found")

        # Convert the cast member object to a dictionary
        member_dict = member_id.to_dict()

        # Create a response with the cast member data and status code 201 (Created)
        response = make_response(
            member_dict,
            201
        )
        return response

    # ======== ⏫ Patch=============

    def patch(self, id):
        # Retrieve the cast members from the database with the given ID
        cast_member = CastMember.query.filter_by(id=id).first()

        # If no cast members are found, raise a NotFound exception with a 404 status code and an error message
        if not cast_member:
            abort(404, "The cast member was not found")

        # Retrieve the JSON data from the request FRontend
        request_json = request.get_json()

        # Update the cast_member object with the values from the request
        for key in request_json:
            # Update each attribute of the request_json with its corresponding value
            setattr(cast_member, key, request_json[key])

        # Add the updated cast members to the database session
        db.session.add(cast_member)
        db.session.commit()

        # Create a response with the updated cast members data and status code 201 (Created)
        response = make_response(
            cast_member.to_dict(),
            200
        )

        # Return the response
        return response

    # ======== ⏫ Delete=============

    def delete(self, id):
        # Retrieve the production from the database with the given ID
        cast_member = CastMember.query.filter_by(id=id).first()

        # If no production is found, raise a NotFound exception with a 404 status code and an error message
        if not cast_member:
            abort(404, "The cast_member is not available")

        # Delete the production from the database session
        db.session.delete(cast_member)
        db.session.commit()

        response = make_response(
            # An empty dictionary or any desired response data
            {"Message": "The Cast member was Deleted Successfully!!! "},
            200  # Status code indicating successful deletion, e.g., 200 (OK)
        )

        # Return the response
        return response


# Add the CastMemberID resource to the API at the "/cast_members/<int:id>" endpoint
api.add_resource(CastMemberID, "/cast_members/<int:id>")


# ==============================================📛 Error-Handling-Route=============================================

# use the @app.errorhandler() decorator to handle Not Found routes

@app.errorhandler(NotFound)
def handle_Not_Found(e):
    response = make_response(
        "Not Found: Sorry the resource you are looking for can not be Found",
        404
    )
    return response


# if __name__ == '__main__':
#     app.run(port=5000, debug=True)


# ================================================🚩Ooops!!===========================================

# class Productions(Resource):
#     def get(self):
#         # production_list = [{
#         # "title": production.title,
#         # "genre": production.genre,
#         # "Budget": production.budget,
#         # "Image": production.image,
#         # "Director": production.director,
#         # "director": production.director,
#         # "Description": production.description,
#         # "Ongoing": production.ongoing,
#         # } for production in Production.query.all()]
#         production_list = [production.to_dict()  # must be a serializer
#                            for production in Production.query.all()]

#         response = make_response(
#             {"data_length": len(production_list),
#              "data": production_list}, 200
#         )
#         return response

#     def post(self):
#         # gets the input from the client
#         request_json = request.get_json()
#         new_production = Production(
#             title=request_json['title'],
#             genre=request_json['genre'],
#             budget=request_json['budget'],
#             image=request_json['image'],
#             director=request_json['director'],
#             description=request_json['description'],
#             ongoing=request_json['ongoing'],
#         )
#         db.session.add(new_production)
#         db.session.commit()

#         # convert it into dictionary
#         response_dict = new_production.to_dict()
#         response = make_response(
#             response_dict,
#             201
#         )
#         return response


#     # creating path
# api.add_resource(Productions, "/productions")

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
