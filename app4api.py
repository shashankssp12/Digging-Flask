from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort

app4api = Flask(__name__) # create an app instance and this is the main entry point to the application
app4api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test2.db' # the URI for the database
db = SQLAlchemy(app4api) # create a database instance / initialize the database
api = Api(app4api) # create an api instance


class UserModel(db.Model): # create a class for the database
    id = db.Column(db.Integer, primary_key=True) # the id column
    name = db.Column(db.String(100), nullable=False) # the content column
    email = db.Column(db.String(100), nullable=False) # the content column

    def __repr__(self): # a string representation of the class
        return f"{self.id}, {self.name}, {self.email}"    
    

user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help='Name cannot be blank')
user_args.add_argument('email', type=str, required=True, help='Email cannot be blank')

userFields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
}


class Users(Resource):
  @marshal_with(userFields)
  def get(self):
    users=UserModel.query.all()
    return users
  @marshal_with(userFields)
  def post(self):
    args = user_args.parse_args()
    user = UserModel(name=args['name'], email=args['email'])
    db.session.add(user)
    db.session.commit()
    return user, 201

api.add_resource(Users, '/api/users/')

# get a user by id 
class User(Resource):
  @marshal_with(userFields)
  def get(self, user_id):
    user = UserModel.query.filter_by(id=user_id).first()
    if not user:
      abort(404, message='User not found')
    return user
  @marshal_with(userFields)
  def put(self, user_id):
    args = user_args.parse_args()
    user = UserModel.query.filter_by(id=user_id).first()
    if not user:
      abort(404, message='User not found')
    user.name = args['name']
    user.email = args['email']
    db.session.commit()
    return user
  def delete(self, user_id):
    user = UserModel.query.filter_by(id=user_id).first()
    if not user:
      abort(404, message='User not found')
    db.session.delete(user)
    db.session.commit()
    return '', 204

api.add_resource(User, '/api/users/<int:user_id>')



@app4api.route('/api') #
def home():
  return 'Flask REST API'
    

if __name__ == '__main__':
  app4api.run(debug=True)  