"""Dictionary functions."""

__author__ = "730553797"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary that is inversed."""
    empty = {}
    if x == empty:
        return empty
    for key in x:
        if x[key] in empty:
            raise KeyError("Repeated keys/values")
        empty[x[key]] = key    
    return empty


def favorite_color(x: dict[str, str]) -> str:
    """Returns the color that appears the most."""
    color_count = count(x.values()) 
    result: str = list(color_count.keys())[0]
    for item in list(color_count.keys()):
        if color_count[result] < color_count[item]:
            result = item        
    return result


def count(x: list[str]) -> dict[str, int]:
    """Tracks number of times a value appears."""
    empty = {}
    if x == empty:
        return empty
    for item in x:
        if item in list(empty.keys()):
            empty[item] = empty[item] + 1
        else:
            empty[item] = 1
    return empty