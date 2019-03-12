#!/usr/bin/python2.7

import sys
from optparse import OptionParser

def main():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-a", "--arg1",
                      help="First Argument")
    parser.add_option("-b", "--arg2",
                      help="Second Argument",)
    (options, args) = parser.parse_args()

    print options
    print args

if __name__ == '__main__':
    print "Running main"
    main()
    print "Done running main"

