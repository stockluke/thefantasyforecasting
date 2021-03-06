from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[
                               DataRequired(message=('Please fill out this field')),
                               Length(min=3, message=('Must be 3 characters or more.')),
                               Length(max=20, message=('Must be 20 characters or less.'))
                           ])
    firstname = StringField('First Name',
                            validators=[
                                DataRequired(message=('Please fill out this field')),
                                Length(max=256, message=('Your name cannot be possible that long.'))
                            ])
    lastname = StringField('Last Name',
                            validators=[
                                DataRequired(message=('Please fill out this field')),
                                Length(max=256, message=('Your name cannot be possible that long.'))
                            ])
    email = StringField('Email',
                        validators=[
                            DataRequired(message=('Please fill out this field')),
                            Email(),
                            Length(max=120)
                        ])
    email_confirm = StringField('Confirm Email',
                                validators=[
                                    DataRequired(message=('Please fill out this field')),
                                    Length(max=120),
                                    EqualTo('email', message=('Emails must match.'))
                                ])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(message=('Please fill out this field')),
                                 Length(min=6, message=('Must contain at least 6 characters.')),
                                 Length(max=256)
                             ])
    password_confirm = PasswordField('Confirm Password',
                                     validators=[
                                         DataRequired(message=('Please fill out this field')),
                                         EqualTo('password', message=('Passwords must match.'))
                                     ])
    # recaptcha = RecaptchaField()
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                                 Length(min=6, max=20)
                             ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
