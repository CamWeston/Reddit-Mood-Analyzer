import sqlite3

conn = sqlite3.connect("../Reddit-Mood-Analyzer.db")

c = conn.cursor()

anger_score = 1.01
fear_score = 1.01
joy_score = 1.01
sadness_score = 1.01
analytical_score = 1.01
confident_score = 1.01
tentative_score = 1.01
username = "jsz"
now = "2019-4-18"
subreddit_name = "abc"
c.execute(
    """INSERT INTO search (username, date, subreddit, anger, fear, joy, sadness, analytical, confident, tentative) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
           (username, now, subreddit_name, anger_score, fear_score, joy_score, sadness_score, analytical_score, confident_score, tentative_score)
           )
conn.commit()
