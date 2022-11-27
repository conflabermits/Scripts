#!/usr/bin/env python3

def bare_except():
    while True:
        try:
            s = input("Input a number: ")
            x = int(s)
            break
        except:  #Problem: can't Ctrl+C to exit!
            print("Not a number, try again")

def better_except():
    while True:
        try:
            s = input("Input a number: ")
            x = int(s)
            break
        except Exception:
            print("Not a number, try again")

def best_except():
    while True:
        try:
            s = input("Input a number: ")
            x = int(s)
            break
        except ValueError:
            print("Not a number, try again")


def main():
    print("At least call out Exception, or try to specify the type of error")

if __name__ == '__main__':
    main()
