import re

from sqlalchemy.orm import validates
from datetime import datetime
from app import db, app


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    birthdate = db.Column(db.Date(), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def __init__(self, username, email, birthdate, address):
        self.username = username
        self.email = email
        self.birthdate = birthdate
        self.address = address

    def __repr__(self):
        return '<User %r>' % self.username

    def to_json(self):
        return {
            "username": self.username,
            "email": self.email,
            "birthdate": self.birthdate.strftime("%Y-%m-%d"),
            "address": self.address
        }

    @validates('email', 'username', 'birthdate', 'address')
    def validate(self, key, field):
        if not field:
            raise AssertionError('{} is required'.format(key.capitalize()))

        if len(field) > app.config['MAX_FIELD_LENGTH']:
            raise AssertionError('{} is too long'.format(key.capitalize()))

        if key == 'email':
            if User.query.filter(User.email == field).first():
                raise AssertionError('Email is already in use')

            if not re.match(r"[a-z_\d]+@[a-z\d]+\.[a-z\d]+", field):
                raise AssertionError('Email format is invalid')

        if key == 'birthdate':
            try:
                request_date = datetime.strptime(field, '%Y-%m-%d')
                if request_date > datetime.now():
                    raise AssertionError("Birthdate can't be in future")
                return request_date.date()
            except ValueError:
                raise AssertionError("Incorrect birthdate format, use YYYY-MM-DD")

        return field
