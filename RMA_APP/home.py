from flask import (
    Blueprint, render_template, request
)


from RMA_APP.auth import login_required
from . import reddit, watson, azure
import json


# Blueprint for main page where user can enter a subreddit
bp = Blueprint('main', __name__)

# Index Route
@bp.route('/')
@login_required
def index():
    return render_template("home.html")


@bp.route('/result', methods=('GET', 'POST'))
@login_required
def analyze():
    # If the user submitted a subreddit name
    if request.method == 'POST':
        subreddit_name = request.form['subredditName']

        # Check if subreddit is valid
        if not reddit.validate_subreddit(subreddit_name):
            return "Failed to validate"
        # If valid use praw to get the text of all posts and comments
        text_from_reddit = reddit.get_text(subreddit_name)

        # Get Tone Analysis from IBM Watson
        watson_analysis = json.loads(watson.analyze_tone(text_from_reddit))



        # Get Tone Analysis from Microsoft Azure
        azure_analysis = azure.analyze(text_from_reddit)

        i = 0
        tones = []
        for tone in watson_analysis['document_tone']['tones']:
            tones.append({
                'tone_id':tone['tone_name'],
                'score':tone['score']
            })



        return render_template("result.html", tones = tones, subreddit_name=subreddit_name)


