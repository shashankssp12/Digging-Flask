from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) # create an app instance and this is the main entry point to the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # the URI for the database
db = SQLAlchemy(app) # create a database instance / initialize the database


class Todo(db.Model): # create a class for the database
    id = db.Column(db.Integer, primary_key=True) # the id column
    content = db.Column(db.String(200), nullable=False) # the content column
    date_created = db.Column(db.DateTime, default=datetime.now) # the date column

    def __repr__(self): # a string representation of the class
        return '<Task %r>' % self.id


@app.route('/', methods=['GET','POST']) # the site to route to, index/main in this case
def index():
    if request.method == 'POST':
        input_task = request.form['task_input']
        new_task = Todo(content=input_task)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        # return "Submitted!"
        except:
            return "There was an issue adding your task"
    else:     
      database_data = Todo.query.order_by(Todo.id).all()
      return render_template('index.html', tasks_info = database_data) # render the template


if __name__ == '__main__':
    app.run(debug=True) # run the application
    
    
