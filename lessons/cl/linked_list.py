"""Practice with recursive functions"""

from __future__ import annotations


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
        if self.next is None:
            rest = "None"
        else:
            rest = self.next.__str__()
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
print(one)
print(str(courses))
print(courses)


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str"""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
    return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base Case: When head is the "last" node
    print(f"Enter last ({head.value})")
    if head.next is None:
        return head.value  # Return its value
    # RECURSIVE CASE
    else:
        rest: int = last(head.next)  # Figure out the last node (recursive call)
        print(f"Return recur : {head.value} -> {rest}")
        return rest  # Return this value!


print(last(two))
print(last(one))  # expect to print 2
print(last(courses))  # expect to print 301
