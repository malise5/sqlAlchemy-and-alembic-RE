# 🤪  setUp Imports
from flask_bcrypt import Bcrypt
from models import db, Production, CastMember, User
from flask_cors import CORS
from werkzeug.exceptions import NotFound
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask import Flask, jsonify, make_response, request, abort, session, render_template
import os
from dotenv import load_dotenv
load_dotenv()


# error Handling

# import Cors from flask_cors


# 🤪  Intialize the App
app = Flask(__name__, static_url_path='')
CORS(app)
bcrypt = Bcrypt(app)


# 🤪  setUp database
# dev
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# prod
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI")
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

        try:
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
        except ValueError as e:
            abort(422, "e.args[0]")

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


# =================================🤟 🌐  Authorization and Authentication===================================================================
class Users(Resource):
    def post(self):
        # Retrieve the JSON input from the request
        form_input = request.get_json()

        # Create a new User object with the provided input
        new_user = User(
            # Assuming the name is provided in the JSON input
            name=form_input['name'],
            # Assuming the email is provided in the JSON input
            email=form_input['email']
        )

        # Add the new_user object to the database session
        db.session.add(new_user)

        # Commit the changes to the database
        db.session.commit()

        # Set the 'user_id' value in the session to the ID of the new user
        session['user_id'] = new_user.id

        # Create a response with the serialized user data and status code 201
        response = make_response(
            new_user.to_dict(),  # Assuming there's a to_dict() method to serialize the user object
            201
        )

        return response


# Add the Users resource to the API with the specified endpoint
api.add_resource(Users, "/user")

# ===================================Signup===================================================


class Signup(Resource):
    def post(self):
        # Get the JSON data from the request
        from_json = request.get_json()

        # Create a new User instance with the provided name and email
        new_user = User(
            name=from_json['name'],
            email=from_json['email']
        )

        # Set the password hash for the new user
        new_user.password_hash = from_json['password']

        # Add the new user to the database session
        db.session.add(new_user)

        # Commit the changes to the database
        db.session.commit()

        response = make_response(
            new_user.to_dict(),
            201
        )
        return response


api.add_resource(Signup, "/signup")

# =====================================LOGIN===============================================


class Login(Resource):
    def post(self):
        try:
            # Retrieve the JSON data from the request
            from_json = request.get_json()

            # Retrieve the user from the database based on the provided name
            user = User.query.filter_by(name=from_json["name"]).first()

            # Authenticate the user by checking the password hash
            if user.authenticate(from_json["password"]):
                # Store the user_id in the session
                session["user_id"] = user.id

                # Create a response with the user data as JSON
                response = make_response(
                    # Update this line with the desired user attribute
                    user.to_dict(),
                    200
                )
                return response
        except:
            # Raise an HTTP 401 Unauthorized error for incorrect user authentication
            abort(401, "Unauthorized error for incorrect user authentication")


# Register the Login resource to the "/login" endpoint
api.add_resource(Login, "/login")


# ==================================Authorized Session====================================================


class AuthorizedSession(Resource):
    def get(self):
        try:
            # Retrieve the user from the database based on the stored user_id in the session
            user = User.query.filter_by(id=session['user_id']).first()

            # Create a response with the user data as a dictionary
            response = make_response(
                user.to_dict(),
                200
            )
            return response
        except:
            # Raise an HTTP 404 Not Found error for unauthorized access
            abort(404, "Unauthorized Access")


# Register the AuthorizedSession resource to the "/authorized" endpoint
api.add_resource(AuthorizedSession, "/authorized")


# ==================================LOGOUT==============================================================


# Create a Logout resource
class Logout(Resource):
    def delete(self):
        # Set the 'user_id' value in the session to None, effectively logging out the user
        session['user_id'] = None

        # Create a response with an empty body and status code 204 (No Content)
        response = make_response('', 204)

        return response


# Add the Logout resource to the API with the specified endpoint
api.add_resource(Logout, "/logout")


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
