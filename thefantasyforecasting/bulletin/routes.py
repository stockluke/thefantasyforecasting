from flask import Blueprint, render_template
from thefantasyforecasting import global_dict

bulletin = Blueprint('bulletin', __name__, template_folder='templates')


@bulletin.route('/announcements')
def announcements():
    return render_template('announcements.html', global_dict=global_dict, title='Announcements')


# Need to add roll_required('Admin')
@bulletin.route('/announcements/new')
def announcements_new():
    return render_template('announcements_new.html', global_dict=global_dict, title='New Announcement')


@bulletin.route('/polls')
def polls():
    return render_template('polls.html', global_dict=global_dict, title='Polls')


# Need to add roll_required('Admin')
@bulletin.route('/polls/new')
def polls_new():
    return render_template('polls_new.html', global_dict=global_dict, title='New Poll')


@bulletin.route('/trophies')
def trophies():
    return render_template('trophies.html', global_dict=global_dict, title='Trophies')