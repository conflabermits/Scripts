import sys
sys.dont_write_bytecode = True
import twitter
from openargs_twitter_creds import *

api = twitter.Api(consumer_key=twitter_consumer_key,
                  consumer_secret=twitter_consumer_secret,
                  access_token_key=twitter_access_token_key,
                  access_token_secret=twitter_access_token_secret)

users = api.GetFriends()
print([u.screen_name for u in users])

