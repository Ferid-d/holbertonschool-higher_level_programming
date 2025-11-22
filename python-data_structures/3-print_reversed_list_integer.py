#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    for i in range(a):
        c = my_list[a - 1 - i]
        print("{:d}".format(c))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
