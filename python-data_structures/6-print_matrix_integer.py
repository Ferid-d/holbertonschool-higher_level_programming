#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i != 0:
                print(" ", end="")  # print space between numbers
            print("{:d}".format(num), end="")  # print integer with format
        print()  # new line after each row
