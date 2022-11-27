#!/usr/bin/env python3

import subprocess

def subprocess_with_shell_true():
    subprocess.run(
        ["echo $SHELL"],
        shell=True
    )

def subprocess_without_shell():
    subprocess.run(
        ["echo", "$SHELL"]
    )

def main():
    subprocess_with_shell_true()
    subprocess_without_shell() # More secure

if __name__ == '__main__':
    main()
