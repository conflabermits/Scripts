#!/usr/bin/python3

import sys
sys.dont_write_bytecode = True
import argparse
import praw
import datetime
import calendar
import textwrap
import re
from reddit_creds import *


parser = argparse.ArgumentParser(description='Scan recent posts on a given subreddit')
parser.add_argument("-s",
                    "--silent",
                    help="Suppress terminal output",
                    action='store_true',
                    required=False)
parser.add_argument("-r",
                    "--subreddit",
                    help="Look for posts on <SUBREDDIT>",
                    type=str,
                    required=True)
parser.add_argument("-u",
                    "--user",
                    help="Send results to <USER> via Reddit message",
                    required=False)
parser.add_argument("-l",
                    "--limit",
                    help="Limit results to N posts (default: %(default)s)",
                    required=False,
                    type=int,
                    default="5")
parser.add_argument("-H",
                    "--hours",
                    help="Find results going back <HOURS> hours",
                    type=int,
                    default="0",
                    required=False)
parser.add_argument("-M",
                    "--minutes",
                    help="Find results going back <MINUTES> minutes",
                    type=int,
                    default="0",
                    required=False)
parser.add_argument("-f",
                    "--filter",
                    help="Filter results using string <FILTER>",
                    type=str,
                    required=False)

args = parser.parse_args()


# Resolve argument conflicts
if args.user is None and args.silent is True:
    print("No output method defined. Exiting.\n")
    sys.exit(2)

if args.hours != 0 and args.minutes != 0:
    print("Warning: Both hours and minutes specified.")
    print("They will be combined into a single value.\n")

if args.hours == 0 and args.minutes == 0:
    args.hours = 336


TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def utc_2_local(utc_time):
    utc = datetime.datetime.utcfromtimestamp(utc_time).strftime(TIME_FORMAT)
    timestamp =  calendar.timegm((datetime.datetime.strptime(utc, TIME_FORMAT)).timetuple())
    local = datetime.datetime.fromtimestamp(timestamp).strftime(TIME_FORMAT)
    return(local)


reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     username=reddit_username,
                     password=reddit_password,
                     user_agent='reddit-checkbot/0.1 by reddit-checkbot')

postNumber = 1
postLimit = args.limit
redditSeparator = "\n\n---\n\n"
messageBody = "Generated at: {0}{1}".format(datetime.datetime.now().strftime(TIME_FORMAT), redditSeparator)


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


for submission in reddit.subreddit(args.subreddit).new(limit=postLimit):
    if datetime.datetime.now() - datetime.timedelta(hours = args.hours, minutes = args.minutes) <= datetime.datetime.fromtimestamp(submission.created_utc):
        if args.filter is None:
            printPost(submission)
            postNumber += 1
        else:
            if re.search(args.filter, submission.title, re.IGNORECASE) or re.search(args.filter, submission.selftext, re.IGNORECASE):
                printPost(submission)
                postNumber += 1
    else:
        break

if args.silent is False and postNumber > 1:
    print(messageBody)

if args.user is not None and postNumber > 1:
    reddit.redditor(args.user).message("Most recent posts from /r/{0}".format(args.subreddit), messageBody)

