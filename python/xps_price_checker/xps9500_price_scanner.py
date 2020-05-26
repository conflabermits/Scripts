#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup
import sys
import price_history

# Base URL: https://www.dell.com/en-us/member/shop/dell-laptops/new-xps-15-laptop/spd/xps-15-9500-laptop/xn9500cto210s
# URL with 512GB SSD: https://www.dell.com/en-us/member/shop/dell-laptops/new-xps-15-laptop/spd/xps-15-9500-laptop/xn9500cto210s?configurationid=62e03267-650b-4469-be2d-38eda0ba102b

# TO DO
# implement price history file
'''
$ python3
Python 3.6.9 (default, Nov  7 2019, 10:44:02)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import shelve
>>> price_history = shelve.open('price_history')
>>> print(price_history['previous_price'])
1714.99
>>> price_history['previous_price'] = 1749.99
>>> print(price_history['previous_price'])
1749.99
>>> price_history.close()
'''
# make file check
'''
$ python3
Python 3.6.9 (default, Nov  7 2019, 10:44:02)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.path.isfile('price_history')
True
'''
# make functions, main block, etc.
# add notification system (email/reddit)

parser = argparse.ArgumentParser(description="Check the price of the Dell XPS 15 9500")
parser.add_argument("-u",
                    "--url",
                    type=str,
                    help="URL used to get product info",
                    required=True)
parser.add_argument("-c",
                    "--contact",
                    type=str,
                    default="Python user",
                    help="String to include in user agent header as contact info or ID",
                    required=False)

args = parser.parse_args()

url = args.url.strip()
user = args.contact
headers = {"User-Agent": "{0} is looking for a discount".format(user)}

try:
    page = requests.get(url, headers=headers)
except:
    print('There was a problem reaching the URL: {0}'.format(url))
    sys.exit(1)

try:
    page.raise_for_status()
except Exception as exc:
    print('There was a problem with the response from the URL: {0}'.format(exc))
    sys.exit(2)

soup = BeautifulSoup(page.content, 'html.parser')

try:
    item_price_str = str(soup.find(attrs={"class": "cf-dell-price"}).contents[1].get_text().strip())
    print("Price is: {}".format(item_price_str))
    item_price_float = float(item_price_str.replace(',', '').replace('$', ''))
    previous_price = float(price_history.previous_price)
    print("Price was: {}".format(previous_price))
    price_difference = item_price_float - previous_price
    if item_price_float == previous_price:
        print("Price remains the same at ${0}".format(item_price_float))
    else:
        if item_price_float - previous_price > 0:
            price_adjective = "higher"
        else:
            price_adjective = "lower"
        print("Price is {0} by ${1}".format(price_adjective, abs(price_difference)))
except:
    print("No item found at that URL.")
    sys.exit(3)
