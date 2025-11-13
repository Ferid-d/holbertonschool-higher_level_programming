#!/usr/bin/python3
alphabet = ""
for i in range(97, 123):
    if chr(i) != "q" and chr(i) != "e":
        alphabet += chr(i)
print("{}".format(alphabet), end="")
