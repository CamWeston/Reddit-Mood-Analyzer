import praw

client = "NuwX_u6Lwkwx4g"
secret = "-hm0-OSd1QPt36A3KWKPRTbPUls"


def connect():
    return praw.reddit(
        client_id = client,
        client_secret = secret,
        username = 'RedditMoodAnalyzer',
        password = 'ChickenSalad123!',
        user_agent = 'Analyze posts and comments from subreddits'
    )

def getText(subRedditName):
    reddit = connect()
    subreddit = reddit.subredit(subRedditName)
    return "Ran Get Text";


