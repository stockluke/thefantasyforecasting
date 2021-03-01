from flask import Blueprint, render_template

extra = Blueprint('extra', __name__, template_folder='templates')


@extra.route('/about')
def about():
    return render_template('about.html', title='about')


# This should only be found in the about page
@extra.route('/contact')
def contact():
    return render_template('contact.html', title='contact')


@extra.route('/FAQ')
def faq():
    return render_template('FAQ.html', title='FAQ')


@extra.route('/privacy')
def privacy():
    return render_template('privacy.html', title='privacy')


@extra.route('/rules')
def rules():
    return render_template('rules.html', title='rules')


@extra.route('/scoring')
def scoring():
    return render_template('scoring.html', title='scoring')


@extra.route('/terms')
def terms():
    return render_template('terms.html', title='terms')
