"""List utility functions."""

__author__ = "730553797"


def only_evens(x: list[int]) -> list:
    """Function that prints even integers into a list."""
    even_numbers = []
    for item in x:
        if item % 2 == 0:
            even_numbers.append(item)
    return even_numbers


def concat(x: list[int], y: list[int]) -> list:
    """Function that combines two lists."""
    empty = []
    for item in x:
        empty.append(item)
    for item in y:
        empty.append(item)
    return empty


def sub(x: list[int], start: int, end: int) -> list:
    """Function that returns values in the middle of the list."""
    empty = []

    if start < 0:
        start = 0
    
    if end > len(x):
        end = len(x)
    
    if len(x) == 0 or start > len(x) or end <= 0:
        return empty

    i = start
    while i < end:
        empty.append(x[i])
        i += 1
    return empty