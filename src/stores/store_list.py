""" convert the csv file of stores to a list of stores"""

from util.fileio import process_csv_file
from stores.store import Store
from stores.binderpos import BinderStore
from stores.scraper import Scraper
from typing import Optional
from stores.mtgmate_scraper_helper import MtgMateScraperHelper


def load_stores(filepath: str) -> list[Store]:
    return process_csv_file(filepath, convert_row_to_store)


def convert_row_to_store(row: dict[str, str]) -> Optional[Store]:
    if len(row) != 2:
        return None

    try:
        if row["URL"] == "www.mtgmate.com.au":
            return Scraper(row["Name"], MtgMateScraperHelper())
        else:
            return BinderStore(row["Name"], row["URL"])
    except KeyError:
        return None
