from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from thefantasyforecasting.models import User


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

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different username.')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email already has an account.')


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


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), Length(min=6, max=20), EqualTo('password')])
    submit = SubmitField('Reset Password')