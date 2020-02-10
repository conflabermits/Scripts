#!/usr/bin/env python3

aTup = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTuple = ()
    for tup in aTup[0::2]:
        newTuple += (tup,)
    return newTuple

print(oddTuples(aTup))
