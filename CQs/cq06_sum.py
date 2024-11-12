"""Summing the elements of a list using different loops"""

__author__ = "730473257"


# while loops to iterate
def w_sum(vals: list[float]) -> float:
    idx: int = 0  # goes through list with as idx
    total_sum: float = 0.0
    while idx < len(vals):
        total_sum += vals[idx]
        idx += 1
    return total_sum


# for , in loop
def f_sum(vals: list[float]) -> float:
    total_sum: float = 0.0
    for elem in vals:
        total_sum += elem
    return total_sum


# for, in loop with range use
def f_range_sum(vals: list[float]) -> float:
    total_sum: float = 0.0
    for idx in range(0, len(vals)):
        total_sum += vals[idx]
    return total_sum
