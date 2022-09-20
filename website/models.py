from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Books(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    carBrand = db.Column(db.String(150))
    numberOfSeats =  db.Column(db.String(150))
    costs = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    books = db.relationship('Books')
  