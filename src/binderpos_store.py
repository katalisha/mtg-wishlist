""" A Store hosted on binderpos.com """


from card import Card, Printing
from dataclasses import dataclass, field
from dataclasses_json import LetterCase, dataclass_json, config
from typing import Any, ClassVar
from decimal import Decimal
import httpx
from time import sleep
from store import Store, Result, StockedCard
from datetime import datetime, timedelta
from functools import reduce
from operator import attrgetter


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Variant:
    title: str
    price: Decimal


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Product:
    dataclass_json_config = config(letter_case=LetterCase.CAMEL)
    id: str
    title: str
    collector_number: str
    variants: list[Variant]


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Inventory:
    products: list[Product]


@dataclass
class BinderStore(Store):
    """Store details"""

    url: str

    requests_blocked_until: ClassVar[datetime | None] = None
    binder_url = "https://portal.binderpos.com/external/shopify/products/forStore"
    avoid_rate_limit = 4  # seconds

    def check(self, card: Card) -> Result:
        if self.rate_limited_to() is not None:
            return Result.ERROR

        data = self.build_request_data(card)
        inventory = self.send_request(data)

        if inventory is None:
            return Result.ERROR
        else:
            sleep(self.avoid_rate_limit)  # TODO: do this better
            matches = filter(
                lambda p: (p.collector_number == card.number), inventory.products
            )
            if len(list(matches)) > 0:
                return Result.HAS_CARD
            else:
                return Result.NO_HAS_CARD

    def send_request(self, data) -> Inventory | None:
        with httpx.Client() as client:
            try:
                response = client.post(self.binder_url, json=data)
                response.raise_for_status()
                body: Inventory = Inventory.from_json(response.text)  # type: ignore
                return body
            except httpx.HTTPStatusError:
                self.check_for_rate_limiting(response)  # type: ignore
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

    def rate_limited_to(self) -> datetime | None:
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
