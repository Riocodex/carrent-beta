from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField
from wtforms.validators import DataRequired , Length , EqualTo , Email

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
    books = db.relationship('Books' , lazy = 'dynamic' , backref=db.backref('category' , lazy=True))
  
class ResetRequestForm(FlaskForm):
    email = StringField(label ='Email' , validators=[DataRequired()])
    password = PasswordField(label='Reset Password' , validators=[DataRequired()])