#!/usr/bin/python3
def isupper(c):
    # Check if character is uppercase
    return 65 <= ord(c) <= 90

def uppercase(str):
    for char in str:
        if not isupper(char) and 97 <= ord(char) <= 122:
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print()
