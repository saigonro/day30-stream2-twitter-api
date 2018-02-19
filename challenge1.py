import tweepy
from auth import api
import json

count = 10

timeline = list(tweepy.Cursor(api.home_timeline).items(count))

tweets_list = []

for status in timeline:
    tweets_list.append(status._json)

with open("tweets.json", "w") as f:
    f.write(json.dumps(tweets_list))

print("Done")