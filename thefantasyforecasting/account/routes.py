from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required, current_user, logout_user
from thefantasyforecasting import bcrypt
from thefantasyforecasting.account.forms import RegistrationForm

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
        return redirect(url_for('main.hub'))
    return render_template('register.html', title='Register', form=form, remove_header=True)


@account.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return render_template('login.html', title='Login')


@account.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@account.route('/achievements/<string:username>')
@login_required
def achievements():
    return render_template('achievements.html', title='Achievements')


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
