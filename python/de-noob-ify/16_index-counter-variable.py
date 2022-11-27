#!/usr/bin/env python3

def creating_index_counter_variable():
    l1 = [1, 2, 3]
    i = 0
    for x in l1:
        print(f"Item {i} in l1 equals {x}.")
        i += 1

def using_enumerate():
    l2 = [4, 5, 6]
    for i, x in enumerate(l2):
        print(f"Item {i} in l2 equals {x}.")

def main():
    creating_index_counter_variable()
    using_enumerate()

if __name__ == '__main__':
    main()
