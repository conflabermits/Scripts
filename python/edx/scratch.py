#!/usr/bin/env python3

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        return char == aStr
    
    midChar = aStr[(len(aStr)//2)]
    if char == midChar:
        return True
    else:
        if char < midChar:
            newStr = aStr[0:(len(aStr)//2)]
        else:
            newStr = aStr[(len(aStr)//2):]
        return isIn(char,newStr)

