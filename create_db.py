from app4api import db,app

with app.app_context():
    db.create_all()# create the database