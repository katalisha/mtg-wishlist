""" A Magic Card """

from typing import Literal
from dataclasses import dataclass

Printing = Literal["Normal", "Foil"]


@dataclass
class Card:
    """Card details"""

    name: str
    set_name: str
    number: str
    printing: Printing
