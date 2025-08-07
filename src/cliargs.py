"""validate cli args and return them"""

from argparse import ArgumentParser
from typing import NamedTuple


class Args(NamedTuple):
    wishlist: str
    storelist: str
    htf: str | None
    verbose: bool


def process_args() -> Args:
    parser = ArgumentParser(
        prog="mtg wishlist",
        description="Searches stores for a wishlist of cards",
    )
    parser.add_argument(
        "-w",
        "--wishlist",
        help="the filepath for the dragon shield wishlist export file",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-s",
        "--storelist",
        help="the filepath for list of stores to search",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-f",
        "--htf",
        help="list of hard to find cards to highlight in the results",
        type=str,
        required=False,
    )
    parser.add_argument("-v", "--verbose", action="store_true")

    args: Args = parser.parse_args()  # type: ignore
    return args
