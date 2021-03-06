from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('hub.html', title='Hub')
    return render_template('landing.html', title='Landing')


@main.route('/util')
def utils():
    from thefantasyforecasting.utils import update_icao_list

    update_icao_list()
    return redirect(url_for('main.home'))
