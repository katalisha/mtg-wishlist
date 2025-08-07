"""A Store hosted on binderpos.com and the json models required to interact with the API"""

from cards.card import Card, Printing
from pydantic import BaseModel
from typing import Any, ClassVar, Optional
from decimal import Decimal
import httpx
from time import sleep
from stores.store import Store, StockedCard, CardSearchFailure
from datetime import datetime, timedelta
from dataclasses import dataclass
from util.string import snake_to_camel


class Variant(BaseModel):
    title: str
    price: Decimal


class Product(BaseModel):
    """A product in the store inventory"""

    id: str
    title: str
    collector_number: str | None
    variants: list[Variant]

    class Config:
        alias_generator = snake_to_camel


class Inventory(BaseModel):
    products: list[Product]


@dataclass
class BinderStore(Store):
    """A Store subclass using the binderpos.com API"""

    url: str

    requests_blocked_until: ClassVar[Optional[datetime]] = None
    binder_url = "https://portal.binderpos.com/external/shopify/products/forStore"
    avoid_rate_limit = 4  # seconds

    def perform_search_for_card(self, card: Card) -> Optional[StockedCard]:
        if self.rate_limited_to() is not None:
            raise CardSearchFailure

        inventory = self.get_inventory(card)
        sleep(self.avoid_rate_limit)  # TODO: do this better

        if inventory is None:
            return None
        else:
            matching_prices = [
                min([v.price for v in p.variants])
                for p in inventory.products
                if p.collector_number == card.number
            ]

            if len(matching_prices) > 0:
                min_price = min(matching_prices)
                return StockedCard(card, min_price)

    def get_inventory(self, card: Card) -> Optional[Inventory]:
        data = self.build_request_data(card)

        with httpx.Client() as client:
            try:
                response = client.post(self.binder_url, json=data)
                response.raise_for_status()
                return Inventory.parse_raw(response.text)

            except httpx.HTTPStatusError as exc:
                if exc.response.status_code == 429:
                    self.handle_rate_limit(exc.response)
                raise CardSearchFailure from exc

            except httpx.HTTPError as exc:
                raise CardSearchFailure from exc

    def build_request_data(self, card: Card) -> dict[str, Any]:
        return {
            "storeUrl": self.url,
            "game": "mtg",
            "strict": "true",
            "sortTypes": [{"type": "title", "asc": "true", "order": 1}],
            "variants": self.printing_to_variant(card.printing),
            "rarities": [],
            "types": [],
            "setNames": [card.set_name],
            "monsterTypes": [],
            "colors": [],
            "title": card.name,
            "priceGreaterThan": "",
            "priceLessThan": "",
            "instockOnly": "true",
        }

    def handle_rate_limit(self, response: httpx.Response):
        if response.status_code == 429:
            retry_after = int(response.headers["Retry-After"])
            if retry_after != 0:
                BinderStore.requests_blocked_until = datetime.now() + timedelta(
                    seconds=retry_after
                )

    def rate_limited_to(self) -> Optional[datetime]:
        if (
            BinderStore.requests_blocked_until is not None
            and BinderStore.requests_blocked_until > datetime.now()
        ):
            return BinderStore.requests_blocked_until

    def printing_to_variant(self, printing: Printing | None) -> list[str]:
        if printing == "Foil":
            return ["Near Mint Foil"]
        else:
            return ["Near Mint"]
