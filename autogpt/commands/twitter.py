"""Simple helper for posting tweets via the Tweepy library.

The functions here expect Twitter API credentials to be provided via the
environment variables ``TW_CONSUMER_KEY``, ``TW_CONSUMER_SECRET``,
``TW_ACCESS_TOKEN`` and ``TW_ACCESS_TOKEN_SECRET``.
"""

import tweepy
import os
from dotenv import load_dotenv

load_dotenv()


def send_tweet(tweet_text: str) -> None:
    """Post ``tweet_text`` to Twitter.

    Parameters
    ----------
    tweet_text : str
        The text content to publish.
    """
    consumer_key = os.environ.get("TW_CONSUMER_KEY")
    consumer_secret = os.environ.get("TW_CONSUMER_SECRET")
    access_token = os.environ.get("TW_ACCESS_TOKEN")
    access_token_secret = os.environ.get("TW_ACCESS_TOKEN_SECRET")
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    # Send tweet
    try:
        api.update_status(tweet_text)
        print("Tweet sent successfully!")
    except tweepy.TweepyException as e:
        print("Error sending tweet: {}".format(e.reason))
