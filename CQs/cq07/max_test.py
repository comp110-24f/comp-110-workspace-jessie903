from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    """find_and_remove_max returns max value"""
    num1: list[int] = [12, 32, 45]
    assert find_and_remove_max(num1) == 45  # checks that max value is returned


def test_find_and_remove_max_behavior() -> None:
    """remove max element from list"""
    num1: list[int] = [12, 32, 35]
    find_and_remove_max(num1)
    assert num1 == [12, 32]  # checks that max value has been removed form list


def test_find_and_remove_max_edge() -> None:
    """function should return correct value in case of wrong input"""
    assert find_and_remove_max([]) == -1  # checks that is list is empty, return -1
