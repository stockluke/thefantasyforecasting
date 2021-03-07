from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required
from thefantasyforecasting import global_dict
from thefantasyforecasting.utils import update_icao_list

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('hub.html', global_dict=global_dict, title='Hub')
    return render_template('landing.html', global_dict=global_dict, title='Landing')


@main.route('/utils')
@login_required
def utils():
    cmd = request.args.get('cmd')
    if cmd is None:
        return render_template('utils.html', global_dict=global_dict, title='Utilities')

    # I want to make a button to perform the action below with model to confirm
    if cmd == 'update_icao_list':
        print('Updated ICAO List')
        #update_icao_list()
    return render_template('utils.html', global_dict=global_dict, title='Utilities')
