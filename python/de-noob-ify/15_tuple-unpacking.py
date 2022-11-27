#!/usr/bin/env python3

def not_using_tuple_unpacking():
    mytuple = 1, 2
    x = mytuple[0]
    y = mytuple[1]
    print(f"x equals {x} and y equals {y}.")

def using_tuple_unpacking():
    mytuple = 3, 4
    x, y = mytuple
    print(f"x equals {x} and y equals {y}.")

def main():
    not_using_tuple_unpacking()
    using_tuple_unpacking()

if __name__ == '__main__':
    main()
