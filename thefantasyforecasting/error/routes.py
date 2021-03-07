from flask import Blueprint, render_template
from thefantasyforecasting import global_dict

error = Blueprint('error', __name__, template_folder='templates')


@error.app_errorhandler(403)
def error_403(e):
    return render_template('403.html', global_dict=global_dict, title='403'), 403


@error.app_errorhandler(404)
def error_404(e):
    return render_template('404.html', global_dict=global_dict, title='404'), 404


@error.app_errorhandler(500)
def error_500(e):
    return render_template('500.html', global_dict=global_dict, title='500'), 500
