#!/usr/bin/python3

import sys
sys.dont_write_bytecode = True
import argparse
import praw
import calendar
import textwrap
#import re
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_tz
import twitter
from openargs_twitter_creds import *
from openargs_reddit_creds import *


parser = argparse.ArgumentParser(description='Grab tweets and retweets from a Twitter account and post to a given subreddit')
parser.add_argument("-a",
                    "--account",
                    help="Account to grab tweets from",
                    type=str,
                    required=True)
parser.add_argument("-s",
                    "--silent",
                    help="Suppress terminal output",
                    action='store_true',
                    required=False)
"""
parser.add_argument("-r",
                    "--subreddit",
                    help="Post to specified subreddit",
                    type=str,
                    required=True)
"""
parser.add_argument("-u",
                    "--user",
                    help="Send results to a user via Reddit message",
                    required=False)
parser.add_argument("-l",
                    "--limit",
                    help="Limit results to N tweets (default: %(default)s)",
                    required=False,
                    type=int,
                    default="50")
parser.add_argument("-H",
                    "--hours",
                    help="How far back, in hours, to search for tweets (default: %(default)s)",
                    type=int,
                    default="24",
                    required=False)
"""
parser.add_argument("-i",
                    "--include",
                    help="Only include results matching <STRING>",
                    type=str,
                    required=False)
parser.add_argument("-e",
                    "--exclude",
                    help="Exclude results matching <STRING>",
                    type=str,
                    required=False)
"""

args = parser.parse_args()

twitter_account = args.account
#reddit_subreddit = args.subreddit

if args.user is None and args.silent is True:
    print("No output method defined. Exiting.\n")
    sys.exit(2)

def convert_twitter_date_to_date_object(datestring):
    time_tuple = parsedate_tz(datestring.strip())
    dt = datetime(*time_tuple[:6])
    return dt - timedelta(seconds=time_tuple[-1])

#TWITTER_DATE_FORMAT = '%a %b %d %H:%M:%S +0000 %Y'
DESIRED_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def convert_utc_2_local(utc_time):
    utc = datetime.utcfromtimestamp(utc_time).strftime(DESIRED_DATE_FORMAT)
    timestamp =  calendar.timegm((datetime.strptime(utc, DESIRED_DATE_FORMAT)).timetuple())
    local = datetime.fromtimestamp(timestamp).strftime(DESIRED_DATE_FORMAT)
    return(local)

reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     username=reddit_username,
                     password=reddit_password,
                     user_agent='openargs_fetchposter/0.1 by verylegalandcoolbot')

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                  consumer_secret=twitter_consumer_secret,
                  access_token_key=twitter_access_token_key,
                  access_token_secret=twitter_access_token_secret,
                  tweet_mode="extended")

twitter_user = twitter_api.VerifyCredentials()

redditSeparator = "\n\n---\n\n"
messageBody = "Generated at: {0}{1}".format(datetime.now().strftime(DESIRED_DATE_FORMAT), redditSeparator)

tweet = twitter_api.GetUserTimeline(screen_name=twitter_account, exclude_replies=True, count=args.limit)
tweets = [i.AsDict() for i in tweet]

for tweet in tweets:
    if 'retweeted_status' in tweet.keys():
        messageBody += "RT by @{0} ({1}) of @{2} ({3}):\n\n".format(
            tweet['user']['screen_name'],
            datetime.strftime(convert_twitter_date_to_date_object(tweet['created_at']), DESIRED_DATE_FORMAT + ' UTC'),
            tweet['retweeted_status']['user']['screen_name'],
            datetime.strftime(convert_twitter_date_to_date_object(tweet['retweeted_status']['created_at']), DESIRED_DATE_FORMAT + ' UTC')
        )
        messageBody += textwrap.indent(
            tweet['retweeted_status']['full_text'],
            "> ",
            lambda line: True
        )
        messageBody += redditSeparator
    else:
        messageBody += "Tweet from @{0} ({1}):\n\n".format(
            tweet['user']['screen_name'],
            datetime.strftime(convert_twitter_date_to_date_object(tweet['created_at']), DESIRED_DATE_FORMAT + ' UTC')
        )
        messageBody += textwrap.indent(
            tweet['full_text'],
            "> ",
            lambda line: True
        )
        messageBody += redditSeparator

if args.silent is False:
    print(messageBody)

if args.user is not None:
    print("Sending message to /u/{0}".format(args.user))
    reddit.redditor(args.user).message("Most recent tweets from @{0}".format(twitter_account), messageBody)
