#!/usr/bin/env python3

from tkinter import W


def manually_open_close_file(filename):
    f = open(filename, "w")
    f.write("hello!\n")
    f.close()

def open_file_using_with(filename):
    with open(filename, "w") as f:
        f.write("howdy!\n")

def main():
    manually_open_close_file("2_file1.txt")
    open_file_using_with("2_file2.txt")

if __name__ == '__main__':
    main()
