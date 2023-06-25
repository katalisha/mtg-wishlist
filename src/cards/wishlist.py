""" convert the wishlist csv to a list of Cards"""

from util.fileio import process_csv_file
from cards.card import Card, Printing
from typing import cast, get_args, Optional


def load_cards(filepath: str) -> list[Card]:
    return process_csv_file(filepath, convert_row_to_card, 1)


def convert_row_to_card(row: dict[str, str]) -> Optional[Card]:
    if len(row) != 11:
        return None

    try:
        if row["Printing"] not in get_args(Printing):
            return None
        else:
            printing = cast(Printing, row["Printing"])

        return Card(
            row["Card Name"],
            row["Set Code"],
            row["Set Name"],
            row["Card Number"],
            printing,
        )
    except KeyError:
        return None
