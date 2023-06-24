""" a store that sells magic cards """

from cards.card import Card
from enum import Enum
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class StockedCard:
    card: Card
    price: Decimal


class Result(Enum):
    HAS_CARD = 1
    NO_HAS_CARD = 2
    ERROR = 3


@dataclass
class Store(ABC):
    """A store that sells cards"""

    name: str
    cards: list[StockedCard] = field(default_factory=list, init=False)

    @abstractmethod
    def check(self, card: Card) -> Result:
        pass

    @abstractmethod
    def rate_limited_to(self) -> Optional[datetime]:
        pass
