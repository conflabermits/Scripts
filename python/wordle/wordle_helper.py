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

def load_words():
    with open('five-letter-words.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

if __name__ == '__main__':

    args = parser.parse_args()

    print('Misses: {0}'.format(args.misses))
    print('Greens: {0}'.format(args.greens))
    print('Yellows: {0}'.format(args.yellows))

    valid_guesses = load_words()
    print(len(valid_guesses))

    narrowed_list=[]

    for guess in valid_guesses:
        potential_guess = True
        for miss_letter in args.misses:
            if miss_letter in guess:
                potential_guess = False
        if potential_guess != False:
            narrowed_list.append(guess)
        
    print(narrowed_list)

    final_list=[]

    for good_guess in narrowed_list:
        print("good_guess = {0}".format(good_guess))
        potential_guess = True
        for green_letter in args.greens:
            slot = int(green_letter[0])
            letter = green_letter[1]
            #print("slot={0} and letter={1}".format(slot, letter))
            #print(good_guess[slot])
            if good_guess[slot - 1] != letter:
                potential_guess = False
        if potential_guess != False:
            final_list.append(good_guess)

    print(final_list)
    print(len(final_list))

    """
    # Ensure input is only alpha
    if not input_letters.isalpha():
        print('Please use only letters A through Z, no numbers or symbols')
        sys.exit(2)

    # Ensure letters are all lowercase
    if not input_letters.islower():
        tmp_letters = input_letters.lower()
        input_letters = tmp_letters
    """
    print('MAIN finished executing!')
