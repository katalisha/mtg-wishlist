""" output stuff to the command line """

from store import Store, Result
from card import Card
import datetime
import sys

# ANSI color codes
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"


class Outputter:
    """Manages output strings"""

    def __init__(self, verbose: bool):
        self.verbose = verbose

    def card(self, card: Card):
        if self.verbose:
            print(self.card_str(card))

    def card_str(self, card: Card) -> str:
        return f"{PURPLE}{BOLD}{card.name}{END} {FAINT}({card.set_name}, {card.number}){END}{END}"

    def store_has_card(self, store: Store, has_card: Result):
        if self.verbose:
            return self.verbose_store_has_card(store, has_card)

    def verbose_store_has_card(self, store: Store, has_card: Result):
        match has_card:
            case Result.HAS_CARD:
                print(f"{GREEN}\N{check mark} {store.name}{END}")
            case Result.NO_HAS_CARD:
                print(
                    f"\N{Multiplication Sign In Double Circle} {CROSSED}{store.name}{END}"
                )
            case Result.ERROR:
                print(f" \N{Skull and Crossbones} {store.name}")

    def requests_blocked(self, name: str, until: datetime.datetime):
        diff = until - datetime.datetime.now()
        if diff > datetime.timedelta(seconds=0):
            readable_time = round(diff.total_seconds() / 60)
            message = (
                f"\N{Skull and Crossbones} {RED}{name}"
                + f" requests blocked for {readable_time} minutes{END} \N{Skull and Crossbones}"
            )
            print(message)

    def shopping_list(self, stores: list[Store]):
        for store in stores:
            print(store.name)
            for stock in store.cards_found():
                print(self.card_str(stock.card) + f" @ ${stock.price}")

    def progress_bar(self, progress: float):
        if not self.verbose:
            bar = "\u2588" * int(progress * 50)
            percentage = progress * 100
            sys.stdout.write(f"\rProgress: [{GREEN}{bar:50s}{END}] {percentage:.0f}%")

            if progress >= 1:
                print()
