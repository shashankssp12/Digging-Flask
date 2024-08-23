from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # create an app instance and this is the main entry point to the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # the URI for the database
db = SQLAlchemy(app) # create a database instance / initialize the database


class Todo(db.Model): # create a class for the database
    id = db.Column(db.Integer, primary_key=True) # the id column
    content = db.Column(db.String(200), nullable=False) # the content column

    def __repr__(self): # a string representation of the class
        return '<Task %r>' % self.id


@app.route('/') # the site to route to, index/main in this case
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True) # run the application
    
    
