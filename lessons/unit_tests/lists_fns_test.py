from lessons.unit_tests.list_fns import get_first, remove_first  # type: ignore


# start with test_
def test_get_first() -> None:
    """get_first should return first element"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert get_first(dog_breeds) == "husky"


# desired return value
def test_remove_first_return_value() -> None:
    """remove_first should return None."""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert remove_first(dog_breeds) == None


# desired behavior
def test_remove_first_behavior() -> None:
    """remove first element from input list"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    remove_first(dog_breeds)
    assert dog_breeds == ["golden", "poodle", "lab"]


def test_get_first_edge_case() -> None:
    """get_first called on empty list should return ""."""
    assert get_first([]) == ""


def test_get_first_edge_case2() -> None:
    """get_first called on empty list should return ""."""
    inp: str = ""
    assert get_first(inp) == ""  # type: ignore
