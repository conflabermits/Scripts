#!/usr/bin/env python3

def manual_str_formatting(field1, field2):
    print('This combines the string "' + field1 + '" with the string "' + field2 + '" using manual formatting.')

def f_str_formatting(field1, field2):
    print(f'This combines the string "{field1}" with the string "{field2}" using f-string formatting.')

def main():
    manual_str_formatting("hello", "world")
    f_str_formatting("howdy", "folks")

if __name__ == '__main__':
    main()
