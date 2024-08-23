# Plan : 
- ✅Setup and Workflow
- ✅Get a basic app running
- ✅Templates and Static Content
- ✅Setting up and using Database (SQLite)
- ✅Create a basic CRUD application
- ❌Deploy to Heroku

# Creating the database: 
- This is the place the app is going to locate the database: 
 app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
- db = SQLALCHEMY(app)
- in python shell type: from app import db,app 
- with app.app_context():
- type:(give identation) db.create_all()
- exit()


# Concepts Used: 
- template inheritance


# Heroku Deployment
- Create an account on Heroku
- Install Heroku CLI 
- Come to your editor and open terminal
- Check if env is on
- A repo must be initialized 
- Type: heroku login (super easy login process)
(Now create a heroku app)
- Type: heroku create task-master
# Unable to do with Heroku due to credit-card verfication

`can deploy on other platforms namely:`
- vercel
- render
- fly.io