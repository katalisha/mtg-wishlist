""" convert the wishlist to a list of cards"""

from util.fileio import process_csv_file
from card import Card, Printing
from typing import cast, get_args


def load_cards(filepath: str) -> list[Card]:
    return process_csv_file(filepath, convert_row_to_card, 1)


def convert_row_to_card(row: dict[str, str]) -> Card | None:
    if len(row) != 11:
        return None

    try:
        if row["Printing"] not in get_args(Printing):
            return None
        else:
            printing = cast(Printing, row["Printing"])

        return Card(row["Card Name"], row["Set Name"], row["Card Number"], printing)
    except KeyError:
        return None
