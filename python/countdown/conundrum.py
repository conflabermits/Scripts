#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser(description="Word puzzle solver for Countdown")
parser.add_argument("-l",
                    "--letters",
                    type=str,
                    help="Letters to use",
                    required=True)
parser.add_argument("-t",
                    "--gametype",
                    type=str,
                    help="Either biggestword or conundrum",
                    required=True)

args = parser.parse_args()

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

def solve_conundrum(letters, words):
    valid_answers = list()
    for word in words:
        if len(word) == len(letters):
            if sorted(word) == sorted(letters):
                valid_answers.append(word)
    return valid_answers

if __name__ == '__main__':
    if args.gametype not in ['biggestword', 'conundrum']:
        print('Please enter either biggestword or conundrum as the game type')
        sys.exit(1)

    english_words = load_words()
    print('Length of english_words: {0}'.format(len(english_words)))
    potential_answers = solve_conundrum(args.letters, english_words)
    print('Length of potential_answers: {0}'.format(len(potential_answers)))
    for word in potential_answers:
        print(word)

