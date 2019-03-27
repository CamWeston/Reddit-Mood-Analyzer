import praw
import sys

client = "NuwX_u6Lwkwx4g"
secret = "-hm0-OSd1QPt36A3KWKPRTbPUls"


def connect():
    return praw.Reddit(client_id=client, client_secret=secret, user_agent='Analyze posts and comments from subreddits')


def validate_subreddit(subreddit_name):
    subreddit_name.replace('/r/', '')
    subreddit_name.replace('/', '')
    reddit = connect()
    exists = True
    try:
        reddit.subreddits.search_by_name(subreddit_name, exact=True)
    except:
        exists = False
    return exists

def get_text(subreddit_name):
    all_text = ""

    reddit = connect()
    subreddit = reddit.subreddit(subreddit_name)

    submissions = subreddit.new()

    for submission in submissions:
        if sys.getsizeof(all_text) < 120000:
            all_text += submission.title
    return all_text



