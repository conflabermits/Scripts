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
                    default="30")
parser.add_argument("-H",
                    "--hours",
                    help="Find results going back <HOURS> hours",
                    type=int,
                    default="0",
                    required=False)
"""
parser.add_argument("-M",
                    "--minutes",
                    help="Find results going back <MINUTES> minutes",
                    type=int,
                    default="0",
                    required=False)
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
parser.add_argument("-a",
                    "--account",
                    help="Account to grab tweets from",
                    type=str,
                    required=True)

args = parser.parse_args()

twitter_account=args.account

# Resolve argument conflicts
if args.user is None and args.silent is True:
    print("No output method defined. Exiting.\n")
    sys.exit(2)

"""
if args.hours != 0 and args.minutes != 0:
    print("Warning: Both hours and minutes specified.")
    print("They will be combined into a single value.\n")

if args.hours == 0 and args.minutes == 0:
    args.hours = 336
"""


def to_datetime(datestring):
    time_tuple = parsedate_tz(datestring.strip())
    dt = datetime(*time_tuple[:6])
    return dt - timedelta(seconds=time_tuple[-1])

DESIRED_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
#TWITTER_DATE_FORMAT = '%a %b %d %H:%M:%S +0000 %Y'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def utc_2_local(utc_time):
    utc = datetime.utcfromtimestamp(utc_time).strftime(TIME_FORMAT)
    timestamp =  calendar.timegm((datetime.strptime(utc, TIME_FORMAT)).timetuple())
    local = datetime.fromtimestamp(timestamp).strftime(TIME_FORMAT)
    return(local)


reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     username=reddit_username,
                     password=reddit_password,
                     user_agent='openargs_fetchposter/0.1 by verylegalandcoolbot')

api = twitter.Api(consumer_key=twitter_consumer_key,
                  consumer_secret=twitter_consumer_secret,
                  access_token_key=twitter_access_token_key,
                  access_token_secret=twitter_access_token_secret,
                  tweet_mode="extended")

twitter_user = api.VerifyCredentials()

"""
print(
    "Running as user \"{0}\" (handle: {1})\n".format(
        twitter_user.name,
        twitter_user.screen_name
    )
)
"""

#postNumber = 1
#postLimit = args.limit
redditSeparator = "\n\n---\n\n"
messageBody = "Generated at: {0}{1}".format(datetime.now().strftime(TIME_FORMAT), redditSeparator)

t = api.GetUserTimeline(screen_name=twitter_account, exclude_replies=True, count=30)
tweets = [i.AsDict() for i in t]

for t in tweets:
    if 'retweeted_status' in t.keys():
        messageBody += "RT by @{0} ({1}) of @{2} ({3}):\n\n".format(
            t['user']['screen_name'],
            datetime.strftime(to_datetime(t['created_at']), DESIRED_DATE_FORMAT + ' UTC'),
            t['retweeted_status']['user']['screen_name'],
            datetime.strftime(to_datetime(t['retweeted_status']['created_at']), DESIRED_DATE_FORMAT + ' UTC')
        )
        messageBody += textwrap.indent(
            t['retweeted_status']['full_text'],
            "> ",
            lambda line: True
        )
        messageBody += redditSeparator
    else:
        messageBody += "Tweet from @{0} ({1}):\n\n".format(
            t['user']['screen_name'],
            datetime.strftime(to_datetime(t['created_at']), DESIRED_DATE_FORMAT + ' UTC')
        )
        messageBody += textwrap.indent(
            t['full_text'],
            "> ",
            lambda line: True
        )
        messageBody += redditSeparator


"""
def printPost(submission):
    global messageBody
    messageBody += "**Post Number:** {0}\n\n".format(postNumber)
    messageBody += "**Post Title:** {0}\n\n".format(submission.title)
    messageBody += "**Post Date:** {0}\n\n".format(utc_2_local(submission.created_utc))
    messageBody += "**Link To Post:** {0}\n\n".format(submission.shortlink)
    if submission.is_self:
        messageBody += "**Post Selftext:**\n\n"
        messageBody += textwrap.indent(submission.selftext,
                                       "> ",
                                       lambda line: True)
    else:
        messageBody += "**External URL:** {0}\n".format(submission.url)
    messageBody += redditSeparator
"""

"""
for submission in reddit.subreddit(args.subreddit).new(limit=postLimit):
    dateGate = datetime.now() - datetime.timedelta(hours = args.hours, minutes = args.minutes) <= datetime.fromtimestamp(submission.created_utc)
    if dateGate:
        if args.include is None and args.exclude is None:
            printPost(submission)
            postNumber += 1
        else:
            if args.include and args.exclude:
                if (re.search(args.include, submission.title, re.IGNORECASE) or re.search(args.include, submission.selftext, re.IGNORECASE)):
                    if not (re.search(args.exclude, submission.title, re.IGNORECASE) or re.search(args.exclude, submission.selftext, re.IGNORECASE)):
                        printPost(submission)
                        postNumber += 1
            if args.exclude is None and args.include:
                if (re.search(args.include, submission.title, re.IGNORECASE) or re.search(args.include, submission.selftext, re.IGNORECASE)):
                    printPost(submission)
                    postNumber += 1
            if args.include is None and args.exclude:
                if not (re.search(args.exclude, submission.title, re.IGNORECASE) or re.search(args.exclude, submission.selftext, re.IGNORECASE)):
                    printPost(submission)
                    postNumber += 1
    else:
        break
"""

if args.silent is False:
    print(messageBody)

if args.user is not None:
    print("Sending message to /u/{0}".format(args.user))
    reddit.redditor(args.user).message("Most recent tweets from @{0}".format(twitter_account), messageBody)

