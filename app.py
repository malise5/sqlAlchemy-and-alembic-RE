# 🤪  setUp Imports

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate

from models import db, Production

# 🤪  Intialize the App
app = Flask(__name__)

# 🤪  setUp database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 🤪  setUp migration and initialize instance with 'db.init)app(app)
migrate = Migrate(app, db)
db.init_app(app)


# =========================================Routes=============================================

@app.before_request
def preprocess_request():
    # Code to be executed before each request
    print("Executing before_request...")
    print("Request Path:", request.path)


@app.route('/')
def index():
    return '<h1> Hallo</h1>'


@app.route('/image')
def image():
    return '<img src="https://www.freecodecamp.org/news/content/images/size/w2000/2022/09/jonatan-pie-3l3RwQdHRHg-unsplash.jpg"alt="Girl in a jacket" width="500" height="600"/>'


@app.route('/productions/<string:title>')
def production(title):
    production = Production.query.filter(Production.title == title).first()
    production_response = {
        "title": production.title,
        "genre": production.genre,
        "Budget": production.budget,
        "Image": production.image,
        "Director": production.director,
        "director": production.director,
        "Description": production.description,
        "Ongoing": production.ongoing,
    }

    response = make_response(
        jsonify(production_response), 200
    )

    return response


# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
