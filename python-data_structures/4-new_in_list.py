#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # siyahının surətini yarat
    new_list = my_list[:]
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list


if __name__ == "__main__":
    my_list = [1, 2, 3]
    idx = 1
    element = 4
    new_list = new_in_list(my_list, idx, element)
    print(new_list)  # [1, 4, 3]
    print(my_list)   # [1, 2, 3]
