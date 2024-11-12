"""Unit tests for only_evens, sub, and add_at_index"""

__author__ = "730473257"

from exercises.ex05.utils import only_evens, sub, add_at_index


# UNIT TESTS FOR ONLY_EVENS
def test_only_evens_case_1():
    """Test that onle_evens returns only even numbers"""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_only_evens_case_2():
    """Test for lists that have no evens"""
    assert only_evens([1, 3, 5]) == []


def test_only_evens_edge_case():
    """Test an empty list"""
    assert only_evens([]) == []


# UNIT TEST FOR SUB
def test_sub_case_1():
    """Test a valid range"""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_case_2():
    """Test sub with a range that exceeds list len"""
    assert sub([10, 20, 30, 40], 0, 10) == [10, 20, 30, 40]


def test_sub_edge_case():
    """Test sub with an empty list"""
    assert sub([], 0, 1) == []


# UNIT TEST FOR ADD_AT_INDEX
import pytest


def test_add_at_index_case_1():
    """Test that function adds element at correct idx"""
    a_list = [1, 2, 3]
    add_at_index(a_list, 4, 3)
    assert a_list == [1, 2, 3, 4]


def test_add_at_index_case_2():
    """Test that function adds at the start of the list"""
    a_list = [2, 3]
    add_at_index(a_list, 1, 0)
    assert a_list == [1, 2, 3]


def test_add_at_index_edge_case():
    """Test that IndexError is raised when list is empty"""
    a_list = []
    with pytest.raises(IndexError):
        add_at_index(a_list, 4, 10)
