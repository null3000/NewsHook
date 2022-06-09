import praw
from discord import Webhook, RequestsWebhookAdapter
from random import randint
from dotenv import load_dotenv
import os


load_dotenv()

reddit = praw.Reddit(client_id = os.getenv("REDDIT_CLIENT_ID"),
                     client_secret = os.getenv("REDDIT_CLIENT_SECRET"),
                     user_agent = os.getenv("REDDIT_USER_AGENT"),
                     check_for_async=False)


webhook = Webhook.from_url(os.getenv("DISCORD_WEBHOOK"), adapter=RequestsWebhookAdapter())


messages = [] 
x=1
while x==1:
        subreddit = reddit.subreddit("news")
        threads = subreddit.top(time_filter="day", limit=5)
        submission = list(threads)[randint(0,2)]
        if not submission.stickied:
            if not submission.distinguished:
                if not submission.over_18: 
                    if submission.id not in messages:
                        if submission.score > 20000:
                            print(submission.url)
                            webhook.send(submission.url)
                            messages.append(submission.id)
                        else:
                            print("Nothing new")
    