#!/usr/local/bin/python3

import praw
import datetime
import time
import calendar
import textwrap
import sys
sys.dont_write_bytecode = True
from reddit_creds import *
#import pprint
#import argparse


#parser = argparse.ArgumentParser(description='Check for recent posts on /r/3DSdeals/new/')
#parser.add_argument("-p", "--password", nargs='1', required=True)
#
#args = parser.parse_args()

###def parse_args():
###    parser = optparse.OptionParser()
###    parser.add_option("-H", "--hostname",
###                      type="str",
###                      help="The hostname to be connected to.")
###    parser.add_option("-P", "--port",
###                      default="8983",
###                      type="str",
###                      help="Port to use to connect to the client.")
###    parser.add_option("-u", "--uri",
###                      type="str",
###                      default="solr",
###                      help="solr uri")
###    parser.add_option("-c", "--critical",
###                      default="300",
###                      type="int",
###                      help="Seconds since last modified time to consider critical")
###    parser.add_option("-w", "--warning",
###                      default="120",
###                      type="int",
###                      help="Seconds since last modified time to consider warning")
###    parser.add_option("-v", "--verbose",
###                      action='store_true',
###                      help='Print more verbose error messages.')
###    options, args = parser.parse_args()
###
###    if not options.hostname:
###        parser.print_help()
###        parser.error("Hostname is required for use.")
###
###    options.uri = options.uri.lstrip('/')
###
###    return options

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
postLimit = 5
#postSeparator = "=" * 140 + "\n"
redditNewline = "\n\n"
redditSeparator = "\n\n---\n\n"
messageBody = "^Generated at: {0}{1}".format(datetime.datetime.now().strftime(TIME_FORMAT), redditSeparator)
#messageBody += datetime.datetime.now().strftime(TIME_FORMAT) + redditNewline

for submission in reddit.subreddit('3DSdeals').new(limit=postLimit):
    #messageBody += "\n"
    messageBody += "**Post Number:** {0}\n\n".format(postNumber)
    messageBody += "**Post Title:** {0}\n\n".format(submission.title)
    messageBody += "**Post Date:** {0}\n\n".format(utc_2_local(submission.created_utc))
    messageBody += "**Link To Post:** {0}\n\n".format(submission.shortlink)
    if submission.is_self:
        messageBody += "**Post Selftext:**\n\n"
        messageBody += textwrap.indent(submission.selftext,
                             #"             |  ",
                             #"    ",
                             "> ",
                             lambda line: True)
    else:
        messageBody += "**External URL:** {0}\n".format(submission.url)
    messageBody += redditSeparator
    #if postNumber < postLimit:
    #    messageBody += postSeparator
    postNumber += 1

reddit.redditor('conflabermits').message("Today's 3DS Deals", messageBody)
#print(messageBody)



#pprint.pprint(vars(submission))
