import sys
sys.dont_write_bytecode = True
import twitter
from openargs_twitter_creds import *

api = twitter.Api(consumer_key=twitter_consumer_key,
                  consumer_secret=twitter_consumer_secret,
                  access_token_key=twitter_access_token_key,
                  access_token_secret=twitter_access_token_secret,
                  tweet_mode="extended")

twitter_user = api.VerifyCredentials()
print("Running as user \"{0}\" (handle: {1})\n".format(twitter_user.name, twitter_user.screen_name))

t = api.GetUserTimeline(screen_name="openargs", exclude_replies=True, count=30)
tweets = [i.AsDict() for i in t]

for t in tweets:
    if 'retweeted_status' in t.keys():
        print(
            t['created_at'] + "\n" + "RT by @" + t['user']['screen_name'] + " from @" + t['retweeted_status']['user']['screen_name'] + ", " + t['retweeted_status']['created_at'] + ":",
            "\n",
            t['retweeted_status']['full_text'],
            "\n")
    else:
        print(
            t['created_at'] + "\n" + "Tweet from @" + t['user']['screen_name'] + ":",
            "\n",
            t['full_text'],
            "\n")

