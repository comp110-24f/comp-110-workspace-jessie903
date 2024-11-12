"""Mutating functions."""

__author__ = "730473257"


def manual_append(list_int: list[int], num: int) -> None:
    """Manually append lists"""
    list_int.append(num)


def double(list_int2: list[int]) -> None:
    """Mutate input by looping through list and (x) every element in list[int] by 2"""
    idx: int = 0
    while idx < len(list_int2):
        list_int2[idx] *= 2  # the *= multiplies values, and then adds to list
    idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
