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
                    choices=['biggestword', 'conundrum'],
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

def get_permutations(permutations):
    given_permutations = list()
    new_permutations = list()
    if permutations is list:
        for permutation in permutations:
            given_permutations.append(permutation)
    else:
        given_permutations.append(permutations)
    for permutation in given_permutations:
        for i in range(0, len(permutation)):
            removal_letter = sorted(permutation).pop(i)
            sorted_permutation = sorted(permutation)
            sorted_permutation.remove(removal_letter)
            potential_new_permutation = ''.join(map(str, sorted_permutation))
            if potential_new_permutation not in new_permutations:
                new_permutations.append(potential_new_permutation)
    return new_permutations


if __name__ == '__main__':

    # Assign variables for ease of re-use
    input_letters = args.letters
    input_gametype = args.gametype

    # Ensure input is only alpha
    if not input_letters.isalpha():
        print('Please use only letters A through Z, no numbers or symbols')
        sys.exit(2)

    # Ensure letters are all lowercase
    if not input_letters.islower():
        tmp_letters = input_letters.lower()
        input_letters = tmp_letters

    ## Ensure gametype is selected properly
    #if input_gametype not in ['biggestword', 'conundrum']:
    #    print('Please enter either biggestword or conundrum as the game type')
    #    sys.exit(1)

    english_words = load_words()

    if input_gametype == "conundrum":
        potential_answers = solve_conundrum(input_letters, english_words)
        print('Length of potential_answers: {0}'.format(len(potential_answers)))
        for word in potential_answers:
            print(word)

    if input_gametype == "biggestword":
        potential_answers = solve_conundrum(input_letters, english_words)
        old_combo = input_letters
        while len(potential_answers) == 0:
            new_letter_combos = get_permutations(old_combo)
            for combo in new_letter_combos:
                new_potential_answers = solve_conundrum(combo, english_words)
                for potential_answer in new_potential_answers:
                    if potential_answer not in potential_answers:
                        potential_answers.append(potential_answer)
            old_combo = new_letter_combos
        for word in potential_answers:
            print(word)

