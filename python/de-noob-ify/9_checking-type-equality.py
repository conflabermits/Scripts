#!/usr/bin/env python3

from collections import namedtuple

def checking_type_using_equals():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    if type(p) == tuple: # Liskov substitution violation
        print("It's a tuple")
    else:
        print("It's not a tuple")
    print(f"Type of var 'p' is {type(p)}.")

def checking_type_using_isinstance():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    if isinstance(p, tuple):
        print("It's an instance of tuple")
    else:
        print("It's not an instance of tuple")

def main():
    checking_type_using_equals()
    checking_type_using_isinstance()

if __name__ == '__main__':
    main()
