#!/usr/bin/env python3

def fizzBuzz(num):
    if not isinstance(num, int):
        return str(num)
    elif num < 1:
        return str(num)
    elif num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)
