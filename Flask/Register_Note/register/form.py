from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField,SubmitField, validators

class BasicForm(FlaskForm):
    username = StringField('Username', validators = [
        validators.DataRequired()
        validators.Length(3, 20)
    ])
    email = EmailField('Email', validators=[
        validators.DataRequired(),
        validators.Length(1, 50),
        validators.Email()
    ])
    password = PasswordField('PassWord', validators=[
        validators.DataRequired(),
        validators.Length(5, 10),
        validators.EqualTo('password2', message='PASSWORD NEED MATCH')
    ])
    password2 = PasswordField('Confirm PassWord', validators=[
        validators.DataRequired()
    ])
    submit = SubmitField('Register New Account')