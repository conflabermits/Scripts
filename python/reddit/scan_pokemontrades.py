#!/usr/local/bin/python3

import argparse
import praw
import datetime
# import time
import calendar
import textwrap
import sys
from reddit_creds import *

sys.dont_write_bytecode = True


parser = argparse.ArgumentParser(description='Scan recent posts on /r/pokemontrades/new/')
parser.add_argument("-s",
                    "--silent",
                    help="Suppress terminal output",
                    action='store_true',
                    required=False)
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
                    required=False)
parser.add_argument("-M",
                    "--minutes",
                    help="Find results going back <MINUTES> minutes",
                    type=int,
                    required=False)

args = parser.parse_args()


# Resolve argument conflicts
if (args.user is None and args.silent is True):
    print("No output method defined. Exiting.\n")
    sys.exit(2)

if (args.hours is not None and args.minutes is not None):
    print("Warning: Both hours and minutes specified.")
    print("They will be combined into a single value.\n")


TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def utc_2_local(utc_time):
    utc = datetime.datetime.utcfromtimestamp(utc_time).strftime(TIME_FORMAT)
    #print "utc_2_local: before convert:", utc
    timestamp =  calendar.timegm((datetime.datetime.strptime( utc, TIME_FORMAT)).timetuple())
    local = datetime.datetime.fromtimestamp(timestamp).strftime(TIME_FORMAT)
    #print "utc_2_local: after convert:", local
    return(local)

reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     username=reddit_username,
                     password=reddit_password,
                     user_agent='3dsDeals-Checkbot/0.1 by conflabermits')

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


for submission in reddit.subreddit('pokemontrades').new(limit=postLimit):
    printPost(submission)
    postNumber += 1

if args.silent is False:
    print(messageBody)

if args.user is not None:
    reddit.redditor(args.user).message("Today's Pokemon Trades", messageBody)

