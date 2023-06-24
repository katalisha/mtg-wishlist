""" A Store hosted on binderpos.com """


from cards.card import Card, Printing
from pydantic import BaseModel
from typing import Any, ClassVar, Optional
from decimal import Decimal
import httpx
from time import sleep
from stores.store import Store, Result, StockedCard
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
    collector_number: str
    variants: list[Variant]

    class Config:
        alias_generator = snake_to_camel

    def min_price(self) -> Decimal:
        return min(v.price for v in self.variants)


class Inventory(BaseModel):
    products: list[Product]


@dataclass
class BinderStore(Store):
    """Store details"""

    url: str

    requests_blocked_until: ClassVar[Optional[datetime]] = None
    binder_url = "https://portal.binderpos.com/external/shopify/products/forStore"
    avoid_rate_limit = 4  # seconds

    def check(self, card: Card) -> Result:
        if self.rate_limited_to() is not None:
            return Result.ERROR

        inventory = self.get_inventory(card)

        if inventory is None:
            return Result.ERROR
        else:
            sleep(self.avoid_rate_limit)  # TODO: do this better

            matches = [
                p for p in inventory.products if p.collector_number == card.number
            ]

            if len(matches) > 0:
                min_price = min(p.min_price() for p in matches)
                self.cards.append(StockedCard(card, min_price))
                return Result.HAS_CARD
            else:
                return Result.NO_HAS_CARD

    def get_inventory(self, card: Card) -> Optional[Inventory]:
        data = self.build_request_data(card)

        with httpx.Client() as client:
            try:
                response = client.post(self.binder_url, json=data)
                response.raise_for_status()
                return Inventory.parse_raw(response.text)

            except httpx.HTTPStatusError:
                self.check_for_rate_limiting(response)  # type: ignore # response is not Unbound when a HTTPStatusError is thrown
                return None

            except (KeyError, httpx.HTTPError):
                return None

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

    def check_for_rate_limiting(self, response: httpx.Response):
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

    def printing_to_variant(self, printing: Printing) -> list[str]:
        if printing == "Foil":
            return ["Near Mint Foil"]
        else:
            return [
                "Near Mint",
                "Lightly Played",
            ]
