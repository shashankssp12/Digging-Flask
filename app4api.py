from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort

app4api = Flask(__name__) # create an app instance and this is the main entry point to the application
app4api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test2.db' # the URI for the database
db = SQLAlchemy(app4api) # create a database instance / initialize the database
api = Api(app4api) # create an api instance

# TODO: Set up the full api thing here





class UserModel(db.Model): # create a class for the database
    id = db.Column(db.Integer, primary_key=True) # the id column
    name = db.Column(db.String(100), nullable=False) # the content column
    email = db.Column(db.String(100), nullable=False) # the content column

    def __repr__(self): # a string representation of the class
        return f"{self.id}, {self.name}, {self.email}"    
    


@app4api.route('/api', methods=['GET','POST']) # the site to route to, index/main in this case
def home():
    if request.method == 'POST':
      pass
  
        
    else:     
        pass