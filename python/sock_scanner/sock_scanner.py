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
    print("Results found!")
    print(soup.find_all(attrs={"class": "resultFound"}))
else:
    print("No results found")


