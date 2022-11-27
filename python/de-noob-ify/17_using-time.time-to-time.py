#!/usr/bin/env python3

import time

def timing_with_time():
    start = time.time()
    time.sleep(1)
    end = time.time()
    print(end - start)

def timing_with_perf_counter():
    start = time.perf_counter()
    time.sleep(1)
    end = time.perf_counter()
    print(end - start)

def main():
    timing_with_time()
    timing_with_perf_counter()

if __name__ == '__main__':
    main()
