""" abstract scraper helper class """
from cards.card import Card
from abc import ABC, abstractmethod
from typing import Optional
from decimal import Decimal


class ScraperHelper(ABC):
    """abstract scraper helper for customising the scraper class"""

    @abstractmethod
    def url(self, card: Card) -> str:
        pass

    @abstractmethod
    def find_stock_level(self, result: str) -> int:
        pass

    @abstractmethod
    def find_price(self, result: str) -> Optional[Decimal]:
        pass
