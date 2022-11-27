#!/usr/bin/env python3

def check_using_bool(x):
    if bool(x):
        print(f"{x} passes 'if bool' check")

def check_using_len(x):
    if len(x) != 0:
        print(f"{x} passes 'if length' check")

def check_directly(x):
    if x:
        print(f"{x} passes bare 'if' check")

def main():
    check_using_bool(True)
    check_using_len([0, 1])
    check_directly(True)
    check_directly([0, 1])

if __name__ == '__main__':
    main()
