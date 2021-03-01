import datetime
from flask import Blueprint, render_template

challenge = Blueprint('challenge', __name__, template_folder='templates')


# For submitting a new forecast
@challenge.route('/challenge/forecast/new')
def forecast_new():
    date = datetime.date.today()
    return render_template('forecast_new.html', title='New Forecast')


# For looking at an individual forecast
@challenge.route('/challenge/forecast/<int:forecast_id>')
def forecast():
    return render_template('forecast.html', title='Forecast')


# For listing past forecasts
@challenge.route('/challenge/history')
def history():
    return render_template('history.html', title='History')


@challenge.route('/challenge/leaderboard')
def leaderboard():
    return render_template('leaderboard.html', title='Leaderboard')
