#!/usr/bin/env python3

from re import L


def append_mutable_list(n, l=[]):
    l.append(n)
    return l

def append_immutable_list(n, l=None):
    if l is None:
        l = []
    l.append(n)
    return l

def main():
    print(append_mutable_list(0))
    print(append_mutable_list(1)) # appends previous list with existing value(s)
    print(append_immutable_list(0))
    print(append_immutable_list(1))

if __name__ == '__main__':
    main()
