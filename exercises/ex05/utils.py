"""Implement List Utility Functions"""

__author__ = "730273257"


def only_evens(input: list[int]) -> list[int]:
    """Return a list of ints, with only even numbers from input list"""
    nums = []
    # loop through the input list and return any even numbers to the empty list
    for elem in input:
        if elem % 2 == 0:
            nums.append(elem)
    return nums


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Return a subset of the list from start idx to the end idx -1"""
    # Empty list, or lists where start is greater than or equal to end, return []
    if len(a_list) == 0 or start >= len(a_list) or start >= end:
        return []
    if start < 0:  # if the start is less than zero, treat is as such
        start = 0
    # if end is greater than len of list, set it to a_list len
    if end > len(a_list):
        end = len(a_list)
    return a_list[start:end]  # return sublist from start to end-1


def add_at_index(a_list: list[int], add: int, idx: int) -> None:
    if idx < 0 or idx > len(a_list):  # raise error if idx is out of bounds
        raise IndexError("Index is out of bounds for the input list.")
    a_list.insert(idx, add)  # add element as specified index
