#!/usr/bin/env python3

def check_using_equals(x):
    if x == None:
        print(f"x is None")
    if x == True:
        print(f"x is True")
    if x == False:
        print(f"x is False")

def check_using_identity(x):
    if x is None:
        print(f"x is None")
    if x is True:
        print(f"x is True")
    if x is False:
        print(f"x is False")

def main():
    check_using_equals(None)
    check_using_equals(True)
    check_using_equals(False)
    check_using_identity(None)
    check_using_identity(True)
    check_using_identity(False)

if __name__ == '__main__':
    main()
