""" A class that scrapes a URL for info """

from dataclasses import dataclass
from stores.store import Store, StockedCard, CardSearchFailure
from stores.scraper_helper import ScraperHelper
from typing import Optional
from cards.card import Card
from datetime import datetime
import httpx


@dataclass
class Scraper(Store):
    """gets a html page and scrapes it for info"""

    helper: ScraperHelper

    def perform_search_for_card(self, card: Card) -> Optional[StockedCard]:
        url = self.helper.url(card)
        try:
            result = self.get_page(url)

            if result is not None:
                stock = self.helper.find_stock_level(result)
                if stock > 0:
                    price = self.helper.find_price(result)
                    if price is not None:
                        return StockedCard(card, price)
        except CardSearchFailure as exc:
            raise exc

    def rate_limited_to(self) -> Optional[datetime]:
        return None

    def get_page(self, url: str) -> Optional[str]:
        with httpx.Client() as client:
            try:
                response = client.get(url)
                response.raise_for_status()
                return response.text

            except httpx.HTTPStatusError as exc:
                # 404 means card not in stock
                if exc.response.status_code == 404:
                    return None
                else:
                    raise CardSearchFailure from exc

            except httpx.HTTPError as exc:
                raise CardSearchFailure from exc
