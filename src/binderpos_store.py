""" A Store hosted on binderpos.com """


from card import Card, Printing
from dataclasses import dataclass
from dataclasses_json import LetterCase, dataclass_json, config  # type: ignore
from typing import Any, ClassVar, Optional
from decimal import Decimal
import httpx
from time import sleep
from store import Store, Result, StockedCard
from datetime import datetime, timedelta


@dataclass_json(letter_case=LetterCase.CAMEL)  # type: ignore
@dataclass
class Variant:
    title: str
    price: Decimal


@dataclass_json(letter_case=LetterCase.CAMEL)  # type: ignore
@dataclass
class Product:
    dataclass_json_config = config(letter_case=LetterCase.CAMEL)  # type: ignore
    id: str
    title: str
    collector_number: str
    variants: list[Variant]

    def min_price(self) -> Decimal:
        return min(v.price for v in self.variants)


@dataclass_json(letter_case=LetterCase.CAMEL)  # type: ignore
@dataclass
class Inventory:
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
                return Inventory.from_json(response.text, parse_float=Decimal)  # type: ignore # dataclasses_json from_json confuses pylance

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
