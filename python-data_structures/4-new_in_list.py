#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return my_list


if __name__ == "__main__":
    idx = 3
    element = 9
    my_list = [1,2,3,4,5]
    new_list = my_list
    new_in_list(my_list)

