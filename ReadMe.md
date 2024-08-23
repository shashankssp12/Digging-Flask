Plan : 
- Setup and Workflow
- Get a basic app running
- Templates and Static Content
- Setting up and using Database (SQLite)
- Create a basic CRUD application
- Deploy to Heroku

# Creating the database: 
- This is the place the app is going to locate the database: 
 app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
- db = SQLALCHEMY(app)
- in python shell type: from app import db
- type: db.create_all()
- exit()


# Concepts Used: 
- template inheritance