#!/usr/bin/env python3

'''
Use numpy for array operations.
Use pandas for data analysis.
'''

import numpy as np
import time

def not_using_numpy():
    start = time.perf_counter()
    x = list(range(20000000))
    y = list(range(20000000))
    s = [a + b for a, b in zip(x, y)]
    end = time.perf_counter()
    print(f"Not using numpy: {end - start}")

def using_numpy():
    start = time.perf_counter()
    x = np.arange(20000000)
    y = np.arange(20000000)
    s = x + y
    end = time.perf_counter()
    print(f"Using numpy: {end - start}")


def main():
    not_using_numpy()
    using_numpy()

if __name__ == '__main__':
    main()
