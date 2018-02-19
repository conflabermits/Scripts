# This is a guess-the-number game

import random
import sys

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)
print('DEBUG: Secret number is: ' + str(secretNumber))

for guessesTaken in range(1, 7):
    print('Take a guess.')
    try:
        guess = int(input())
    except ValueError:
        print('It looks like you didn\'t enter a number.')
        sys.exit(1)
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')

