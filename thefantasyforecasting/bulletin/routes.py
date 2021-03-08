from flask import Blueprint, render_template, request
from thefantasyforecasting import global_dict
from thefantasyforecasting.models import Post

bulletin = Blueprint('bulletin', __name__, template_folder='templates')


@bulletin.route("/post/<int:post_id>")
def post(post_id):
    posts = Post.query.get_or_404(post_id)
    return render_template('post.html', global_dict=global_dict, post=posts)


@bulletin.route('/announcements')
def announcements():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('announcements.html', global_dict=global_dict, title='Announcements', posts=posts)


# Need to add roll_required('Admin')
@bulletin.route('/announcements/new')
def announcements_new():
    return render_template('announcements_new.html', global_dict=global_dict, title='New Announcement')


@bulletin.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html', global_dict=global_dict, title='Leaderboard')


@bulletin.route('/trophies')
def trophies():
    return render_template('trophies.html', global_dict=global_dict, title='Trophies')
