from flask import (
    Blueprint, render_template, request, session
)


from RMA_APP.auth import login_required
from . import reddit, watson, azure
import json

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
    if not session.get("username"):
        return render_template("auth/login.html")
    else:
        return render_template("home.html")


@bp.route('/result', methods=('GET', 'POST'))
@login_required
def analyze():
    username = session["username"]

    # If the user submitted a subreddit name
    if request.method == 'POST':
        
        # content needs to be inserted
        subreddit_name = request.form['subredditName']
        # username = login_user()
        
        subreddit_sort=request.form['subredditSort']
        
        now = datetime.datetime.now()
        #now = "2019-4-18"

        db = get_db()
        
        # Check if subreddit is valid
        if not reddit.validate_subreddit(subreddit_name):
            return "Failed to validate"
        # If valid use praw to get the text of all posts and comments
        text_from_reddit = reddit.get_text(subreddit_name, subreddit_sort)

        
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
        # return watson.analyze_tone(text_from_reddit)


        # TODO: Return a template with the tones instead of json dump -Cam


        # Get Tone Analysis from IBM Watson
        watson_analysis = json.loads(watson.analyze_tone(text_from_reddit))

        tones = []
        for tone in watson_analysis['document_tone']['tones']:
            tones.append({
                'tone_id':tone['tone_name'],
                'score':tone['score']
            })

        # Get Tone Analysis from Microsoft Azure
        azure_analysis = azure.analyze(text_from_reddit)




        return render_template("result.html", tones = tones, azure_score = azure_analysis, subreddit_name=subreddit_name)



