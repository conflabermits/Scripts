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

    # Steps:
        # Collect inputs
        # Load word list into "valid_guesses"
        # Determine which letters are duplicates
            # Duplicate letters can affect logic for misses (makes them location-specific)
            # Duplicate letters can affect logic for yellows (condition might need to be combined, not separate for each letter)
        # valid_guesses - misses = narrowed_list
        # narrowed_list + greens = narrower_list
        # narrower_list + yellows = final_list

    # Collect inputs, display them for sanity
    args = parser.parse_args()
    
    # Account for empty variables
    greens = []
    yellows = []
    misses = []
    if args.greens:
        greens = args.greens
    if args.yellows:
        yellows = args.yellows
    if args.misses:
        misses = args.misses
    
    print('Misses: {0}'.format(misses))
    print('Greens: {0}'.format(greens))
    print('Yellows: {0}'.format(yellows))

    # Load words from dictionary file into array variable
    valid_guesses = load_words()
    #print(len(valid_guesses))

    # Determine which leters are duplicates
    all_letters = []
    for green_arg in greens:
        all_letters.append(green_arg[1])
    for yellow_arg in yellows:
        all_letters.append(yellow_arg[1])
    for missed_letter in misses:
        all_letters.append(missed_letter)
    print("All letters: {0}".format(all_letters))
    checked = set()
    dupes = {letter for letter in all_letters if letter in checked or (checked.add(letter) or False)}
    print("Duplicate letters: {0}".format(dupes))
    #for letter in dupes:
    #    print("Dupe letter: {0}".format(letter))


    # Take the full list,
    # remove anything that has definite missed letters,
    # and spit it out into "narrowed_list"
    narrowed_list=[]
    for guess in valid_guesses:
        potential_guess = True
        for miss_letter in misses:
            if miss_letter in guess and miss_letter not in dupes:
                potential_guess = False
        if potential_guess == True:
            narrowed_list.append(guess)
    #print(narrowed_list)


    # Take the greens, identify slot + letter combo,
    # iterate over them to determine which words have that,
    # and put results into "narrower_list"
    narrower_list=[]
    for good_guess in narrowed_list:
        #print("good_guess = {0}".format(good_guess))
        potential_guess = True
        for green_letter in greens:
            slot = int(green_letter[0])
            letter = green_letter[1]
            #print("slot={0} and letter={1}".format(slot, letter))
            #print(good_guess[slot])
            if good_guess[slot - 1] != letter:
                potential_guess = False
        if potential_guess == True:
            narrower_list.append(good_guess)


    # Take the yellows, identify slot + letter combo,
    # iterate over them to determine which words have that letter,
    # but, importantly, NOT IN THAT SPOT,
    # and put those results into "final_list"
    final_list=[]
    for good_guess in narrower_list:
        potential_guess = True
        for yellow_letter in yellows:
            slot = int(yellow_letter[0])
            letter = yellow_letter[1]
            if letter not in good_guess:
                potential_guess = False
            if good_guess[slot - 1] == letter:
                potential_guess = False
        if potential_guess == True:
            final_list.append(good_guess)


    print("Total suggested guesses: {0}".format(len(final_list)))
    print(sorted(final_list))

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
    #print('MAIN finished executing!')

