from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)


from RMA_APP.auth import login_required
from . import reddit

bp = Blueprint('main', __name__)


@bp.route('/')
@login_required
def index():
    return render_template("home.html")


@bp.route('/result', methods=('GET', 'POST'))
@login_required
def analyze():
    if request.method == 'POST':
        sName = request.form['subredditName']

        ##Check if subreddit is valid
        if(reddit.validateSubreddit(sName) == False):
            return "Failed to validate"

        return reddit.getText(sName)

        ##Get Tone Analyzer Results
    ##return render_template("result.html",subredditName=sName);

