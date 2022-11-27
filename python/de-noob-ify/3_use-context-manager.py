#!/usr/bin/env python3

import socket

def finally_instead_of_context_manager(host, port):
    s = socket.socker(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.sendall(b'Hello, world')
    finally:
        s.close()

def using_context_manager(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'Hello, world')

def main():
    print("Nope, not trying this one")

if __name__ == '__main__':
    main()
