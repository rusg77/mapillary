from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class CreateUserForm(FlaskForm):
    username = StringField('username')
    email = StringField('email')
    birthdate = StringField('birthdate')
    address = StringField('address')
    submit = SubmitField('Create')
