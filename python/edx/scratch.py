#!/usr/bin/env python3

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x
    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y
    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    def __eq__(self, other):
        return Coordinate.getX(self) == Coordinate.getX(other) and Coordinate.getY(self) == Coordinate.getY(other)
    def __repr__(self):
        return 'Coordinate({0},{1})'.format(self.getX(),self.getY())
