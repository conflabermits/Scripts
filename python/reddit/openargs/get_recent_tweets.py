import sys
sys.dont_write_bytecode = True
import twitter
from openargs_twitter_creds import *

api = twitter.Api(consumer_key=twitter_consumer_key,
                  consumer_secret=twitter_consumer_secret,
                  access_token_key=twitter_access_token_key,
                  access_token_secret=twitter_access_token_secret)

twitter_user = api.VerifyCredentials()
print("Running as user \"{0}\" (handle: {1})\n".format(twitter_user.name, twitter_user.screen_name))

t = api.GetUserTimeline(screen_name="openargs", count=10)
tweets = [i.AsDict() for i in t]
for t in tweets:
    print(t['id'], t['text'])

