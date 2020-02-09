#!/usr/bin/env python3

print('Please think of a number between 0 and 100!')

low_range = 0
high_range = 100
response = ''
guess = round((high_range - low_range) / 2)

while response != 'c':
    print('Is your secret number {0}?'.format(guess))
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ", end='')
    response = input()
    if response not in {'h', 'l', 'c'}:
        print('Sorry, I did not understand your input.')
    if response == 'h':
        high_range = guess
        guess = int((high_range + low_range) / 2)
        #guess = round((high_range + low_range) / 2)
    if response == 'l':
        low_range = guess
        guess = int((high_range + low_range) / 2)
        #guess = round((high_range + low_range) / 2)

print('Game over. Your secret number was: {0}'.format(guess))

