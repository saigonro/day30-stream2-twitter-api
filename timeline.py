import tweepy
from auth import api

count = 10

timeline = list(tweepy.Cursor(api.home_timeline).items(count))

print(timeline[1]._json.keys())

# Get the text of tweets
for tweet in timeline:
    print(tweet._json['text'])

# Get text of tweets with more than 10 retweets
for tweet in timeline:
    if tweet._json['retweet_count'] > 10:
        print("----------*-----------")
        print(tweet._json['text'])