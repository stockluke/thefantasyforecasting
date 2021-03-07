from flask import Blueprint, render_template
from thefantasyforecasting import global_dict

extra = Blueprint('extra', __name__, template_folder='templates')


@extra.route('/about')
def about():
    return render_template('about.html', global_dict=global_dict, title='about')


# This should only be found in the about page
@extra.route('/contact')
def contact():
    return render_template('contact.html', global_dict=global_dict, title='contact')


@extra.route('/FAQ')
def faq():
    return render_template('FAQ.html', global_dict=global_dict, title='FAQ')


@extra.route('/privacy')
def privacy():
    return render_template('privacy.html', global_dict=global_dict, title='privacy')


@extra.route('/rules')
def rules():
    return render_template('rules.html', global_dict=global_dict, title='rules')


@extra.route('/scoring')
def scoring():
    return render_template('scoring.html', global_dict=global_dict, title='scoring')


@extra.route('/terms')
def terms():
    return render_template('terms.html', global_dict=global_dict, title='terms')
