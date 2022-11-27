#!/usr/bin/env python3

import logging

def using_print():
    print("debug info")
    print("some more info")
    print("bad error")

def using_logging():
    level = logging.DEBUG
    fmt = '%(asctime)s - [%(levelname)s] - %(message)s'
    logging.basicConfig(level=level, format=fmt)
    logging.debug("debug info")
    logging.info("some more info")
    logging.error("bad error")

def main():
    using_print()
    using_logging()

if __name__ == '__main__':
    main()
