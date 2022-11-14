"""Dictionary test utilities."""

__author__ = "730553797"

from dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Tests for inverted dictionaries."""
    invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}
    invert({'apple': 'cat'}) == {'cat': 'apple'}
    invert({}) == {}


def test_favorite_color() -> None:
    """Tests which color appears the most."""
    favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"
    favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Isaac": "yellow"}) == "yellow"
    favorite_color({"Tracy": "purple", "Neil": "green", "Tam": "purple"}) == "purple"


def test_count() -> None:
    """Counts how many times an item appears."""
    count(["blue", "blue", "red"]) == {"blue": 2, "red": 1}
    count(["time", "money", "work"]) == {"time": 1, "money": 1, "work": 1}
    count([]) == {}