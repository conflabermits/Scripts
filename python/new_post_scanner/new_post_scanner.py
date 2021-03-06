#!/usr/bin/env python3

import requests
import argparse
from bs4 import BeautifulSoup
from site_vars import *
import ezgmail

parser = argparse.ArgumentParser(description='Scan website for recent items')
parser.add_argument("-t",
                    "--timescale",
                    type=str,
                    help="Specify how far back to look (e.g., seconds, hours, days, weeks)",
                    default="hours",
                    required=False)
parser.add_argument("-m",
                    "--mailrecipient",
                    type=str,
                    help="Specify an email address to receive results",
                    required=False)

args = parser.parse_args()

time_scale_keyword = args.timescale
time_range_values = ['seconds', 'minutes', 'hours', 'days', 'weeks', 'months', 'years']
scale_value = time_range_values.index(time_scale_keyword) + 1
time_range_list = time_range_values[0:scale_value]

request_url = "{0}{1}{2}".format(site_hostname, site_path, site_query)
request_cookies = dict(site_cookie_list)

r = requests.get(request_url, cookies=request_cookies)
soup = BeautifulSoup(r.text, 'html.parser')

item_names = soup.find_all('a', attrs={'class': site_item_names_class})
item_times = soup.find_all('div', attrs={'class': site_item_times_class})

results = list()
for i in range(0,50):
    item_name = item_names[i].next
    if item_times[i].next.split()[1] == '|':
        item_time = item_times[i].next.split()[3]
    else:
        item_time = item_times[i].next.split()[1]
    if item_time in time_range_list:
        results.append((item_name, item_time))

if len(results) > 0:
    message_body = ''
    for result in results:
        message_body += '* {0}\n'.format(result[0])
    print(message_body)
    #print(results)
    if args.mailrecipient:
        ezgmail.send(args.mailrecipient, 'New posts from {0}'.format(site_hostname), message_body)

