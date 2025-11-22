#!/usr/bin/python
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    total = 0
    for i in argv:
        total += int(i)
    print(total)
