# get_first: takes a list[str] as input and returns first element
# remove_first: takes a list[str] as input and removes first element (no return)
# get_and_remove_first: takes a list[str] as input and returns + removes first element


def get_first(input: list[str]) -> str:
    """Return first element of list"""
    if len(input) == 0:
        return ""
    return input[0]


# TEST IT OUT print((get_first)(["eggs", "milk", "bread"]))


def remove_first(input: list[str]) -> None:
    """Remove first element"""
    input.pop(0)


# TEST IT OUT print((remove_first)(["eggs", "milk", "bread"]))


def get_and_remove_first(input: list[str]) -> str:
    """Remove AND return first element"""
    first_element: str = input[0]  # store first element
    input.pop(0)  # remove first element
    return first_element  # return the stored element; first element is not same now


# TEST IT OUT print((get_and_remove_first)(["eggs", "milk", "bread"]))
