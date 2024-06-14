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
import re


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

        if not inventory.products:
            return None

        return self.validate_inventory(card, inventory)

    def build_request_params(self, card: Card) -> dict[str, Any]:
        return {
            "siteId": self.site_id,
            "bgfilter.collection_handle": ["magic-the-gathering-singles", "in-stock"],
            "filter.collection_handle": re.sub("\W+", "-", card.set_name.casefold()),
            "q": f"{card.name}",
            "resultsFormat": "native",
        }

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

    def validate_inventory(
        self, card: Card, inventory: Inventory
    ) -> Optional[StockedCard]:
        def is_foil_product(product: Product) -> bool:
            return product.collection_handle.count("foil") > 0

        def product_matches_number(product: Product, card: Card) -> bool:
            return product.name.find(f"{card.number}") != -1

        def product_matches_printing(product: Product, card: Card) -> bool:
            if card.printing == "Foil" and is_foil_product(product):
                return True
            elif card.printing != "Foil":
                return True
            else:
                return False

        try:
            min_price = min(
                p.price
                for p in inventory.products
                if product_matches_number(p, card) and product_matches_printing(p, card)
            )
            return StockedCard(card, min_price)
        except ValueError:
            return None

    def rate_limited_to(self) -> Optional[datetime]:
        return None
