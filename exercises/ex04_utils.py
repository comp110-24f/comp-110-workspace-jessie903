"""Implementation of algorithims to practice computational thinking"""

__author__ = "730273257"


def all(nums: list[int], num: int) -> bool:
    # If list is empty, return False
    if len(nums) == 0:
        return False
    # loop thorugh numbers in list, return true or false depending on list content
    for elem in nums:
        if elem != num:
            return False
    return True  # if num == nums, return True


def max(numbers: list[int]) -> int:
    """Finds max value in list"""
    # If there is no list, raise ValueError
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")
    max_value = numbers[0]
    # loop through elements to find max value
    for elem in numbers:
        if elem > max_value:
            max_value = elem
    return max_value


def is_equal(num1: list[int], num2: list[int]) -> bool:
    "Tells if every element at every index is equal in both lists"
    # return false if not equal lists
    if len(num1) != len(num2):
        return False
    # loops through lists to compare elems
    for idx in range(len(num1)):
        if num1[idx] != num2[idx]:
            return False
    return True


def extend(num1: list[str], num2: list[str]) -> None:
    # for every num in list 2, add to list 1
    for idx in range(len(num2)):
        num1.append(num2[idx])
