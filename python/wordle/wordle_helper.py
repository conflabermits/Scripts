#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Wordle helper")
parser.add_argument("-m",
                    "--misses",
                    nargs='+',
                    help="A list of letters already guessed that aren't in the word",
                    required=True)
parser.add_argument("-g",
                    "--greens",
                    nargs='*',
                    help="A list of letters that returned green and where they are",
                    required=False)
parser.add_argument("-y",
                    "--yellows",
                    nargs='*',
                    help="A list of letters that returned yellow and where they are",
                    required=False)

args = parser.parse_args()

print('Misses: {0}'.format(args.misses))
print('Greens: {0}'.format(args.greens))
print('Yellows: {0}'.format(args.yellows))
