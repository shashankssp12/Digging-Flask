# Plan : 
- ✅Setup and Workflow
- ✅Get a basic app running
- ✅Templates and Static Content
- ✅Setting up and using Database (SQLite)
- ✅Create a basic CRUD application
- ❌Deploy to Heroku

# Creating the database: 
## Method 1:
- This is the place the app is going to locate the database: 
 app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
- db = SQLALCHEMY(app)
- in python shell type: from app import db,app 
- with app.app_context():
- type:(give identation) db.create_all()
- exit()
## Method 2: 
- Create file: *create_db.py* 
- Enter code: 
    - `from app4api import db,app`
    - `with app.app_context():`
    - `db.create_all()`  


# Concepts Used: 
- template inheritance
- serialized json (with the use of marshal_with we can send json back)


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

# Learnt shortcuts: 
- shift + alt + downarrow: Copies full line below
- alt + z : to refactor the current line of code


[Video Ref link for Creating RESTAPI](https://youtu.be/z3YMz-Gocmw?feature=shared)