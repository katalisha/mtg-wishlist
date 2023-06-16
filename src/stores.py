""" convert the csv file of stores to a list of stores"""

from util.fileio import process_csv_file
from store import Store
from binderpos_store import BinderStore


def load_stores(filepath: str) -> list[Store]:
    return process_csv_file(filepath, convert_row_to_store)


def convert_row_to_store(row: dict[str, str]) -> Store | None:
    if len(row) != 2:
        return None

    try:
        return BinderStore(row["Name"], row["URL"])
    except KeyError:
        return None
