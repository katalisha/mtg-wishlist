""" a store that sells magic cards """

from card import Card
from enum import Enum
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


class Result(Enum):
    HAS_CARD = 1
    NO_HAS_CARD = 2
    ERROR = 3


@dataclass
class Store(ABC):
    name: str

    @abstractmethod
    def check(self, card: Card) -> Result:
        pass

    @abstractmethod
    def rate_limited_to(self) -> datetime:
        pass
