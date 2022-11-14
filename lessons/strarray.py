"""Examples of "vectorized" operations via magic methods."""

from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items
    
    def __repr__(self) -> str:
        return f"StrArray({self.items})"
    
    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: StrArray = StrArray([])
        if isinstance(rhs, str):
            for item in self.items:
                result.items.append(item + rhs)
        else:
            assert len(self.items) == len(rhs.items)
            for item in range(len(self.items)):
                result.items.append(self.items[item] + rhs.items[item])
        return result
    
a: StrArray = StrArray(StrArray(["Armando", "Pete", "Leaky"]))
b: StrArray = StrArray(StrArray(["Bactot", "Nance", "Black"]))
print(a)
print(a + "!")
print(a + " " + b)
print(b + ", " + a + "!")