"""Testing for functions."""

__author__ = "730553797"

from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Tests for evens."""
    only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    only_evens([1, 5, 3]) == []
    only_evens([4, 4, 4]) == [4, 4, 4]


def test_concat() -> None:
    """Tests for combining two lists."""
    concat([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    concat([3, 5, 7], [9, 1, 2, 3]) == [3, 5, 7, 9, 1, 2, 3]
    concat([1, 2, 3], []) == [1, 2, 3]


def test_sub() -> None:
    """Test for middle of list ints."""
    sub([10, 20, 30, 40], 1, 3) == [20, 30]
    sub([], 1, 2) == []
    sub([10, 20, 30], 1, 5) == [30]