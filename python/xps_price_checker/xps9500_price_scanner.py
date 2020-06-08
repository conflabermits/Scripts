#!/usr/bin/env python3

import os
import sys
import shelve
import argparse
import requests
from bs4 import BeautifulSoup

# Base URL: https://www.dell.com/en-us/member/shop/dell-laptops/new-xps-15-laptop/spd/xps-15-9500-laptop/xn9500cto210s
# URL with 512GB SSD: https://www.dell.com/en-us/member/shop/dell-laptops/new-xps-15-laptop/spd/xps-15-9500-laptop/xn9500cto210s?configurationid=62e03267-650b-4469-be2d-38eda0ba102b

# Example
'''
$ ./xps9500_price_scanner.py -u "https://www.dell.com/en-us/member/shop/dell-laptops/new-xps-15-laptop/spd/xps-15-9500-laptop/xn9500cto210s" -c "abc@xyz.tld" -f "histfile.bin"
Item price is $1714.99
Price is lower by $35.0
'''

# TO DO
# add notification system (email/reddit)
# add min/max price history && add dates to price history
'''
prices = {
    'last': {
        'price': 1714.99
        'date': '2020-05-25'
    },
    'max': {
        'price': 1749.99
        'date': '2020-05-20'
    },
    'min': {
        'price': 1714.99
        'date': '2020-05-22'
    }
}
'''

parser = argparse.ArgumentParser(
    description="Check the price of the Dell XPS 15 9500"
)
parser.add_argument(
    "-u",
    "--url",
    type=str,
    help="URL used to get product info",
    required=True
)
parser.add_argument(
    "-c",
    "--contact",
    type=str,
    default="Python user",
    help="String to include in user agent header as contact info or ID",
    required=False
)
parser.add_argument(
    "-f",
    "--savefile",
    type=str,
    help="Name of file used to store previous price of item",
    required=False
)

args = parser.parse_args()

url = args.url.strip()
if args.savefile:
    save_file = args.savefile
    use_save_file = True
else:
    use_save_file = False
user = args.contact
headers = {"User-Agent": "{0} is looking for a discount".format(user)}

def check_file(file):
    return os.path.isfile(file)

def get_previous_price(file):
    history_file = shelve.open(file)
    previous_price = history_file['previous_price']
    history_file.close()
    return float(previous_price)

def put_new_price(file, new_price):
    history_file = shelve.open(file)
    history_file['previous_price'] = float(new_price)
    history_file.close()
    pass

def get_page(url, headers):
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
    return page

def get_price(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    item_price_str = str(soup.find(attrs={"class": "cf-dell-price"}).contents[1].get_text().strip())
    item_price_float = float(item_price_str.replace(',', '').replace('$', ''))
    return item_price_float

def price_comparison(old_price, new_price):
    if old_price == new_price:
        return str("Price remains the same at ${0}".format(old_price))
    else:
        price_difference = new_price - old_price
        if price_difference > 0:
            price_adjective = 'higher'
        else:
            price_adjective = 'lower'
        return str("Price is {0} by ${1}".format(price_adjective, abs(price_difference)))

def main(url, headers, use_save_file):
    try:
        price_page = get_page(url, headers)
        current_price = get_price(price_page)
        print('Item price is ${0}'.format(current_price))
    except:
        print("No item found at that URL.")
        sys.exit(3)
    if use_save_file:
        if check_file(save_file):
            previous_price = get_previous_price(save_file)
            print(price_comparison(previous_price, current_price))
            put_new_price(save_file, current_price)
        else:
            put_new_price(save_file, current_price)

if __name__ == "__main__":
    main(url, headers, use_save_file)
