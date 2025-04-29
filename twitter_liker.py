import tweepy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twitter API credentials from .env
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate to Twitter using OAuth 1.0a
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def like_tweet(tweet_id):
    try:
        print(f"❤️ Liking Tweet ID: {tweet_id}")
        api.create_favorite(tweet_id)
        print("✅ Tweet liked successfully!")

    except tweepy.errors.Forbidden as e:
        print("🚫 Forbidden Error:", e)
    except tweepy.errors.TooManyRequests:
        print("⚠️ Rate limit exceeded. Try again later.")
    except Exception as e:
        print("❌ Some other error occurred:", e)

# Replace with a real Tweet ID
like_tweet("1873729163271762254")