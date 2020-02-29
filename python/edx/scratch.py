#!/usr/bin/env python3

def avg(grades):
    try:
        assert not len(grades) == 0
    except AssertionError:
        print('No grades entered')
        return 0
    return sum(grades)/len(grades)
