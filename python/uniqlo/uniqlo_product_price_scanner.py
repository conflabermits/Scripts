#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup
import sys

#NAVY:  https://www.uniqlo.com/on/demandware.store/Sites-UniqloUS-Site/default/Product-Variation?pid=420942&dwvar_420942_color=COL69
#WHITE: https://www.uniqlo.com/on/demandware.store/Sites-UniqloUS-Site/default/Product-Variation?pid=420942&dwvar_420942_color=COL00
#BLACK: https://www.uniqlo.com/on/demandware.store/Sites-UniqloUS-Site/default/Product-Variation?pid=420942&dwvar_420942_color=COL09
#WHITE-MEDIUM: https://www.uniqlo.com/on/demandware.store/Sites-UniqloUS-Site/default/Product-Variation?pid=420942&dwvar_420942_size=SMA004&dwvar_420942_color=COL00

#LOOKING-FOR: <span class="price-sales pdp-space-price sale-price-only" itemprop="price">29.90</span>
#IN: <div class="product-price" itemprop="offers" itemscope="" itemtype="http://schema.org/Offer">
#IN: <div class="seoproduct" itemscope="" itemtype="http://schema.org/Product">

'''
Examples:

$ python3 python/uniqlo/uniqlo_product_price_scanner.py --url "https://www.uniqlo.com/on/demandware.store/Sites-UniqloUS-Site/default/Product-Variation?pid=420942&dwvar_420942_size=&dwvar_420942_color=COL69"
Item price is 29.90

$ python3 python/uniqlo/uniqlo_product_price_scanner.py --url "https://www.uniqlo.com/on/demandware.store/Sites-UniqloUS-Site/default/Product-Variation?pid=418797&dwvar_418797_size=SMA004&dwvar_418797_color=COL09"
Item price is 24.90

$ python3 python/uniqlo/uniqlo_product_price_scanner.py --url " https://wwwx.uniqlo.com/on/demandware.store/Sites-UniqloUS-Site/default/Product-Variation?pid=420942&dwvar_420942_size=SMA004&dwvar_420942_color=COL00" 
There was a problem reaching the URL: https://wwwx.uniqlo.com/on/demandware.store/Sites-UniqloUS-Site/default/Product-Variation?pid=420942&dwvar_420942_size=SMA004&dwvar_420942_color=COL00

$ python3 python/uniqlo/uniqlo_product_price_scanner.py --url " https://www.uniqlo.com/404" 
There was a problem with the response from the URL: 404 Client Error: Not Found for url: https://www.uniqlo.com/404

$ python3 python/uniqlo/uniqlo_product_price_scanner.py --url " https://www.uniqlo.com/us/en/home/"
No item found at that URL.
'''

parser = argparse.ArgumentParser(description="Check the price of a product on the Uniqlo site")
parser.add_argument("-u",
                    "--url",
                    type=str,
                    help="Uniqlo URL used to get product info",
                    required=True)

args = parser.parse_args()

url = args.url.strip()
headers = {"User-Agent": "Just someone learning python"}

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
    item_price = str(soup.find(attrs={"class": "price-sales pdp-space-price sale-price-only"}).contents[0])
except:
    print("No item found at that URL.")
    sys.exit(3)

if item_price:
    print("Item price is {0}".format(item_price))

