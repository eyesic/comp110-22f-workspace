"""Dictionary related utility functions."""

__author__ = "730553797"

from csv import DictReader

DATA_DIRECTORY = "../../data"
DATA_FILE_PATH = f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of the csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produces a new table with only first N rows."""
    empty: dict[str, list[str]] = {}

    for column in table:
        i: int = 0
        empty_list: list[str] = []
        for item in table[column]:
            if i < N:
                empty_list.append(item)
                i += 1
            empty[column] = empty_list

    return empty


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produces a new table with a specific subset."""
    empty: dict[str, list[str]] = {}

    for item in names:
        empty[item] = table[item]
        
    return empty


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables."""
    empty: dict[str, list[str]] = {}

    for key1 in table_1:
        empty[key1] = table_1[key1]

    for key2 in table_2:
        if key2 in empty:
            empty[key2] += table_2[key2]
        else: 
            empty[key2] = table_2[key2]
    return empty


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