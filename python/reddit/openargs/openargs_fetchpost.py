#!/usr/bin/python3

import sys
sys.dont_write_bytecode = True
import argparse
import praw
import textwrap
from datetime import datetime, timedelta
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
parser.add_argument("-r",
                    "--subreddit",
                    help="Post to specified subreddit",
                    type=str,
                    required=False)
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

args = parser.parse_args()

twitter_account = args.account
reddit_subreddit = args.subreddit
twitter_pull_limit = args.limit * 2
reddit_post_limit = args.limit
hour_limit = args.hours
silent_arg = args.silent
reddit_target_user = args.user

#TWITTER_DATE_FORMAT = '%a %b %d %H:%M:%S +0000 %Y'
DESIRED_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def check_output_method(user_arg, silent_arg):
    if user_arg is None and silent_arg is True:
        print("No output method defined. Exiting.\n")
        sys.exit(2)

check_output_method(reddit_target_user, silent_arg)

def convert_twitter_date_to_date_object(datestring):
    time_tuple = parsedate_tz(datestring.strip())
    dt = datetime(*time_tuple[:6])
    return dt - timedelta(seconds=time_tuple[-1])

reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     username=reddit_username,
                     password=reddit_password,
                     user_agent='python3:openargs_fetchposter:v1.1.0 (by /u/conflabermits)')

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                  consumer_secret=twitter_consumer_secret,
                  access_token_key=twitter_access_token_key,
                  access_token_secret=twitter_access_token_secret,
                  tweet_mode="extended")

twitter_user = twitter_api.VerifyCredentials()

redditSeparator = "\n\n---\n\n"
messageTitle = "Recent tweets from @{0}, {1}".format(twitter_account, (datetime.now() - timedelta(hours = hour_limit)).strftime('%A %B %d'))
messageBody = "Generated at: {0} ET{1}".format(datetime.now().strftime(DESIRED_DATE_FORMAT), redditSeparator)

tweet = twitter_api.GetUserTimeline(screen_name=twitter_account, exclude_replies=True, count=twitter_pull_limit)
tweets = [i.AsDict() for i in tweet]

numTweets = 0

for tweet in tweets:
    dateGateBool = datetime.now() - timedelta(hours = hour_limit) <= datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
    if dateGateBool is True and numTweets < reddit_post_limit:
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
        numTweets += 1
    else:
        break

if numTweets > 0:
    messageBody += 'This is an automated message posted by the openargs_fetchposter (/u/verylegalandcoolbot).\n\n'
    messageBody += 'Tweet times are in [UTC](http://www.timebie.com/std/utc.php).\n\n'
    messageBody += 'For more information contact /u/conflabermits.'

    if silent_arg is False:
        print(messageTitle)
        print(messageBody)
    
    if reddit_target_user is not None:
        if silent_arg is False:
            print("Sending message to /u/{0}".format(reddit_target_user))
        reddit.redditor(reddit_target_user).message(messageTitle, messageBody)
    
    if reddit_subreddit is not None:
        if silent_arg is False:
            print("Posting message to /r/{0}".format(reddit_subreddit))
        reddit.subreddit(reddit_subreddit).submit(messageTitle, selftext=messageBody, send_replies=True)
