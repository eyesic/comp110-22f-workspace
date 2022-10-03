"""List Exercise."""

__author__ = "730553797"


def all(int_list: list[int], number: int) -> bool:
    """Checks if an int is in the list."""
    i: int = 0
    if len(int_list) == 0:
        return False
    while i < len(int_list):
        if number != int_list[i]: 
            return False
        i += 1
    return True


def max(int_list: list[int]) -> int:
    """Defines the maximum int in a list."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    number: int = int_list[i]
    while i < len(int_list):
        if number < int_list[i]:
            number = int_list[i]
        i += 1
    return number


def is_equal(int_list: list[int], list_ints: list[int]) -> bool:
    """Checks if two lists are equal to each other."""
    i: int = 0
    if len(int_list) != len(list_ints):
        return False
    while i < len(int_list):
        if int_list[i] != list_ints[i]:
            return False
        i += 1
    return True
    