# importing libraries
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import abort


# creating an instance of the flask app
app = Flask(__name__)


# Initializing our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# db.create_all()
#
# if __name__ == '__main__':
#     pass