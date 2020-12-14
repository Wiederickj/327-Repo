from qa327 import app
from flask_sqlalchemy import SQLAlchemy

"""
This file defines all models used by the server
These models provide us a object-oriented access
to the underlying database, so we don't need to 
write SQL queries such as 'select', 'update' etc.
"""


db = SQLAlchemy()
db.init_app(app)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    balance = db.Column(db.Numeric(10,2), default=0)
   
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(100))
    name = db.Column(db.String(100))
    quantity = db.Column(db.Numeric(10,2), default = 0)
    price = db.Column(db.Numeric(10,2), default = 0)
    date = db.Column(db.String(100))

# it creates all the SQL tables if they do not exist
with app.app_context():
    db.create_all()
    db.session.commit()
