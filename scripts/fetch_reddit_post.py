import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit_client_id = os.getenv('REDDIT_CLIENT_ID')
reddit_client_secret = os.getenv('REDDIT_CLIENT_SECRET')
reddit_user_agent = os.getenv('REDDIT_USER_AGENT')


reddit = praw.Reddit(
    client_id = reddit_client_id,
    client_secret = reddit_client_secret,
    user_agent = reddit_user_agent
)

subreddit_name = 'dataengineering'
subreddit = reddit.subreddit(subreddit_name)

try:
    top_post = subreddit.top(time_filter='day', limit=5)
    for post in top_post:
        print(post.id)
        print(post.title)
        print(f"Score: {post.score}")
        print(f"Author: {post.author}")
        print(f"URL: {post.url}")
        print(f"Comments: {post.num_comments}")
        print("-" * 40)  
except Exception as e:
    print(f"Failed to fetch top post: {e}")