#!/usr/bin/env python3

def range_len_pattern():
    a = [1, 2, 3]
    for i in range(len(a)):
        print(f"Value of a[{i}] is {a[i]}.")

def for_value_in_object():
    b = [4, 5, 6]
    for value in b:
        print(f"Value is {value}.")

def enumerate_index_and_value():
    c = [7, 8, 9]
    for i, v in enumerate(c):
        print(f"Value of c[{i}] is {v}.")

def main():
    range_len_pattern()
    for_value_in_object()
    enumerate_index_and_value()

if __name__ == '__main__':
    main()
