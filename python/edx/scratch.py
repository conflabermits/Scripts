#!/usr/bin/env python3

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, otherSet):
        """Returns a new intSet of integers that appear in both s1 and s2"""
        newSet = intSet()
        for x in (self.vals and otherSet.vals):
            if self.member(x) and otherSet.member(x):
                newSet.insert(x)
        return newSet

    def __len__(self):
        """Returns the length of the object, an integer >= 0"""
        return len(self.vals)

x = intSet()
y = intSet()
x.insert(1)
y.insert(2)
x.insert(3)
y.insert(3)
x.insert(4)
y.insert(5)
x.insert(6)
y.insert(6)

