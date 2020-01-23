#!/usr/bin/env python3

# Using data from https://pokemondb.net/pokedex/game/sword-shield

import argparse
import requests
from bs4 import BeautifulSoup
import sys

parser = argparse.ArgumentParser(description="Get a neatly organized list of all pokemon from a pokemondb.net URL")
parser.add_argument("-u",
                    "--url",
                    type=str,
                    help="PokemonDB.net URL used to get pokemon info",
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
pokemon_infocards = soup.find_all('div', attrs={"class": "infocard"})

for i, infocard in enumerate(pokemon_infocards):
    infocard_soup = BeautifulSoup(str(infocard), 'html.parser')
    poketext = infocard_soup.get_text().split()
    if len(poketext[2:]) > 1:
        poketype = '{0},{1}'.format(poketext[2], poketext[-1])
    else:
        poketype = poketext[2]
    print('{0},{1},{2}'.format(poketext[0], poketext[1], poketype))

