"""ex08"""

from __future__ import annotations

__author__ = "730473257"


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    # MAGIC METHOD: COVERT OBJECT TO STR
    # rest=self.next.__str__() to str(self.next)
    def __str__(self) -> str:
        """Produce a string representation of a linked list"""
        rest: str = "TODO"
        # TODO: figure out the rest of the list
        # Base Case
        if self.next is None:
            rest = "None"
        # Recursive Case
        else:
            rest = self.next.__str__()
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
# print(one)
# print(str(courses))
# print(courses)


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str"""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
    return f"{head.value} -> {rest}"


# print(to_str(one))
# print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base Case: When head is the "last" node
    if head.next is None:
        return head.value  # Return its value
    # RECURSIVE CASE
    else:
        rest: int = last(head.next)  # Figure out the last node (recursive call)
        return rest  # Return this value!


# print(last(two))
# print(last(one))  # expect to print 2
# print(last(courses))  # expect to print 301


def recursive_range(start: int, end: int) -> Node | None:
    """Build a list recursively from start to end"""
    # Edge Case: raise ValueError("Invalid Arguments")
    if start > end:
        raise ValueError("Invalid Arguments, start > end,")
    # Base case
    if start == end:
        return None
    # Recursive Case
    else:
        # 1 Handle first value in new list
        first: int = start
        # 2 let the rest of the list be handled recursively
        rest: Node | None = recursive_range(start + 1, end)
        # 3 return a new node which is first followed by rest
        return Node(first, rest)


def value_at(head: Node | None, index: int) -> int:
    """Return the data of the Node stored at a given index"""
    # EDGE CASE (if None, raise index error)
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # BASE CASE (return data if index is 0 and we are at target node)
    if index == 0:
        return head.value
    # RECURSIVE CASE (move to next node and decrease index)
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return max data value in linked list."""
    # EDGE CASE (if none, raise error)
    if head is None:
        raise ValueError("Cannot call max with None")
    # Base Case
    if head.next is None:
        return head.value
    # Recursive Case
    max_in_list = max(head.next)
    if head.value > max_in_list:
        return head.value
    else:
        return max_in_list


def linkify(items: list[int]) -> Node | None:
    """Build a list recursively from input."""
    # base case
    if len(items) == 0:
        return None
    else:
        # create node for first elements of items
        first: int = items[0]
        # use linkify to recrursively go through rest of the list
        rest: Node | None = linkify(items[1:])
        # return new node with first value followed by rest
        return Node(first, rest)


def scale(head: Node | None, factor: int) -> Node | None:
    "New linked list that has been scaled by factor."
    # base case
    if head is None:
        return None
    else:
        # start with first node
        scaled_value: int = head.value * factor
        # iteratie through rest of nodes
        rest: Node | None = scale(head.next, factor)
        return Node(scaled_value, rest)
