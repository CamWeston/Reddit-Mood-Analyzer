import praw
import sys

client = "NuwX_u6Lwkwx4g"
secret = "-hm0-OSd1QPt36A3KWKPRTbPUls"

# Returns praw reddit instance
def connect():
    return praw.Reddit(client_id=client, client_secret=secret, user_agent='Analyze posts and comments from subreddits')

# Determines whether given subreddit_name exists or not, returns boolean value
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

# Return the raw text from posts and comments of the given subreddit. Able to sort by new, hot, and top.
# Text size will be between 8000 and 120000 characters. If naturally below 8000 it will be buffered with whitespace.
def get_text(subreddit_name, subreddit_sort):
    all_text = ""

    reddit = connect()
    subreddit = reddit.subreddit(subreddit_name)
    
    # Sort submissions
    # Will only work if the given subreddit_sort is one of three expected values. Matches radio buttons.
    if subreddit_sort == "New":
        submissions = subreddit.new()
    elif subreddit_sort == "Hot":
        submissions = subreddit.hot()
    elif subreddit_sort == "Top":
        submissions = subreddit.top()
    
    # Get text from posts and comments, does not expand comment blocks.
    for submission in submissions:
        if sys.getsizeof(all_text) < 120000:
            all_text += submission.title + " "
            submission.comments.replace_more(limit=0)
            for comment in submission.comments:
                # Ignores stickied comments (typically bot or moderator, not indicative of mood)
                if not comment.stickied and sys.getsizeof(all_text) < 120000:
                    all_text += comment.body + " "

    # Buffer text size to prevent azure crashes
    if len(all_text) < 8000:
        all_text += " "*(8000-len(all_text))
                    
    return all_text[:120000]

