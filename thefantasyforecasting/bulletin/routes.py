from flask import Blueprint, render_template

bulletin = Blueprint('bulletin', __name__, template_folder='templates')


@bulletin.route('/announcements')
def announcements():
    return render_template('announcements.html', title='Announcements')


# Need to add roll_required('Admin')
@bulletin.route('/announcements/new')
def announcements_new():
    return render_template('announcements_new.html', title='New Announcement')


@bulletin.route('/polls')
def polls():
    return render_template('polls.html', title='Polls')


# Need to add roll_required('Admin')
@bulletin.route('/polls/new')
def polls_new():
    return render_template('polls_new.html', title='New Poll')


@bulletin.route('/trophies')
def trophies():
    return render_template('trophies.html', title='Trophies')