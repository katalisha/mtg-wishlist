"""a store that sells magic cards"""

from cards.card import Card
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal


class CardSearchFailure(Exception):
    pass


@dataclass
class StockedCard:
    card: Card
    price: Decimal


@dataclass
class Store(ABC):
    """Abstract class for stores that sell cards"""

    name: str
    cards: list[StockedCard] = field(default_factory=list[StockedCard], init=False)

    def search_for_card(self, card: Card) -> bool:
        stocked_card = self.perform_search_for_card(card)
        result = stocked_card is not None
        if result:
            self.cards.append(stocked_card)
        return result

    @abstractmethod
    def perform_search_for_card(self, card: Card) -> StockedCard | None:
        pass

    @abstractmethod
    def rate_limited_to(self) -> datetime | None:
        pass
