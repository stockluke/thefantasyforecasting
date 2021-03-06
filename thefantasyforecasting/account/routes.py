from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_required, current_user, login_user, logout_user
from thefantasyforecasting import bcrypt, db
from thefantasyforecasting.models import User
from thefantasyforecasting.account.forms import RegistrationForm, LoginForm

account = Blueprint('account', __name__, template_folder='templates')


@account.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    return render_template('settings.html', title='Settings')


@account.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Register', form=form, remove_header=True)


@account.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            valid_password = bcrypt.check_password_hash(user.password, form.password.data)
            if valid_password:
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful.', 'danger')
    return render_template('login.html', title='Login', form=form)


@account.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@account.route('/achievements')
@account.route('/achievements/<string:username>')
def achievements(username):
    return render_template('achievements.html', title='Achievements')


@account.route('/messages')
@login_required
def messages():
    return render_template('messages.html', title='Messages')


@account.route('/reset_request', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return render_template('reset_request.html', title='Password Reset Request')


@account.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return render_template('reset_request.html', title='Password Reset')
