""" output stuff to the command line """

from stores.store import Store
from cards.card import Card
import datetime
import sys
from util.cli_style import PURPLE, BOLD, END, FAINT, CROSSED, GREEN, RED


class Renderer:
    """Manages output strings"""

    def __init__(self, verbose: bool):
        self.verbose = verbose

    def next_card(self, card: Card, index: int, total: int):
        if self.verbose:
            print(self.card_str(card))
        else:
            progress = index / total
            self.progress_update(progress)

    def done(self, stores: list[Store]):
        if not self.verbose:
            self.progress_update(1)

        self.shopping_list(stores)

    def card_str(self, card: Card) -> str:
        return f"{PURPLE}{BOLD}{card.name}{END} {FAINT}({card.set_name}, {card.number}){END}{END}"

    def card_search_result(self, store: Store, has_card: bool):
        if self.verbose:
            if has_card:
                print(f"{GREEN}\N{check mark} {store.name}{END}")
            else:
                print(
                    f"\N{Multiplication Sign In Double Circle} {CROSSED}{store.name}{END}"
                )

    def progress_update(self, progress: float):
        if not self.verbose:
            bar = "\u2588" * int(progress * 50)
            percentage = progress * 100
            sys.stdout.write(f"\rProgress: [{GREEN}{bar:50s}{END}] {percentage:.0f}%")

    def shopping_list(self, stores: list[Store]):
        for store in stores:
            total = sum(s.price for s in store.cards)
            print(f"\n{BOLD}{store.name}{END}: ${total:.2f}")
            for stock in store.cards:
                print(
                    f"\N{check mark} {self.card_str(stock.card)} @ ${stock.price:.2f}"
                )

    def requests_blocked(self, name: str, until: datetime.datetime):
        diff = until - datetime.datetime.now()
        if diff > datetime.timedelta(seconds=0):
            readable_time = round(diff.total_seconds() / 60)
            message = (
                f"\N{Skull and Crossbones} {RED}{name}"
                + f" requests blocked for {readable_time} minutes{END} \N{Skull and Crossbones}"
            )
            print(message)

    def card_search_error(self, store_name: str, err: str):
        if self.verbose:
            print(f" \N{Skull and Crossbones} {store_name} {FAINT}({err}){END}")
