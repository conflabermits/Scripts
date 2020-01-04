#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser(description='Scan the NY&C website for products by string')
parser.add_argument("-q",
                    "--query",
                    type=str,
                    help="String text used to query the NY&C website",
                    required=True)

args = parser.parse_args()

page = requests.get('https://www.nyandcompany.com/search/?Dy=1&Nty=1&Ntp=1&Ntt={0}'.format(args.query))
soup = BeautifulSoup(page.content, 'html.parser')

if soup.find_all(attrs={"class": "resultFound"}):
    soup2 = BeautifulSoup(str(soup.find(id="filteredRecCount")), 'html.parser')
    num_results = soup2.get_text()
    print('{0} results found!'.format(num_results))
else:
    print("No results found.")


