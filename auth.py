import tweepy
from tweepy import OAuthHandler

MONGODB_URI = 'mongodb://root:1234@ds237848.mlab.com:37848/day30bootcampflask'

CONSUMER_KEY = 'Z72QVYrxCGlIf8wuHT2RHOcQP'
CONSUMER_SECRET = 'nwolyvMJWw8RWjigDNVnI9luu9mjL2nqNeiuW6r7y0gWl5nKPh'
OAUTH_TOKEN = '964439599698272258-03fvJbgYMfHSRmtU4PgjymcAjQEa8fP'
OAUTH_TOKEN_SECRET = 'D8H4dm3o7rtZXp4QsEQY4xU7HfYNCAQYXnU13W5S3fWZO'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth