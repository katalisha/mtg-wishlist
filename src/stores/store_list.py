""" convert the csv file of stores to a list of stores"""

from util.fileio import process_csv_file
from stores.store import Store
from stores.binderpos import BinderStore
from stores.scraper import Scraper
from stores.search_spring import SearchSpringStore
from typing import Optional
from stores.mtgmate_scraper_helper import MtgMateScraperHelper
from enum import Enum


class StoreIdentifier(Enum):
    BINDER_POS = "myshopify.com"
    MTG_MATE = "mtgmate.com.au"
    SEARCH_SPRING = "searchspring.io"


def load_stores(filepath: str) -> list[Store]:
    return process_csv_file(filepath, convert_row_to_store)


def convert_row_to_store(row: dict[str, str]) -> Optional[Store]:
    if len(row) != 2:
        return None

    store_type = [t for t in list(StoreIdentifier) if t.value in row["URL"]]

    try:
        match store_type[0] if store_type else None:
            case StoreIdentifier.BINDER_POS:
                return BinderStore(row["Name"], row["URL"])
            case StoreIdentifier.MTG_MATE:
                return Scraper(row["Name"], MtgMateScraperHelper())
            case StoreIdentifier.SEARCH_SPRING:
                return SearchSpringStore(row["Name"], row["URL"])
            case None:
                raise NotImplementedError

    except KeyError:
        return None
