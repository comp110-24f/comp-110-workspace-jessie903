__author__ = "730473257"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0  # stores number of times we encounter search_char
    index: int = 0  # what letter are we at
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count
