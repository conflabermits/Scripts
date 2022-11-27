#!/usr/bin/env python3

def never_using_comprehensions():
    squares = {}
    for i in range(0, 11):
        squares[i] = i * i
    print(squares)

def using_comprehension():
    odd_squares = {i: i * i for i in range(1, 10, 2)}
    print(odd_squares)

def example_comprehensions():
    examples = '''
    dict_comp = {i: i * i for i in range(10)}
    list_comp = [x * x for x in range(10)]
    set_comp = {i % 3 for i in range(10)}
    gen_comp = (2 * x + 5 for x in range(10))
    '''
    return examples

def main():
    never_using_comprehensions()
    using_comprehension()
    print(example_comprehensions())

if __name__ == '__main__':
    main()
