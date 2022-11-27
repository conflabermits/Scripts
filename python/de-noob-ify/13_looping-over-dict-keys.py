#!/usr/bin/env python3

def for_key_in_dict_keys():
    dict1 = {"a": 1, "b": 2, "c": 3}
    for key in dict1.keys():
        print(f"dict1[{key}] has value {dict1[key]}.")

def for_key_in_dict():
    dict2 = {"d": 4, "e": 5, "f": 6}
    for key in dict2:
        print(f"dict2[{key}] has value {dict2[key]}.")

def modify_dict_during_loop():
    dict3 = {"g": 7, "h": 8, "i": 9}
    for key in list(dict3):
        print(f"Zeroing out key {key} in dict3, which was {dict3[key]}.")
        dict3[key] = 0
        print(f"dict3[{key}] now has value {dict3[key]}.")

def main():
    for_key_in_dict_keys()
    for_key_in_dict()
    modify_dict_during_loop()

if __name__ == '__main__':
    main()
