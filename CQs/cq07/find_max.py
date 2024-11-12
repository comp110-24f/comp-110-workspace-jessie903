__author__ = "730473257"


def find_and_remove_max(num1: list[int]) -> int:
    while len(num1) == 0:
        return -1
    max_num = num1[0]  # returns max value
    for elem in num1:
        if elem > max_num:
            max_num = elem
    index: int = 0  # removes all instances of max value
    while index < len(num1):
        if num1[index] == max_num:
            num1.pop(index)
        else:
            index += 1
    return max_num  # return the max value
