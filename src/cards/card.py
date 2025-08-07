"""A Magic Card"""

from typing import Literal
from dataclasses import dataclass

Printing = Literal["Normal", "Foil"]


@dataclass
class Card:
    name: str
    set_code: str
    set_name: str
    number: str
    printing: Printing | None
