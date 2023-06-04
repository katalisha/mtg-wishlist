""" A Magic Card """

from typing import Literal

Printing = Literal["Normal", "Foil"]


class Card:
    """Card details"""

    def __init__(self, name: str, set_id: str, number: str, printing: Printing):
        self.name = name
        self.set_id = set_id
        self.number = number
        self.printing = printing

    def __repr__(self):
        return f"<{self.name}|{self.set_id}|{self.number}|{self.printing}>"

    def __str__(self) -> str:
        return self.name
