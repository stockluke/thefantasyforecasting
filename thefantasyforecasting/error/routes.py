from flask import Blueprint, render_template

error = Blueprint('error', __name__, template_folder='templates')


@error.app_errorhandler(403)
def error_403(e):
    return render_template('403.html', title='403'), 403


@error.app_errorhandler(404)
def error_404(e):
    return render_template('404.html', title='404'), 404


@error.app_errorhandler(500)
def error_500(e):
    return render_template('500.html', title='500'), 500
