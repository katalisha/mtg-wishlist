""" A Store hosted on searchspring.com and the json models required to interact with the API """

from cards.card import Card
from pydantic import BaseModel
from typing import Any, Optional
from decimal import Decimal
import httpx
from stores.store import Store, StockedCard, CardSearchFailure
from datetime import datetime
from dataclasses import dataclass, field
from urllib.parse import urlparse


class Product(BaseModel):
    name: str
    collection_handle: list[str]
    price: Decimal


class Inventory(BaseModel):
    products: list[Product]

    class Config:
        fields = {"products": {"alias": "results"}}
        allow_population_by_field_name = True


@dataclass
class SearchSpringStore(Store):
    """A Store subclass using the searchspring.com API"""

    url: str
    site_id: str = field(init=False)
    api_path = "/api/search/search.json"

    def __post_init__(self):
        components = urlparse(self.url)
        if components.hostname is None:
            raise ValueError
        self.site_id = components.hostname.split(".")[0]

    def perform_search_for_card(self, card: Card) -> Optional[StockedCard]:
        inventory = self.get_inventory(card)

        if inventory.products:
            min_price = min(p.price for p in inventory.products)
            return StockedCard(card, min_price)
        else:
            return None

    def get_inventory(self, card: Card) -> Inventory:
        params = self.build_request_params(card)

        with httpx.Client() as client:
            try:
                response = client.get(self.url + self.api_path, params=params)
                response.raise_for_status()
                return Inventory.parse_raw(response.text)

            except httpx.HTTPStatusError as exc:
                raise CardSearchFailure from exc

            except httpx.HTTPError as exc:
                raise CardSearchFailure from exc

    def build_request_params(self, card: Card) -> dict[str, Any]:
        return {
            "siteId": self.site_id,
            "bgfilter.collection_handle": "magic-the-gathering-singles",
            "q": f"{card.number} {card.set_name}",
            "resultsFormat": "native",
        }

    def rate_limited_to(self) -> Optional[datetime]:
        return None
