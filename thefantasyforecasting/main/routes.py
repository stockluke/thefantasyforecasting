from flask import Blueprint, render_template
from flask_login import current_user

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('hub.html', title='Hub')
    return render_template('landing.html', title='Landing')
