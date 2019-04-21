from flask import (
    Blueprint, render_template, request
)


from RMA_APP.auth import login_required, login_user
from . import reddit, watson

from RMA_APP.db import get_db

import datetime

import sqlite3

import ast

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
    username = login_user

    # If the user submitted a subreddit name
    if request.method == 'POST':
        
        # content needs to be inserted
        subreddit_name = request.form['subredditName']
        # username = login_user()
        
        now = datetime.datetime.now()
        #now = "2019-4-18"

        db = get_db()
        
        # Check if subreddit is valid
        if not reddit.validate_subreddit(subreddit_name):
            return "Failed to validate"
        # If valid use praw to get the text of all posts and comments
        text_from_reddit = reddit.get_text(subreddit_name)
        
        # score init
        anger_score = 0
        fear_score = 0
        joy_score = 0
        sadness_score = 0
        analytical_score = 0
        confident_score = 0
        tentative_score = 0
        
        string_init_score_dictionary = watson.analyze_tone(text_from_reddit)
        init_score_dictionary = eval(string_init_score_dictionary)
        second_dictionary = init_score_dictionary["document_tone"]
        third_list = second_dictionary["tones"]
        for i in range (len(third_list)):
            if(third_list[i]["tone_id"] == "anger"):
                anger_score = third_list[i]["score"]
            elif(third_list[i]["tone_id"] == "fear"):
                fear_score = third_list[i]["score"]
            elif(third_list[i]["tone_id"] == "joy"):
                joy_score = third_list[i]["score"]
                    
            elif(third_list[i]["tone_id"] == "sadness"):
                sadness_score = third_list[i]["score"]
                
            elif(third_list[i]["tone_id"] == "analytical"):
                analytical_score = third_list[i]["score"]
                    
            elif(third_list[i]["tone_id"] == "confident"):
                confident_score = third_list[i]["score"]
            
            elif(third_list[i]["tone_id"] == "tentative"):
                tentative_score = third_list[i]["score"]
        
        db.execute(
                   """INSERT INTO search (username, date, subreddit, anger, fear, joy, sadness, analytical, confident, tentative) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                   (username, str(now), str(subreddit_name), anger_score, fear_score, joy_score, sadness_score, analytical_score, confident_score, tentative_score)
                   )
        db.commit()
        # Get Tone Analyzer Results
        return watson.analyze_tone(text_from_reddit)


        # TODO: Return a template with the tones instead of json dump -Cam

