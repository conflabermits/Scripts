#!/usr/bin/env python3

def not_using_dict_items():
    dict1 = {"a": 1, "b": 2, "c": 3}
    for key in dict1:
        print(f"dict1[{key}] is {dict1[key]}.")

def loop_using_key_and_value():
    dict2 = {"d": 4, "e": 5, "f": 6}
    for key, val in dict2.items():
        print(f"dict2[{key}] is {val}.")

def main():
    not_using_dict_items()
    loop_using_key_and_value()

if __name__ == '__main__':
    main()
