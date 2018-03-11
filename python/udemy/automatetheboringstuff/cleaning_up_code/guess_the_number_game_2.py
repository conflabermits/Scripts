# This is a guess-the-number game

import random
import sys

def run_game():
    secretNumber = get_secret_number()
    greet_user()
    name = input()
    guess, guessesTaken = take_guesses(name, secretNumber)
    return_results(name, secretNumber, guess, guessesTaken)

def get_secret_number():
    secretNumber = random.randint(1, 20)
    return secretNumber

def greet_user():
    print('Hello. What is your name?')

def check_guess(guess, secretNumber):
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')

def take_guesses(name, secretNumber):
    print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
    for guessesTaken in range(1, 7):
        print('Take a guess.')
        try:
            guess = int(input())
        except ValueError:
            print('It looks like you didn\'t enter a number.')
            sys.exit(1)
        check_guess(guess, secretNumber)
        if guess == secretNumber:
            break
    return guess, guessesTaken

def return_results(name, secretNumber, guess, guessesTaken):
    if guess == secretNumber:
        print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')

run_game()
