#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Find the longest alphabetical substring for a given string")
parser.add_argument("-s",
                    "--string",
                    type=str,
                    help="given string",
                    required=True)

args = parser.parse_args()

s = args.string

alpha_sorted = "abcdefghijklmnopqrstuvwxyz"
sub_start = 0
sub_end = 1
longest_substring = ""
result = s[0]

while sub_end < len(s):
    if alpha_sorted.find(s[sub_end-1]) <= alpha_sorted.find(s[sub_end]):
        sub_end += 1
        longest_substring = s[sub_start:sub_end]
        if len(longest_substring) > len(result):
            result = longest_substring
    else:
        sub_start = sub_end
        sub_end += 1

print("Longest substring in alphabetical order is:", result)

