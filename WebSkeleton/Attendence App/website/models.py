from . import db
from sqlalchemy.sql.functions import user
from flask_login import UserMixin
from sqlalchemy.sql import func



class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    firstname=db.Column(db.String(150))
    lastname=db.Column(db.String(50))
    