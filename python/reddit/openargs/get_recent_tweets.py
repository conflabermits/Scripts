#!/usr/bin/python3

import sys
sys.dont_write_bytecode = True
import argparse
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_tz
import twitter
from openargs_twitter_creds import *


parser = argparse.ArgumentParser(description='Grab tweets and retweets from one or more accounts')
parser.add_argument("-s",
                    "--silent",
                    help="Suppress terminal output",
                    action='store_true',
                    required=False)
parser.add_argument("-a",
                    "--account",
                    help="Account(s) to grab tweets from",
                    type=str,
                    required=True)

args = parser.parse_args()


def to_datetime(datestring):
    time_tuple = parsedate_tz(datestring.strip())
    dt = datetime(*time_tuple[:6])
    return dt - timedelta(seconds=time_tuple[-1])

DESIRED_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
#TWITTER_DATE_FORMAT = '%a %b %d %H:%M:%S +0000 %Y'

api = twitter.Api(consumer_key=twitter_consumer_key,
                  consumer_secret=twitter_consumer_secret,
                  access_token_key=twitter_access_token_key,
                  access_token_secret=twitter_access_token_secret,
                  tweet_mode="extended")

twitter_user = api.VerifyCredentials()
print(
    "Running as user \"{0}\" (handle: {1})\n".format(
        twitter_user.name,
        twitter_user.screen_name
    )
)

t = api.GetUserTimeline(screen_name=args.account, exclude_replies=True, count=30)
tweets = [i.AsDict() for i in t]

for t in tweets:
    if 'retweeted_status' in t.keys():
        print(
            "RT by @{0} ({1}) of @{2} ({3}):\n{4}\n\n".format(
                t['user']['screen_name'],
                datetime.strftime(to_datetime(t['created_at']), DESIRED_DATE_FORMAT + ' UTC'),
                t['retweeted_status']['user']['screen_name'],
                datetime.strftime(to_datetime(t['retweeted_status']['created_at']), DESIRED_DATE_FORMAT + ' UTC'),
                t['retweeted_status']['full_text']
            )
        )
    else:
        print(
            "Tweet from @{0} ({1}):\n{2}\n\n".format(
                t['user']['screen_name'],
                datetime.strftime(to_datetime(t['created_at']), DESIRED_DATE_FORMAT + ' UTC'),
                t['full_text']
            )
        )
